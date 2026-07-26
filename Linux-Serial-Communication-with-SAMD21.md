# Linux Serial Communication with SAMD21

- Source: https://claude.ai/share/759d64f0-1edb-4da0-959f-b2f2bc6a4bda
- Author: Rusty
- Created: 2025-06-10
- Messages: 2

---

## Human

Hello everyone. I was hoping the community could help me out. I’m not sure what I’m doing wrong. I’m having trouble trying to send a command from a Linux Debian 12 computer to a Sparkfun SAMD21 Mini Breakout via serial monitor.
I connected a USB to USB-C adaptor cable from the USB port on my Linux device to the USB-C connector on the Mini breakout. Here is my current sketch.

image578×790 48.1 KB

When I try this using the Serial Monitor on Arduino IDE on my Windows laptop it works fine. I see the “Please Press 1 to Generate PIN” message. When I press “1” and then “Enter” I get the “Success” message sent back to me.
I’m trying to reproduce this, using a linux Debian 12 device to send the command. I’m trying send the command “1” from the Linux computer through the USB-C connector on the Sparkfun SAMD21 Mini breakout. I have tried using the programs screen, picocom, and minicom, without any success.
When I log into my linux device via ssh I can see that the Sparkfun Mini Breakout is “ttyACM0.” When I try to use the program "screen for example, I use the command “screen /dev/ttyACM0 115200.” I had set my baud rate to 115200 in my sketch.
However it doesn’t seem to do anything. I just see a blinking cursor. I don’t even get the “Please press 1 to Generate PIN” message from the Mini breakout. When I press the buttons on my keyboard I don’t see them on screen.
What’s odd is that I tried something similar with an Arduino UNO and I was able to send this command using screen from my linux device. I got the response message from the Arduino UNO as well.
Here’s the link to Sparkfun’s website explaining the serial USB port works on the SAMD21 Mini breakout. Are there any drivers that I need to install on Linux to fix this problem? Thanks.
learn.sparkfun.com

---

## Assistant

Based on your description, this sounds like a common issue with SAMD21-based boards and Linux serial communication. Here are several things to check and try:

## 1. Check USB Enumeration and Device Recognition

First, verify that Linux is properly recognizing the device:

```bash
# Check if the device is detected
lsusb | grep -i samd

# Check dmesg output when you plug/unplug the device
dmesg | tail -20

# Verify the device appears and permissions
ls -l /dev/ttyACM*
```

## 2. User Permissions

Make sure your user is in the `dialout` group:

```bash
# Check current groups
groups

# Add yourself to dialout group if needed
sudo usermod -a -G dialout $USER

# Log out and back in, or use:
newgrp dialout
```

## 3. SAMD21-Specific Issues

The SAMD21 has some quirks that differ from traditional Arduino boards:

### Reset Behavior
The SAMD21 may reset when you open the serial connection. Try this sequence:

```bash
# Open screen but don't expect immediate output
screen /dev/ttyACM0 115200

# Press the reset button on the board AFTER opening screen
# Or try double-tapping reset to enter bootloader mode, then single reset
```

### CDC (USB Serial) Driver
The SAMD21 uses USB CDC (Communications Device Class). Check if the `cdc_acm` driver is loaded:

```bash
lsmod | grep cdc_acm
```

If it's not loaded:
```bash
sudo modprobe cdc_acm
```

## 4. Alternative Serial Tools with Better Control

Try `stty` to configure the port before using screen:

```bash
# Configure the port
stty -F /dev/ttyACM0 115200 cs8 -cstopb -parenb raw

# Then use screen
screen /dev/ttyACM0 115200
```

Or try `picocom` with specific flags:
```bash
picocom -b 115200 --omap crcrlf --echo /dev/ttyACM0
```

## 5. Check for Device Disconnection

SAMD21 boards sometimes disconnect/reconnect during operation. Monitor this:

```bash
# In one terminal, watch for device changes
watch -n 1 'ls -l /dev/ttyACM*'

# In another terminal, try your serial connection
```

## 6. Bootloader vs Application Mode

The SAMD21 might be in bootloader mode. Check if you see a different device name or if double-tapping reset changes the device enumeration.

## 7. Arduino IDE Serial Monitor Working but Terminal Not

Since Arduino IDE works on Windows, the issue might be:
- **Flow control**: Try adding `-crtscts` to disable hardware flow control
- **Line endings**: The Arduino IDE might be sending different line endings

Try:
```bash
echo "1" > /dev/ttyACM0
```

## 8. Debugging Steps

1. **Verify sketch is running**: Add more frequent `Serial.print()` statements in your `loop()`
2. **Check baud rate**: Try common rates like 9600, 57600
3. **Test with `cat`**: `cat /dev/ttyACM0` to see if any data comes through

## 9. No Additional Drivers Needed

Linux should handle SAMD21 USB CDC without additional drivers, but the `cdc_acm` kernel module must be loaded.

Try these steps in order, and let me know what you discover. The most common issues are permissions, the reset behavior, or the device being in bootloader mode rather than running your sketch.
