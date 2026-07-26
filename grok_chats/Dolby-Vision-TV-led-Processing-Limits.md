# Dolby Vision TV-led Processing Limits

- Source: https://grok.com/share/bGVnYWN5_989bdedf-7204-4513-be35-cd86c922c451
- Created: 2025-05-28
- Messages: 2

---

## Human

can TV sets that support TV-led Dolby vision input and process, can also do TV-led processing for the Full enhancement layer of Profile 7?

---

## Assistant

To address whether TV sets that support TV-led Dolby Vision input and processing can also handle TV-led processing for the Full Enhancement Layer (FEL) of Profile 7, let’s break down the key concepts and provide a clear answer based on available information.

### Understanding Dolby Vision and Profile 7
Dolby Vision is a high dynamic range (HDR) technology that uses dynamic metadata to optimize picture quality on a per-frame or per-scene basis, adjusting to the display’s capabilities. Profile 7 is a dual-layer Dolby Vision format primarily used for Ultra HD Blu-ray, consisting of:
- **Base Layer (BL):** Typically a 10-bit HDR10-compatible stream.
- **Enhancement Layer (EL):** Either a Full Enhancement Layer (FEL) or Minimum Enhancement Layer (MEL), which, when combined with the BL, produces a 12-bit video stream for enhanced color and brightness.[](https://en.m.wikipedia.org/wiki/Dolby_Vision)

**TV-led Dolby Vision** (also called player-led or low-latency Dolby Vision, LLDV) means the TV processes the Dolby Vision metadata and applies tone mapping, while the source device (e.g., a media player) passes the raw Dolby Vision data to the TV. This is distinct from **player-led Dolby Vision**, where the source device processes the metadata and sends a pre-processed signal to the TV.

### Can TVs Process FEL for Profile 7 in TV-led Mode?
The ability of a TV to process the Full Enhancement Layer (FEL) of Profile 7 in TV-led mode depends on both the TV’s hardware and firmware capabilities and the source device’s ability to deliver the FEL data correctly.

1. **TV Capabilities**:
   - Many modern Dolby Vision-capable TVs, such as those from Sony (e.g., A95K, X95L), LG (e.g., C2, OLED models), and others, support TV-led Dolby Vision for profiles like Profile 5 (single-layer, streaming) and Profile 8 (single-layer, often used for MKV files). These TVs can interpret Dolby Vision metadata and apply dynamic tone mapping based on their display capabilities.[](https://www.whathifi.com/advice/dolby-vision-hdr-everything-you-need-to-know)[](https://www.reddit.com/r/PleX/comments/njxx3m/is_dolby_vision_profile_7_actually_working/)
   - However, Profile 7 FEL requires processing both the Base Layer and the Full Enhancement Layer, which contains additional video data to achieve a true 12-bit output. This is more computationally intensive than processing the Minimum Enhancement Layer (MEL) or single-layer profiles, as FEL includes a full secondary video stream that enhances detail, particularly in complex scenes.[](https://en.m.wikipedia.org/wiki/Dolby_Vision)[](https://handwiki.org/wiki/Engineering:Dolby_Vision)
   - There is no definitive evidence from the provided information that consumer TVs explicitly advertise or support FEL processing for Profile 7 in TV-led mode. Most TVs are designed to handle the Base Layer and Reference Picture Unit (RPU) metadata, which is sufficient for MEL or single-layer Dolby Vision content. The FEL, however, requires specific hardware decoding capabilities that may not be universally implemented in consumer TVs.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-9)

2. **Source Device Role**:
   - For a TV to process Profile 7 FEL in TV-led mode, the source device (e.g., a media player like Ugoos AM6B Plus, Dune HD, or a UHD Blu-ray player) must deliver both the BL and EL streams, along with the RPU metadata, to the TV via HDMI without stripping or converting the FEL. Devices like the Nvidia Shield, for example, support Profile 7 but often ignore the FEL, using only the RPU metadata, resulting in an output similar to MEL or Profile 8.[](https://www.reddit.com/r/PleX/comments/12vv5s1/streaming_device_dovi_profile_7_support/)[](https://www.reddit.com/r/PleX/comments/njxx3m/is_dolby_vision_profile_7_actually_working/)
   - Some devices, such as the Ugoos AM6B Plus or Minix U22X-J, can process FEL when using specific software like Kodi or Plex with custom builds (e.g., CoreELEC or Monsoon’s Kodi build). However, even these devices may not always pass the FEL intact to the TV for TV-led processing, as they often decode the FEL themselves or convert it to a format like Profile 8.1.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-9)[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-6)

3. **Challenges with FEL Processing**:
   - **Hardware Limitations**: The FEL requires dual-stream decoding, which demands more processing power than MEL or single-layer Dolby Vision. Many TVs may not have the necessary hardware to decode and process the FEL stream, even if they support TV-led Dolby Vision for other profiles.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-8)
   - **Content Availability**: FEL content is rare, primarily found in specific UHD Blu-ray titles (e.g., *Terminator 2*, *Saving Private Ryan*), and even then, the visual difference between FEL and MEL may be subtle on current 10-bit displays, as most TVs cannot fully reproduce the 12-bit color depth of FEL.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-6)[](https://www.reddit.com/r/PleX/comments/12vv5s1/streaming_device_dovi_profile_7_support/)
   - **Firmware and Software**: Even if a TV theoretically supports FEL processing, it may require specific firmware updates or compatibility with the source device’s output. For example, Sony TVs like the X950G and A95K support Profile 7 and 8, but there’s no clear indication they process FEL natively in TV-led mode.[](https://www.reddit.com/r/PleX/comments/njxx3m/is_dolby_vision_profile_7_actually_working/)
   - **Flickering Issues**: Some titles, like *Saving Private Ryan*, exhibit flickering when the FEL is not processed, as the RPU metadata alone can cause inconsistent brightness mapping. Proper FEL processing stabilizes this, but it’s unclear if TVs can handle this correction in TV-led mode without a capable source device.[](https://www.reddit.com/r/PleX/comments/12vv5s1/streaming_device_dovi_profile_7_support/)

4. **Practical Observations**:
   - Devices like the Ugoos AM6B Plus and Minix U22X-J, when paired with specific Kodi builds or Plex, can output Profile 7 FEL correctly to TVs, but this often involves the device decoding the FEL and sending a processed signal, not necessarily relying on the TV to handle the FEL.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-9)[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-6)
   - TVs like the Sony A95K or LG C2 are noted for their Dolby Vision capabilities, but discussions suggest they may fall back to MEL or HDR10 if the FEL is not properly passed or processed. For example, a user with a Sony A80J noted that Profile 7 content triggered Dolby Vision mode, but it was unclear if the FEL was utilized.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-7)
   - The *What Hi-Fi?* article mentions that Dolby Vision support can be added via firmware updates on TVs with powerful processors, suggesting that some high-end TVs might theoretically support FEL with the right software, but this is not explicitly confirmed for TV-led FEL processing.[](https://www.whathifi.com/advice/dolby-vision-hdr-everything-you-need-to-know)

### Conclusion
While TVs that support TV-led Dolby Vision can process dynamic metadata for profiles like 5 and 8, there is no conclusive evidence that they can natively process the Full Enhancement Layer of Profile 7 in TV-led mode. The FEL requires specific hardware and software support to decode the dual-layer stream, which is typically handled by specialized media players (e.g., Ugoos AM6B Plus, Dune HD) rather than the TV itself. Most consumer TVs likely process only the Base Layer and RPU metadata, treating Profile 7 FEL content as MEL or falling back to HDR10 if the FEL is not supported.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-9)[](https://www.reddit.com/r/PleX/comments/12vv5s1/streaming_device_dovi_profile_7_support/)

For full Profile 7 FEL support, you would likely need a media player like the Ugoos AM6B Plus with a compatible Kodi build (e.g., CoreELEC or Monsoon’s build) or a device like the Dune HD Pro Vision 4K for ISO/BDMV playback, paired with a Dolby Vision-capable TV. Even then, the TV may rely on the player to process the FEL, with the TV handling the final tone mapping based on the processed signal.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-6)[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-8)

If you’re aiming for the best Profile 7 FEL experience, consider:
- **Source Device**: Use a media player like Ugoos AM6B Plus or Minix U22X-J with CoreELEC or Plex, which can handle FEL processing.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-9)
- **TV**: Choose a high-end Dolby Vision TV (e.g., Sony A95K, LG C2) to maximize tone mapping quality, though the TV may not process FEL natively.[](https://www.reddit.com/r/PleX/comments/njxx3m/is_dolby_vision_profile_7_actually_working/)
- **Content Format**: Ensure content is in a compatible format (e.g., MKV, ISO, or BDMV) to preserve the FEL.[](https://www.avsforum.com/threads/media-players-that-processing-dolby-vision-full-enhancement-layer.3183512/page-6)

If you need specific recommendations for your setup or want to verify FEL support for a particular TV model, please provide the TV model and source device details, and I can tailor the response further. For more information on Dolby Vision, you can refer to Dolby’s official site (https://www.dolby.com).[](https://www.dolby.com/technologies/dolby-vision/)
