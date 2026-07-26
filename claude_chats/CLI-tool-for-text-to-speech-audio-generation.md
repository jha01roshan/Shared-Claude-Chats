# CLI tool for text-to-speech audio generation

- Source: https://claude.ai/share/2e01ad60-ca38-4e14-ab60-74eaa45b2fbd
- Author: Simon
- Created: 2026-01-22
- Messages: 4

---

## Human

Build a CLI tool for generating audio

uv run tool.py "say this text out loud"

Defaults to saving to output.wav - or output-2.wav etc if that filename mistaken 

-o saved.wav to control the filename

-l/--language X for language, default to English

-i/--instruct "deep low voice" to influence the voice 

You can also pipe content to it instead of passing a string as a positional argument 

Needs to depend on 
mlx-audio==0.3.0rc1

---

## Assistant

Looking at the screenshot, I can see this is using the `mlx_audio` library with the Qwen3-TTS model. Let me build a CLI tool based on this pattern.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's your CLI tool. It supports:

- **Positional text argument**: `uv run tool.py "say this text out loud"`
- **Piped input**: `echo "hello world" | uv run tool.py`
- **Custom output file**: `-o saved.wav`
- **Language selection**: `-l Chinese` or `--language Spanish`
- **Voice instruction**: `-i "deep low voice"` or `--instruct "A calm, soothing female voice"`
- **Auto-increment filenames**: If `output.wav` exists, it saves to `output-2.wav`, `output-3.wav`, etc. (only for the default filename)

---

## Human

Add a -v/--verbose option

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. The tool now runs silently by default and shows progress messages only with `-v`/`--verbose`.
