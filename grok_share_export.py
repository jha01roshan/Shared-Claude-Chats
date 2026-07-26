#!/usr/bin/env python3
"""Export grok.com share links to markdown transcripts.

Usage:
    grok_share_export.py <url-or-share-id> [...] [-o OUTDIR]
    grok_share_export.py links.txt [-o OUTDIR]
    grok_share_export.py -f links.txt [-o OUTDIR]

A links file is newline-delimited; blank lines and #-comments are ignored.

Re-running the same links file is cheap: a manifest records what has already
been exported, and known conversations are skipped before any network
request. Use --force to re-fetch them.

The manifest survives tidying up: it is looked for in the output directory
and then just above it, and a recorded transcript that has been moved into a
subdirectory is still recognised (and its new location recorded) rather than
being downloaded a second time.

The share page is an empty SPA shell that loads the conversation from
/rest/app-chat/share_links_data/<id>, so this reads that endpoint directly.
It is public -- no credentials -- but sits behind a Cloudflare check that
fingerprints TLS rather than headers, which is why this uses curl_cffi
(browser TLS impersonation) instead of plain requests.

This is the grok sibling of claude_share_export.py; the CLI and manifest
format match, but the two keep separate manifests.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

try:
    from curl_cffi import requests as cffi_requests
except ImportError:  # pragma: no cover - dependency hint
    sys.exit("error: curl_cffi is required. Install it with: pip install curl_cffi")

API_URL = "https://grok.com/rest/app-chat/share_links_data/{share_id}"
SHARE_URL = "https://grok.com/share/{share_id}"
UUID = r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
# Share ids look like "c2hhcmQtNA_<uuid>" -- a base64 shard tag, an underscore,
# then the conversation UUID. The tag is optional and case-sensitive (it is
# base64), so unlike the UUID it must never be normalised.
SHARE_ID_RE = re.compile(rf"(?:[A-Za-z0-9_=-]{{1,64}}_)?{UUID}")
IMPERSONATE = "chrome"
TIMEOUT = 30
MAX_SLUG = 80
MANIFEST_NAME = ".grok-share-export.json"


class ExportError(Exception):
    """A single link failed; the batch continues."""


def extract_share_id(raw: str) -> str:
    """Pull the share id out of a share URL or a bare id."""
    match = SHARE_ID_RE.search(raw.strip())
    if not match:
        raise ExportError(
            "no share id found -- expected https://grok.com/share/<id> or a bare id"
        )
    return match.group(0)


def fetch_snapshot(share_id: str) -> dict:
    """Fetch the conversation JSON behind a public share link."""
    try:
        response = cffi_requests.get(
            API_URL.format(share_id=share_id),
            impersonate=IMPERSONATE,
            timeout=TIMEOUT,
            headers={"Accept": "*/*", "Referer": SHARE_URL.format(share_id=share_id)},
        )
    except Exception as exc:
        raise ExportError(f"network error: {type(exc).__name__}: {exc}") from exc

    if response.status_code == 404:
        raise ExportError("not found -- the share was deleted, revoked, or never public")
    if response.status_code in (401, 403):
        # 401 here means the id was rejected as a public share, not that we
        # need to log in: the endpoint takes no credentials.
        raise ExportError(
            f"HTTP {response.status_code} -- the share is not public, or TLS "
            "impersonation was rejected (try upgrading curl_cffi)"
        )
    if response.status_code != 200:
        raise ExportError(f"unexpected HTTP {response.status_code}")

    try:
        payload = response.json()
    except Exception as exc:
        raise ExportError("response was not JSON (likely a challenge page)") from exc

    if not isinstance(payload, dict):
        raise ExportError("unexpected JSON shape (expected an object)")
    return payload


def _quote(text: str) -> str:
    return "\n".join(f"> {line}" for line in text.splitlines())


def _thinking_text(response: dict) -> str:
    """Flatten the `steps` list -- grok's thinking and tool-use trace."""
    parts: list[str] = []
    for step in response.get("steps") or []:
        if not isinstance(step, dict):
            continue
        tags = [t for t in (step.get("tags") or []) if isinstance(t, str)]
        text = "\n".join(t for t in (step.get("text") or []) if isinstance(t, str))
        text = text.strip()
        if not text:
            # A step with no text still says something happened; name it.
            if tags:
                parts.append(f"_[{', '.join(tags)}]_")
            continue
        label = tags[0] if tags else "step"
        parts.append(f"**{label}**\n\n{text}")
    if not parts:
        return ""
    return "> **Thinking**\n>\n" + _quote("\n\n".join(parts))


def _sources(response: dict) -> list[str]:
    """Web pages and X posts the answer drew on, cited ones preferred."""
    results = response.get("citedWebSearchResults") or response.get("webSearchResults")
    lines = []
    for item in results or []:
        if not isinstance(item, dict):
            continue
        url = item.get("url")
        if not url:
            continue
        title = (item.get("title") or "").strip() or url
        lines.append(f"- [{title}]({url})")

    posts = response.get("citedXposts") or response.get("xposts")
    for item in posts or []:
        if not isinstance(item, dict):
            continue
        handle = item.get("username") or item.get("screenName") or ""
        post_id = item.get("postId") or item.get("id") or ""
        text = (item.get("text") or "").strip().replace("\n", " ")
        if post_id and handle:
            lines.append(f"- [@{handle}](https://x.com/{handle}/status/{post_id})")
        elif text:
            lines.append(f"- x post: {text[:120]}")
    return lines


def _attachment_names(response: dict) -> list[str]:
    names: list[str] = []
    for key in ("fileAttachmentsMetadata", "fileAttachmentAssetMetadata"):
        for item in response.get(key) or []:
            if isinstance(item, dict):
                name = item.get("fileName") or item.get("file_name") or item.get("name")
                if name:
                    names.append(str(name))
    for key in ("fileAttachments", "fileUris", "imageAttachments"):
        for item in response.get(key) or []:
            if isinstance(item, str) and item:
                names.append(item.rsplit("/", 1)[-1])
            elif isinstance(item, dict):
                name = item.get("fileName") or item.get("name") or item.get("fileUri")
                if name:
                    names.append(str(name).rsplit("/", 1)[-1])
    # Dedupe, keep order.
    seen: set[str] = set()
    return [n for n in names if not (n in seen or seen.add(n))]


def render_markdown(
    snapshot: dict, share_id: str, include_thinking: bool, include_sources: bool
) -> tuple[str, int]:
    """Render the snapshot as a markdown transcript. Returns (text, message_count)."""
    conversation = snapshot.get("conversation")
    conversation = conversation if isinstance(conversation, dict) else {}
    title = (conversation.get("title") or "").strip() or "Untitled Grok conversation"
    created = (conversation.get("createTime") or "")[:10]
    responses = [r for r in (snapshot.get("responses") or []) if isinstance(r, dict)]
    # The API returns them in order; createTime is the tiebreak, and enumerate
    # keeps that original order stable when timestamps collide.
    responses = [
        r
        for _, r in sorted(
            enumerate(responses), key=lambda pair: (pair[1].get("createTime") or "", pair[0])
        )
    ]

    models = []
    for response in responses:
        model = (response.get("model") or "").strip()
        if model and model not in models:
            models.append(model)

    lines = [f"# {title}", ""]
    lines.append(f"- Source: {SHARE_URL.format(share_id=share_id)}")
    if created:
        lines.append(f"- Created: {created}")
    if models:
        lines.append(f"- Model: {', '.join(models)}")
    lines.append(f"- Messages: {len(responses)}")

    if not responses:
        lines += ["", "---", "", "_This share contains no messages._"]
        return "\n".join(lines) + "\n", 0

    for response in responses:
        sender = (response.get("sender") or "").lower()
        label = {"human": "Human", "assistant": "Assistant"}.get(
            sender, sender.title() or "Unknown"
        )
        # The rule matters: message bodies carry their own #/## headings, so
        # without it a turn boundary is indistinguishable from in-message structure.
        lines += ["", "---", "", f"## {label}", ""]

        if include_thinking:
            thinking = _thinking_text(response)
            if thinking:
                lines += [thinking, ""]

        body = (response.get("message") or "").strip()
        lines.append(body if body else "_[empty message]_")

        for url in response.get("generatedImageUrls") or []:
            if isinstance(url, str) and url:
                lines += ["", f"![generated image]({url})"]

        names = _attachment_names(response)
        if names:
            lines += ["", f"_Attachments: {', '.join(names)}_"]

        if include_sources:
            sources = _sources(response)
            if sources:
                lines += ["", "_Sources:_", ""] + sources

    return "\n".join(lines) + "\n", len(responses)


def slugify(text: str, fallback: str) -> str:
    """Filesystem-safe slug that preserves non-Latin scripts."""
    normalised = unicodedata.normalize("NFC", text or "")
    kept = []
    for char in normalised:
        if char.isalnum():
            kept.append(char)
        elif char in " -_.":
            kept.append("-")
        # Everything else (path separators, control chars, punctuation) is dropped.
    slug = re.sub(r"-+", "-", "".join(kept)).strip("-")
    return slug[:MAX_SLUG].strip("-") or fallback


def unique_path(directory: Path, slug: str) -> Path:
    """Never overwrite an existing export."""
    candidate = directory / f"{slug}.md"
    counter = 2
    while candidate.exists():
        candidate = directory / f"{slug}-{counter}.md"
        counter += 1
    return candidate


def read_link_file(path: Path) -> list[str]:
    """Newline-delimited links; blank lines and #-comments ignored."""
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ExportError(f"cannot read {path}: {exc}") from exc
    links = []
    for line in raw.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            links.append(line)
    return links


def collect_links(positionals: list[str], link_files: list[str]) -> list[str]:
    """Positionals may be links or a path to a links file."""
    links: list[str] = []
    for item in positionals:
        candidate = Path(item)
        if not SHARE_ID_RE.search(item) and candidate.is_file():
            links.extend(read_link_file(candidate))
        else:
            links.append(item)
    for item in link_files:
        links.extend(read_link_file(Path(item)))
    return links


class Manifest:
    """The record of what has already been exported, and where it landed.

    This is what makes a re-run cheap: a share id listed here whose transcript
    is still on disk is never requested from the network again.
    """

    def __init__(self, path: Path, outdir: Path, entries: dict):
        self.path = path
        self.outdir = outdir
        self.entries = entries
        self.dirty = False
        self._by_name: dict[str, Path] | None = None

    @classmethod
    def load(cls, outdir: Path) -> "Manifest":
        """Find and read the manifest governing this output directory.

        A missing or unreadable manifest is not an error -- it just means
        nothing is known yet, so everything gets fetched.
        """
        path = cls._locate(outdir)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return cls(path, outdir, {})
        entries = data.get("exports") if isinstance(data, dict) else None
        return cls(path, outdir, entries if isinstance(entries, dict) else {})

    @staticmethod
    def _locate(outdir: Path) -> Path:
        """Prefer a manifest in outdir, else one just above it.

        Transcripts get tidied into a subdirectory after the fact, leaving the
        manifest behind in the parent. Starting a fresh manifest in the new
        directory would re-download every conversation the old one knows about,
        so an existing one within two levels up is adopted instead.
        """
        here = outdir / MANIFEST_NAME
        if here.exists():
            return here
        for parent in list(outdir.resolve().parents)[:2]:
            candidate = parent / MANIFEST_NAME
            if candidate.exists():
                return candidate
        return here

    def _index(self) -> dict[str, Path]:
        """Lazily map transcript filename -> location, one level deep.

        Built only when a recorded path has gone missing, which is the moved-
        into-a-subdirectory case.
        """
        if self._by_name is not None:
            return self._by_name
        index: dict[str, Path] = {}
        roots = {self.outdir, self.path.parent}
        for root in roots:
            for child in self._listdir(root):
                if child.is_dir():
                    if not child.name.startswith("."):
                        for grandchild in self._listdir(child):
                            if grandchild.suffix == ".md" and grandchild.is_file():
                                index.setdefault(grandchild.name, grandchild)
                elif child.suffix == ".md":
                    index.setdefault(child.name, child)
        self._by_name = index
        return index

    @staticmethod
    def _listdir(directory: Path) -> list[Path]:
        try:
            return sorted(directory.iterdir())
        except OSError:
            return []

    def lookup(self, share_id: str) -> Path | None:
        """The already-exported file for this share id, if it is still on disk."""
        entry = self.entries.get(share_id)
        if not isinstance(entry, dict):
            return None
        name = entry.get("file")
        if not name:
            return None
        for base in (self.path.parent, self.outdir):
            candidate = base / name
            if candidate.exists():
                return candidate
        # Recorded but not where it was left: find it by name before concluding
        # it needs fetching again. If it is genuinely gone, so is the cache hit.
        return self._index().get(Path(name).name)

    def messages(self, share_id: str) -> int:
        entry = self.entries.get(share_id)
        return (entry.get("messages") or 0) if isinstance(entry, dict) else 0

    def _record_name(self, path: Path) -> str:
        """Store the location relative to the manifest, so moves stay legible."""
        try:
            return path.resolve().relative_to(self.path.parent.resolve()).as_posix()
        except ValueError:
            return path.name

    def note_location(self, share_id: str, path: Path) -> None:
        """Point a stale entry at where its transcript actually lives now."""
        entry = self.entries.get(share_id)
        if not isinstance(entry, dict):
            return
        name = self._record_name(path)
        if entry.get("file") != name:
            entry["file"] = name
            self.dirty = True

    def record(self, share_id: str, path: Path, snapshot: dict, count: int) -> None:
        conversation = snapshot.get("conversation")
        conversation = conversation if isinstance(conversation, dict) else {}
        self.entries[share_id] = {
            "file": self._record_name(path),
            "title": (conversation.get("title") or "").strip(),
            "messages": count,
            "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        self.dirty = True

    def save(self) -> None:
        if not self.dirty:
            return
        payload = {"version": 1, "exports": self.entries}
        try:
            self.path.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
        except OSError as exc:
            # Losing the manifest degrades caching but must not lose transcripts.
            print(f"warning: could not write manifest: {exc}", file=sys.stderr)
        else:
            self.dirty = False


def export_one(
    link: str,
    outdir: Path,
    include_thinking: bool,
    include_sources: bool,
    manifest: Manifest,
    force: bool,
) -> tuple[str, Path, int]:
    """Returns (status, path, message_count) where status is 'written' or 'skipped'."""
    share_id = extract_share_id(link)

    existing = manifest.lookup(share_id)
    if existing is not None and not force:
        # The whole point: no network request for something we already have.
        manifest.note_location(share_id, existing)
        return "skipped", existing, manifest.messages(share_id)

    snapshot = fetch_snapshot(share_id)
    markdown, count = render_markdown(
        snapshot, share_id, include_thinking, include_sources
    )

    if existing is not None:
        # Refreshing a known conversation replaces it rather than piling up -2, -3.
        path = existing
    else:
        conversation = snapshot.get("conversation")
        title = conversation.get("title") if isinstance(conversation, dict) else ""
        slug = slugify(title or "", share_id.rsplit("_", 1)[-1])
        path = unique_path(outdir, slug)
    path.write_text(markdown, encoding="utf-8")

    manifest.record(share_id, path, snapshot, count)
    return "written", path, count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Save grok.com share links as markdown transcripts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  %(prog)s https://grok.com/share/<id>\n"
            "  %(prog)s links.txt -o out/\n"
            "  %(prog)s -f links.txt -o out/\n"
        ),
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        metavar="LINK|FILE",
        help="share URLs, bare share ids, or a path to a newline-delimited links file",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="append",
        default=[],
        metavar="FILE",
        help="read links from FILE (repeatable)",
    )
    parser.add_argument(
        "-o",
        "--out",
        default=".",
        metavar="DIR",
        help="output directory (default: current directory)",
    )
    parser.add_argument(
        "--include-thinking",
        action="store_true",
        help="include grok's thinking and tool-use steps",
    )
    parser.add_argument(
        "--include-sources",
        action="store_true",
        help="include web and X sources cited by each answer",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="re-fetch conversations already exported to DIR, replacing them",
    )
    args = parser.parse_args()

    if not args.inputs and not args.file:
        parser.error("no links given")

    try:
        links = collect_links(args.inputs, args.file)
    except ExportError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    # Dedupe by share id where possible so a messy file does not write twice.
    seen: set[str] = set()
    ordered: list[str] = []
    for link in links:
        match = SHARE_ID_RE.search(link)
        key = match.group(0) if match else link
        if key not in seen:
            seen.add(key)
            ordered.append(link)

    if not ordered:
        print("error: no links found", file=sys.stderr)
        return 1

    outdir = Path(args.out)
    try:
        outdir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create {outdir}: {exc}", file=sys.stderr)
        return 1

    manifest = Manifest.load(outdir)
    if manifest.entries:
        print(f"manifest: {manifest.path} ({len(manifest.entries)} already exported)")

    failures: list[tuple[str, str]] = []
    written = skipped = 0

    for link in ordered:
        try:
            status, path, count = export_one(
                link,
                outdir,
                args.include_thinking,
                args.include_sources,
                manifest,
                args.force,
            )
        except ExportError as exc:
            failures.append((link, str(exc)))
            print(f"failed {link}: {exc}", file=sys.stderr)
        except OSError as exc:
            failures.append((link, str(exc)))
            print(f"failed {link}: cannot write output: {exc}", file=sys.stderr)
        else:
            if status == "skipped":
                skipped += 1
                print(f"skipped {path} (already exported)")
            else:
                written += 1
                print(f"wrote {path} ({count} messages)")
                # Persist as we go so an interrupted batch keeps its progress.
                manifest.save()

    # Skips can still have corrected stale paths worth keeping.
    manifest.save()

    summary = f"{written} written, {skipped} skipped"
    if failures:
        print(f"\n{summary}, {len(failures)} of {len(ordered)} failed", file=sys.stderr)
        return 1
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
