# NVMe Enclosure Power Management Guide

- Source: https://claude.ai/share/b0a3ac6d-b265-4c23-bc76-5c90b8d381d6
- Author: Suganthi
- Created: 2025-07-07
- Messages: 6

---

## Human

rewrite below for a FAQ response and use some symbols as needed.  also give the steps for mac. We use REALTEK 9210 chipset. 

how to disable power saver or sleeping mode on windows / MAC? 

Our enclosure relies on the NVMe SSD to manage it’s own power states and does not provide additional power management features. There are only a few USB 3 to NVMe bridge chipsets on the market and from what I have seen none of them offer additional power management features beyond the SSD’s built-in feature set, like our PiBOX India adapter.
Most likely the delay is caused by a Windows setting called USB selective suspend, if this is the case it will affect our NVMe SSD enclosure just like the enclosure you currently have. This setting will normally not interfere with the enclosure when connected directly to the computer, but may cause the behavior you describe if the enclosure is connected through an external ( or internal ) USB hub, or USB docking station.
Selective suspend can be disabled through Windows Power Management settings by performing the following:
1. Right click on the Start Menu and select “Power options” to open the “Power & Sleep” settings panel
2. Select “Additional power settings” on the right side of the panel
3. Under “Choose or customize a power plan” select “Change plan settings” for your currently selected power plan
4. Select “Change advanced power settings” - This will open a new “Power Options” window
5. Expand the panel for “USB settings” > “USB selective suspend settings”
6. Set these options to “Disabled” if not already disabled I also recommend connecting the enclosure directly to the computer rather than through a USB hub or docking station just to rule out a power management setting in the external device causing reduced performance.

---

## Assistant

# ❓ FAQ: How to Disable Power Saving/Sleep Mode on Windows & Mac

## 🔍 **Issue Description**
Our enclosure uses the **REALTEK 9210 chipset** and relies on the NVMe SSD to manage its own power states. Like most USB 3.0 to NVMe bridge chipsets, it doesn't provide additional power management features beyond the SSD's built-in capabilities.

The most common cause of delays/disconnections is **USB selective suspend** - a power-saving feature that can interfere with external storage devices, especially when connected through USB hubs or docking stations.

---

## 💻 **Windows Solution**

**Disable USB Selective Suspend:**

1. 🖱️ Right-click the **Start Menu** → Select **"Power Options"**
2. 📋 Click **"Additional power settings"** (right side panel)
3. ⚙️ Under "Choose or customize a power plan" → Click **"Change plan settings"**
4. 🔧 Select **"Change advanced power settings"** (opens new Power Options window)
5. 📂 Expand **"USB settings"** → **"USB selective suspend settings"**
6. ❌ Set both options to **"Disabled"**
7. ✅ Click **"Apply"** and **"OK"**

---

## 🍎 **Mac Solution**

**Disable USB Power Management:**

1. 🍎 Click **Apple Menu** → **"System Preferences"** (or **"System Settings"** on newer macOS)
2. 🔋 Select **"Energy Saver"** (or **"Battery"** on newer versions)
3. ⚙️ Click **"Power Adapter"** tab
4. ❌ **Uncheck** "Put hard disks to sleep when possible"
5. 🖥️ Set **"Turn display off after"** to **"Never"** (while testing)

**Alternative Terminal Method:**
```bash
sudo pmset -a disksleep 0
```

---

## 💡 **Additional Recommendations**

- 🔌 Connect the enclosure **directly to your computer** (avoid USB hubs/docking stations)
- 🔄 Try different USB ports if issues persist
- 📱 Ensure you're using a high-quality USB cable rated for data transfer

---

## ⚠️ **Note**
These settings affect system-wide power management. The enclosure should work normally when connected directly to your computer's USB ports.

---

## Human

can you also give some settings breakdown for windows 10/11 ? i want to see if i can add some screenshots

---

## Assistant

# 🖥️ **Detailed Windows 10/11 Settings Breakdown**

## 🎯 **Method 1: Power Options (Recommended)**

### **Step 1: Access Power Options**
**Windows 10:**
- 🖱️ Right-click **Start Menu** → **"Power Options"**
- *Screenshot location: Start menu context menu*

**Windows 11:**
- 🖱️ Right-click **Start Menu** → **"Power Options"** 
- *Alternative: Settings app → System → Power & battery*

### **Step 2: Power & Sleep Settings Panel**
**What you'll see:**
- 💤 Sleep settings dropdown menus
- 🖥️ Screen timeout options
- ➡️ **"Additional power settings"** link (right side)
- *Screenshot location: Main Power & Sleep panel*

### **Step 3: Classic Power Options**
**What you'll see:**
- ⚡ Power plan selection (Balanced, High Performance, Power Saver)
- 🔧 **"Change plan settings"** links next to each plan
- *Screenshot location: Choose or customize power plan window*

### **Step 4: Edit Plan Settings** 
**What you'll see:**
- ⏰ "Turn off the display" dropdown
- 💤 "Put the computer to sleep" dropdown  
- 🔧 **"Change advanced power settings"** link
- *Screenshot location: Edit Plan Settings window*

### **Step 5: Advanced Power Options**
**What you'll see:**
- 📂 Expandable tree menu with categories
- 🔍 Look for **"USB settings"** folder
- *Screenshot location: Power Options dialog box*

### **Step 6: USB Settings Configuration**
**What you'll see:**
- 📂 **"USB settings"** expanded
- 📂 **"USB selective suspend setting"** sub-option
- ⚡ **"On battery"** and **"Plugged in"** dropdown menus
- 🎯 **Change both to "Disabled"**
- *Screenshot location: USB selective suspend settings expanded*

---

## 🎯 **Method 2: Device Manager**

### **Step 1: Open Device Manager**
- 🖱️ Right-click **Start Menu** → **"Device Manager"**
- *Screenshot location: Start menu context menu*

### **Step 2: USB Controllers Section**
**What you'll see:**
- 📂 **"Universal Serial Bus controllers"** section
- 🔍 Look for **"USB Root Hub"** entries
- *Screenshot location: Device Manager with USB section expanded*

### **Step 3: USB Hub Properties**
- 🖱️ Right-click any **"USB Root Hub"** → **"Properties"**
- 📋 Click **"Power Management"** tab
- ❌ **Uncheck** "Allow the computer to turn off this device to save power"
- 🔄 **Repeat for ALL USB Root Hub entries**
- *Screenshot location: USB Root Hub Properties → Power Management tab*

---

## 🎯 **Method 3: Registry Edit (Advanced Users)**

### **Registry Path:**
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USB
```

### **Key to Modify:**
- **Value:** `DisableSelectiveSuspend`
- **Type:** DWORD (32-bit)
- **Data:** `1` (to disable)

⚠️ **Warning:** Only for advanced users. Backup registry before making changes.

---

## 🎯 **Method 4: Command Prompt/PowerShell**

### **Disable USB Selective Suspend:**
```cmd
powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /SETACTIVE SCHEME_CURRENT
```

### **Check Current Setting:**
```cmd
powercfg /QUERY SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226
```

---

## 📱 **Screenshot Checklist for Documentation**

### **Essential Screenshots:**
1. ✅ **Start Menu context menu** (showing Power Options)
2. ✅ **Power & Sleep main panel** (with Additional power settings link)
3. ✅ **Power Plans selection** (Choose or customize power plan)
4. ✅ **Edit Plan Settings** (with Change advanced power settings link)
5. ✅ **Power Options dialog** (showing USB settings folder)
6. ✅ **USB selective suspend settings** (showing Enabled→Disabled change)
7. ✅ **Device Manager USB section** (expanded Universal Serial Bus controllers)
8. ✅ **USB Root Hub Properties** (Power Management tab with checkbox)

### **Optional Screenshots:**
- 🔧 Registry Editor (for advanced section)
- 💻 Command Prompt/PowerShell (showing commands)
- ✅ Confirmation dialogs and Apply buttons

---

## 🎨 **Visual Tips for Screenshots**

- 🖼️ **Crop tightly** around relevant UI elements
- 🔴 **Use red arrows/circles** to highlight important buttons
- 📝 **Add numbered callouts** for step sequence
- 🌟 **Highlight the "before/after"** states (Enabled vs Disabled)

This breakdown should give you plenty of material for comprehensive documentation with clear screenshot opportunities! 📸

---

## Human

can i run a powershell command for this also ?

---

## Assistant

# 💻 **PowerShell Commands for USB Selective Suspend**

## ⚡ **Quick Solution (Administrator Required)**

### **Disable USB Selective Suspend:**
```powershell
# Run PowerShell as Administrator first!
powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /SETACTIVE SCHEME_CURRENT
```

### **Enable USB Selective Suspend (if you want to revert):**
```powershell
powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1
powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1
powercfg /SETACTIVE SCHEME_CURRENT
```

---

## 🔍 **Check Current Settings**

### **Query USB Selective Suspend Status:**
```powershell
powercfg /QUERY SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226
```

### **Human-Readable Status Check:**
```powershell
$usbSetting = powercfg /QUERY SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226
if ($usbSetting -match "Current AC Power Setting Index: 0x00000000") {
    Write-Host "✅ USB Selective Suspend is DISABLED (AC Power)" -ForegroundColor Green
} else {
    Write-Host "❌ USB Selective Suspend is ENABLED (AC Power)" -ForegroundColor Red
}
```

---

## 🎯 **Alternative PowerShell Methods**

### **Method 1: Registry Approach**
```powershell
# Disable via Registry (requires restart)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\USB" -Name "DisableSelectiveSuspend" -Value 1 -Type DWord
Write-Host "✅ Registry setting applied. Restart required." -ForegroundColor Yellow
```

### **Method 2: WMI Power Management**
```powershell
# Get all USB Root Hubs and disable power management
$usbHubs = Get-WmiObject -Class Win32_USBHub
foreach ($hub in $usbHubs) {
    $hub.SetPowerState(1)  # 1 = Full power, no suspend
}
Write-Host "✅ USB Hub power management disabled" -ForegroundColor Green
```

### **Method 3: Device Manager via PowerShell**
```powershell
# Disable power management for all USB Root Hubs
$usbDevices = Get-WmiObject -Class Win32_PnPEntity | Where-Object { $_.Name -like "*USB Root Hub*" }
foreach ($device in $usbDevices) {
    $device.SetPowerState(1)
}
```

---

## 🛠️ **Complete PowerShell Script**

```powershell
# USB Selective Suspend Manager Script
# Run as Administrator

function Disable-USBSelectiveSuspend {
    Write-Host "🔧 Disabling USB Selective Suspend..." -ForegroundColor Cyan
    
    # Method 1: PowerCfg (AC Power)
    powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
    
    # Method 2: PowerCfg (Battery Power)
    powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
    
    # Apply changes
    powercfg /SETACTIVE SCHEME_CURRENT
    
    Write-Host "✅ USB Selective Suspend disabled successfully!" -ForegroundColor Green
}

function Enable-USBSelectiveSuspend {
    Write-Host "🔧 Enabling USB Selective Suspend..." -ForegroundColor Cyan
    
    powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1
    powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1
    powercfg /SETACTIVE SCHEME_CURRENT
    
    Write-Host "✅ USB Selective Suspend enabled successfully!" -ForegroundColor Green
}

function Get-USBSelectiveSuspendStatus {
    Write-Host "🔍 Checking USB Selective Suspend status..." -ForegroundColor Cyan
    
    $result = powercfg /QUERY SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226
    
    if ($result -match "Current AC Power Setting Index: 0x00000000") {
        Write-Host "✅ AC Power: DISABLED" -ForegroundColor Green
    } else {
        Write-Host "❌ AC Power: ENABLED" -ForegroundColor Red
    }
    
    if ($result -match "Current DC Power Setting Index: 0x00000000") {
        Write-Host "✅ Battery Power: DISABLED" -ForegroundColor Green
    } else {
        Write-Host "❌ Battery Power: ENABLED" -ForegroundColor Red
    }
}

# Main execution
Write-Host "🔋 USB Selective Suspend Manager" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Yellow

# Check if running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ This script requires Administrator privileges!" -ForegroundColor Red
    exit 1
}

# Show current status
Get-USBSelectiveSuspendStatus

# Disable USB Selective Suspend
Disable-USBSelectiveSuspend

# Verify changes
Write-Host "`n🔍 Verifying changes..." -ForegroundColor Cyan
Get-USBSelectiveSuspendStatus
```

---

## 🚀 **One-Liner Commands**

### **Quick Disable:**
```powershell
powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0; powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0; powercfg /SETACTIVE SCHEME_CURRENT; Write-Host "✅ USB Selective Suspend Disabled" -ForegroundColor Green
```

### **Quick Status Check:**
```powershell
powercfg /QUERY SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 | Select-String "Current.*Setting Index"
```

---

## 📋 **How to Use**

1. **🔓 Open PowerShell as Administrator:**
   - Press `Win + X` → Select **"Windows PowerShell (Admin)"** or **"Terminal (Admin)"**

2. **📄 Copy and paste any of the commands above**

3. **⚡ Press Enter to execute**

4. **✅ Restart is usually NOT required** (changes take effect immediately)

---

## 🎯 **GUID Explanation**

The long GUIDs in the commands represent:
- `2a737441-1930-4402-8d77-b2bebba308a3` = **USB settings category**
- `48e6b7a6-50f5-4782-a5d4-53bb8f07e226` = **USB selective suspend setting**

These are Windows system identifiers that don't change between systems! 🔧
