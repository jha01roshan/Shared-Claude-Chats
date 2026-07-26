# PSVR2 Setup on Bazzite Explained

- Source: https://grok.com/share/c2hhcmQtMw_bb6b9d03-1d4c-4663-a095-4f46b2d1792c
- Created: 2026-01-27
- Model: grok-4-auto, grok-4
- Messages: 4

---

## Human

How can I use my PSVR2 headset on Bazzite?

---

## Assistant

**Using PSVR2 on Bazzite is experimental and relies on the open-source Monado OpenXR runtime (not official Sony support, which is Windows-only via the PlayStation VR2 App and PC Adapter).** It enables basic VR functionality with SteamVR, including head and controller tracking for PCVR games, but features like hand/eye tracking and haptics are partial or WIP.<grok:render card_id="312ad3" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render><grok:render card_id="781a5c" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render><grok:render card_id="f635c8" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">39</argument>
</grok:render>

### Requirements
| Category | Details |
|----------|---------|
| **Hardware** | - PSVR2 headset + official **PC Adapter** (required; ~$60 from Sony—provides USB upstream to PC + DisplayPort out).<grok:render card_id="4622b4" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">116</argument>
</grok:render><grok:render card_id="9d4159" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render><br>- GPU with **DisplayPort 1.4** (DSC support needed; e.g., RTX 30-series+, RX 6000+).<br>- **USB 3.2 Gen 2x2** port for adapter.<br>- Reliable Bluetooth 5.0+ adapter/dongle for Sense controllers (built-in may work inconsistently).<grok:render card_id="cb6077" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render> |
| **Firmware** | Update PSVR2 to latest via PS5 (or Windows PC for PC mode unlock). |
| **PC Specs** | High-end: e.g., Ryzen 9, RX 7900+ as tested; 16GB+ RAM.<grok:render card_id="8fd310" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render> |
| **Software** | Bazzite (SteamVR pre-installed); Monado (via Distrobox/Envision). |

**Notes:** No native cinema mode without adapter on most GPUs. AMD GPUs may need EDID overrides.<grok:render card_id="70e1e7" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render>

### Step-by-Step Setup on Bazzite
1. **Install Distrobox & Envision (Monado installer):**
   - Bazzite is immutable, so use Distrobox for packages.
   - Open **Decky Loader** or Konsole: Install Distrobox if needed (`ujust install distrobox`).
   - Create Fedora container: `distrobox create --name fedora-vr --image fedora:41`.
   - Enter: `distrobox enter fedora-vr`.
   - Inside: `sudo dnf install envision mesa-libGL-devel` (fix conflicts if any, e.g., via `rpm --erase` for duplicates).<grok:render card_id="afa955" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">81</argument>
</grok:render><grok:render card_id="285887" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">83</argument>
</grok:render>
   - Run `envision`—it auto-installs/configures Monado + compositor.

2. **Connect Hardware:**
   - Power on PSVR2 (white light).
   - Plug: Headset USB-C → PC Adapter → USB to PC + DP cable to GPU DP port.
   - Pair controllers via Bluetooth (they appear as `/dev/input/js*`).<grok:render card_id="d159bc" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render>

3. **Configure SteamVR for Monado:**
   - Launch SteamVR (via Gamescope/Steam).
   - SteamVR Settings > **OpenXR** tab: Set **OpenXR Runtime** to Monado (path: `~/.local/share/flatpak/...` or Distrobox mount).
   - Restart SteamVR—PSVR2 should show in dashboard with tracking.<grok:render card_id="17cbc4" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render><grok:render card_id="f9a90a" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">125</argument>
</grok:render>

4. **Launch VR Games:**
   - SteamVR games: Native OpenXR works; OpenVR via xrizer/OpenComposite.
   - Proton games: Add launch option `PROTON_USE_WINED3D=1 %command%` or use mods (e.g., MechWarrior 5 VR mod).<grok:render card_id="eadc41" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render>
   - Tested: Overload, MechWarrior 5 (head/controller tracking, 6DoF).

5. **Troubleshoot:**
   | Issue | Fix |
   |-------|-----|
   | No detection | Run `vrstartup` in terminal; ensure X11 (not Wayland).<grok:render card_id="f1e05e" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">79</argument>
</grok:render> |
   | Dep conflicts | In Distrobox: `sudo dnf swap mesa-libGL-devel` or remove old pkgs.<grok:render card_id="6771b5" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">85</argument>
</grok:render> |
   | Low perf/latency | `CAP_SYS_NICE` on monado-service; NVIDIA: `nvidia-modeset.conceal_vrr_caps=1` in GRUB.<grok:render card_id="499dad" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">125</argument>
</grok:render> |
   | Controllers | Power on before Monado; test in `jstest /dev/input/js0`. |

### Limitations & Alternatives
- **Experimental:** Bugs in tracking, no full hand/eye (WIP), no official Sony app (Proton reports poor).<grok:render card_id="348f04" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render><grok:render card_id="f87e93" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">113</argument>
</grok:render>
- **Bazzite Notes:** Works via Distrobox (no native packages); SteamVR solid, but test hardware compat.<grok:render card_id="59350d" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">114</argument>
</grok:render>
- **Alternatives:**
  | Method | Pros/Cons |
  |--------|-----------|
  | **Wine + PSVR2 Toolkit** | Windows drivers via Wine RPC; 1:1 tracking prototype (Sep 2025)—very hacky, broken.<grok:render card_id="d733d4" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">30</argument>
</grok:render> |
  | **Dual-boot Windows** | Full official support. |
  | **Proton PSVR2 App** | Crashes/fails setup; not viable.<grok:render card_id="ece56f" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">113</argument>
</grok:render> |

Join Monado Discord/GitLab for PSVR2 channel/help. Test on non-Bazzite Linux first if possible. Success varies by GPU/BT—report on r/Bazzite or Universal Blue Discourse!<grok:render card_id="ff5b9e" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">44</argument>
</grok:render>

---

## Human

At step 1, when I run "envision", it opens a window. When I click Start, it opens a screen but it's black. There's a "SteamVR Quick Calibration", but when I click calibrate, it says "SteamVR not found", despite it being installed and running

---

## Assistant

**The black screen after clicking "Start" in Envision is completely normal and indicates success.**<grok:render card_id="8fff54" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">58</argument>
</grok:render><grok:render card_id="2ba28f" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">59</argument>
</grok:render> Monado's compositor/runtime launches without a built-in launcher or viewer app (unlike SteamVR), so the headset display stays black until you connect hardware and launch a VR app/game. You can safely close the black screen or leave Envision running—proceed to step 2.

**"SteamVR not found" during Quick Calibration is a common Flatpak/container issue on Bazzite and can be skipped.**<grok:render card_id="cc00c9" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">58</argument>
</grok:render> This feature auto-runs SteamVR's room setup for convenience (e.g., floor height/chaperone), but it's **optional**—especially for inside-out tracking like PSVR2 (no base stations needed). Envision can't detect your host's Flatpak SteamVR from inside Distrobox.

### Quick Fixes to Proceed
1. **Apply Flatseal overrides to Steam Flatpak** (critical for SteamVR to access Monado files):<grok:render card_id="8aa5ba" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">58</argument>
</grok:render>
   - Install Flatseal: `flatpak install flathub com.github.tchx84.Flatseal`
   - Open Flatseal > Select **com.valvesoftware.Steam** > **Filesystem** tab > Add these **one by one** (Other files):
     | Path | Permissions |
     |------|-------------|
     | `xdg-data/envision:ro` | Read-only |
     | `xdg-run/monado_comp_ipc` | Read/Write |
     | `xdg-config/openxr:ro` | Read-only |
     | `xdg-config/openvr:ro` | Read-only |
     | `~/.local/share/envision:ro` | Read-only (backup if issues) |
   - Close/relaunch Steam.

2. **(Optional) Manually register Monado SteamVR driver** if SteamVR doesn't detect PSVR2 hardware later:
   - In Distrobox (`distrobox enter fedora-vr`), build finishes with Envision—note the SteamVR plugin path (usually `~/.local/share/steamvr-monado`).
   - On **host** (exit Distrobox): Find vrpathreg:
     ```
     find ~/.var/app/com.valvesoftware.Steam -name "*vrpathreg*" 2>/dev/null
     ```
     Typical: `~/.var/app/com.valvesoftware.Steam/data/Steam/steamapps/common/SteamVR/bin/linux64/vrpathreg`
   - `cd` to its **dir**, run:
     ```
     ./vrpathreg adddriver ~/.local/share/steamvr-monado
     ```
     (Adjust path if different; rerun `find ~/.local/share -name "steamvr-monado"` in Distrobox).<grok:render card_id="a7e846" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">63</argument>
</grok:render><grok:render card_id="78352a" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">57</argument>
</grok:render>

3. **Switch to X11 session** (SteamVR/Monado prefers it over Wayland):
   - Log out > Gear icon > Select "GNOME on Xorg" > Log in.
   - Relaunch everything.

### Updated Full Flow (Post-Envision)
- Keep Envision "built/installed" (don't uninstall).
- **Step 2:** Connect PSVR2 + PC Adapter (USB/DP). Power on headset/controllers **before** starting Envision/Monado.<grok:render card_id="e47439" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">59</argument>
</grok:render>
- In Distrobox: `envision` > Start (black=OK).
- **Host:** Launch SteamVR > Settings > **OpenXR** tab:
  - Active Runtime: Select **Monado** (`~/.local/share/monado/openxr/1/active_runtime.json` or similar—refresh if missing).<grok:render card_id="0d2063" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">59</argument>
</grok:render>
  - PSVR2 should appear (head/controllers tracking).
- Test: Launch OpenXR VR game (e.g., add `PROTON_ENABLE_NVAPI=1 %command%` if NVIDIA/Proton).

### Common Next Issues & Fixes
| Issue | Fix |
|-------|-----|
| **No PSVR2 detection** | USB 3.2 Gen2x2 port; `lsusb` shows Sony? Update Monado: Rerun Envision build. Firmware latest via PS5.<grok:render card_id="c815d8" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">80</argument>
</grok:render> |
| **mesa-libGL-devel conflict** (if rebuild fails) | In Distrobox: `sudo dnf copp` enable Bazzite COPR; or `sudo rpm-ostree override replace mesa-libGL --from repo=updates-archive` (reboot).<grok:render card_id="0806c1" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">46</argument>
</grok:render> |
| **Low perf/tracking jitter** | AMD: `sudo setcap cap_sys_nice+eip $(which monado-service)`.<br>NVIDIA: GRUB `nvidia-modeset.conceal_vrr_caps=1`; disable monitor VRR.<grok:render card_id="084854" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">59</argument>
</grok:render> |
| **PSVR2 blocked on Bazzite** (recent reports) | Immutable/kernel quirks—try `ujust update` or wait Monado update. Dual-boot Windows as fallback.<grok:render card_id="597dad" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">25</argument>
</grok:render> |

**PSVR2 works experimentally on Linux/Monado (head/controller tracking, SteamVR games like HL:Alyx tested).** No dedicated Envision profile (auto-detected via USB), but haptics/eye-tracking WIP.<grok:render card_id="3ea11d" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">87</argument>
</grok:render> If stuck, post logs (`monado-service -vv`) on r/Bazzite, Universal Blue Discourse, or Monado Discord (PSVR2 channel). Success rate high on AMD/high-end GPUs!<grok:render card_id="390950" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">26</argument>
</grok:render>
