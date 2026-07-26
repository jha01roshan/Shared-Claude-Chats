# Accessing CMD from Locked Win10 Screen

- Source: https://grok.com/share/bGVnYWN5_635c9b19-50e1-4dc6-b726-6ecdee41ca51
- Created: 2025-06-10
- Messages: 4

---

## Human

What .exe file is replaced to acess cmd while the win10 is locked screen

---

## Assistant

To access the Command Prompt (cmd.exe) from the Windows 10 lock screen, a common method involves replacing the **utilman.exe** file with **cmd.exe**. The **utilman.exe** file is associated with the Ease of Access button on the lock screen, and by replacing it, clicking the Ease of Access button launches the Command Prompt instead.

### Steps to Replace utilman.exe with cmd.exe:
1. **Boot from Windows Installation Media or Recovery Drive**:
   - You need a Windows 10 installation USB/DVD or a recovery drive to access a Command Prompt outside of the locked system.
   - Boot from the media, select your language, and choose **Repair your computer** at the setup screen.
   - Press **Shift + F10** to open a Command Prompt, or navigate to **Troubleshoot > Command Prompt**.

2. **Locate the Windows System Drive**:
   - In the Command Prompt, identify the drive letter where Windows is installed (usually `C:` or `D:`). Use commands like `dir C:` or `dir D:` to check for the `Windows` folder.
   - Navigate to the System32 folder by typing:
     ```
     cd /d D:\Windows\System32
     ```
     (Replace `D:` with the correct drive letter.)

3. **Back Up and Replace utilman.exe**:
   - Rename the original `utilman.exe` to create a backup:
     ```
     ren utilman.exe utilman_bak.exe
     ```
   - Copy `cmd.exe` to replace `utilman.exe`:
     ```
     copy cmd.exe utilman.exe
     ```

4. **Reboot the System**:
   - Exit the Command Prompt and reboot the computer normally:
     ```
     wpeutil reboot
     ```
   - Remove the installation media.

5. **Access Command Prompt from Lock Screen**:
   - At the Windows 10 lock screen, click the **Ease of Access** button (usually a clock-like icon in the bottom-right corner).
   - This will open `cmd.exe` instead of the Ease of Access menu, often with SYSTEM privileges.

### Important Notes:
- **Security Risks**: This method can bypass security and is considered a potential vulnerability. Microsoft has patched some versions of Windows to limit this exploit, so it may not work on fully updated systems or those with Secure Boot enabled.
- **Restoring Original Settings**: To revert, boot back into the recovery environment and restore the original `utilman.exe`:
  ```
  ren utilman.exe cmd.exe
  ren utilman_bak.exe utilman.exe
  ```
- **Legal and Ethical Considerations**: Only use this method on systems you own or have explicit permission to access. Unauthorized use may violate laws or policies.
- **BitLocker**: If BitLocker is enabled, you may need the recovery key to access the drive.
- **Alternative Methods**: Another older method involved replacing `sethc.exe` (Sticky Keys) with `cmd.exe`, triggered by pressing the Shift key five times, but this is less reliable in modern Windows versions due to security updates.

This method has been documented in various sources, including tech forums and tutorials, but its effectiveness may depend on the Windows 10 version and security settings.[](https://www.askvg.com/how-to-launch-command-prompt-or-other-programs-using-ease-of-access-button-at-login-screen-in-windows-vista-and-7/)[](https://mytekrescue.com/how-to-reset-the-password-on-almost-any-windows-computer/)[](https://www.isunshare.com/windows-10-password/enable-built-in-administrator-when-windows-10-locked-out.html)

---

## Human

Can you make a tutorial of it from start

---

## Assistant

Below is a step-by-step tutorial to replace the **utilman.exe** file with **cmd.exe** to access the Command Prompt from the Windows 10 lock screen. This method is often used to bypass a locked screen, but it requires physical access to the system and a Windows 10 installation or recovery media. Please note that this should only be performed on a system you own or have explicit permission to access, as unauthorized use may be illegal or unethical.

---

### **Tutorial: Accessing Command Prompt from Windows 10 Lock Screen by Replacing utilman.exe**

#### **What You’ll Need**
- A Windows 10 installation USB/DVD or a Windows 10 recovery drive.
- Physical access to the computer.
- Basic familiarity with Command Prompt commands.

#### **Step-by-Step Instructions**

1. **Prepare the Installation or Recovery Media**
   - If you don’t have a Windows 10 installation USB or recovery drive:
     - Download the Windows 10 ISO from Microsoft’s official website (https://www.microsoft.com/en-us/software-download/windows10).
     - Use a tool like the **Windows Media Creation Tool** to create a bootable USB or burn the ISO to a DVD.
     - Alternatively, create a recovery drive on another Windows 10 PC by searching for “Create a recovery drive” in the Start menu and following the prompts.
   - Ensure the USB/DVD is ready before proceeding.

2. **Boot from the Installation or Recovery Media**
   - Insert the Windows 10 installation USB/DVD or recovery drive into the locked computer.
   - Restart the computer and enter the **BIOS/UEFI settings** to set the USB/DVD as the primary boot device:
     - Press the appropriate key during startup (usually **F2**, **F12**, **Del**, or **Esc**, depending on your device).
     - In the BIOS/UEFI, navigate to the **Boot** menu and prioritize the USB/DVD drive.
     - Save changes and exit (usually **F10**).
   - The computer should boot from the media. If prompted, press any key to boot from the USB/DVD.

3. **Access the Command Prompt in the Recovery Environment**
   - Once the Windows Setup screen appears:
     - Select your language, time, and keyboard preferences, then click **Next**.
     - Instead of clicking **Install now**, select **Repair your computer** (bottom-left corner).
   - In the recovery menu, navigate to:
     - **Troubleshoot** > **Advanced options** > **Command Prompt**.
     - Alternatively, press **Shift + F10** at the setup screen to open a Command Prompt directly.

4. **Identify the Windows System Drive**
   - In the Command Prompt, the drive letters may differ from those in a running Windows system (e.g., the C: drive might appear as D:).
   - To find the correct drive, check for the Windows folder:
     ```
     dir C:
     ```
     or
     ```
     dir D:
     ```
   - Look for a folder named `Windows`. If it’s not on C: or D:, try other letters (E:, F:, etc.).
   - Once identified (e.g., D:), navigate to the System32 folder:
     ```
     cd /d D:\Windows\System32
     ```
     Replace `D:` with the correct drive letter.

5. **Back Up and Replace utilman.exe**
   - Create a backup of the original **utilman.exe** file to restore later if needed:
     ```
     ren utilman.exe utilman_bak.exe
     ```
   - Replace **utilman.exe** with **cmd.exe** by copying the Command Prompt executable:
     ```
     copy cmd.exe utilman.exe
     ```
   - Verify the replacement by checking the file:
     ```
     dir utilman.exe
     ```

6. **Reboot the Computer**
   - Close the Command Prompt:
     ```
     exit
     ```
   - In the recovery menu, select **Continue** to exit and reboot, or use the following command:
     ```
     wpeutil reboot
     ```
   - Remove the installation USB/DVD or recovery drive before the system restarts.

7. **Access Command Prompt from the Lock Screen**
   - Once the computer boots to the Windows 10 lock screen, locate the **Ease of Access** button (a clock-like icon in the bottom-right corner, next to the power button).
   - Click the **Ease of Access** button.
   - A Command Prompt window should open with **SYSTEM** privileges, bypassing the login screen.

8. **Using the Command Prompt (Optional Actions)**
   - From the Command Prompt, you can perform various tasks, such as:
     - **Reset a User Password**:
       ```
       net user <username> <newpassword>
       ```
       Replace `<username>` with the account name and `<newpassword>` with the desired password.
     - **Create a New User**:
       ```
       net user newuser newpassword /add
       net localgroup administrators newuser /add
       ```
     - **Enable the Built-in Administrator Account**:
       ```
       net user administrator /active:yes
       ```
   - After completing your tasks, close the Command Prompt by typing `exit`.

9. **Restore the Original utilman.exe (Optional)**
   - To revert the changes and restore the Ease of Access functionality:
     - Boot back into the recovery environment using the same installation/recovery media (repeat steps 2–3).
     - Navigate to the System32 folder again:
       ```
       cd /d D:\Windows\System32
       ```
     - Delete the modified **utilman.exe**:
       ```
       del utilman.exe
       ```
     - Restore the original file:
       ```
       ren utilman_bak.exe utilman.exe
       ```
     - Reboot the computer:
       ```
       wpeutil reboot
       ```

---

#### **Important Notes**
- **Security Patches**: This method may not work on fully updated Windows 10 systems or those with Secure Boot enabled, as Microsoft has patched this vulnerability in later builds.
- **BitLocker**: If the drive is encrypted with BitLocker, you’ll need the recovery key to access the system drive in the recovery environment.
- **Legal and Ethical Considerations**: Only use this method on systems you own or have explicit permission to modify. Unauthorized access to a computer is illegal in many jurisdictions.
- **Alternative Method**: Historically, replacing **sethc.exe** (Sticky Keys) with **cmd.exe** and pressing Shift five times was another way to access the Command Prompt, but this is less reliable in modern Windows versions.
- **Risks**: Incorrectly modifying system files can cause instability. Always back up important data before proceeding.

---

This tutorial is based on well-documented techniques found in tech forums, security blogs, and system administration guides. If you encounter issues (e.g., the method doesn’t work due to updates or security settings), let me know, and I can suggest alternative approaches or troubleshoot further.
