# Installing Applets on Fedora COSMIC Atomic

- Source: https://grok.com/share/bGVnYWN5_5a2922a3-f838-4c2d-9115-f219293e5475
- Created: 2025-05-14
- Messages: 2

---

## Human

Installing self compiled applets on cosmic Atomic Fedora, fails due to read only file system

---

## Assistant

Fedora COSMIC Atomic uses an immutable, read-only file system for core components, managed by `rpm-ostree`, which prevents direct modifications like installing self-compiled applets to system directories (e.g., `/usr`). To work around this, you can use containerized or user-level approaches to install and run custom applets without modifying the read-only system. Below are steps and solutions to address this issue:

### Understanding the Issue
- **Read-Only File System**: Fedora COSMIC Atomic employs `rpm-ostree`, which makes `/usr` and other system directories read-only to ensure atomic updates and system stability. Self-compiled applets typically try to install to these directories, causing errors.
- **COSMIC Applets**: COSMIC applets are modular components (e.g., dock or panel widgets) written in Rust, designed to integrate with the COSMIC Desktop Environment (DE). Installing them requires compatibility with COSMIC’s API and a way to bypass the read-only constraint.
- **Atomic Nature**: Changes to the system are layered or containerized, and direct writes to the file system are restricted unless done through specific mechanisms.

### Solutions to Install Self-Compiled Applets

#### 1. **Install Applets in User Space**
   Instead of installing applets to system directories, compile and place them in a user-writable directory (e.g., `~/.local`) and configure COSMIC to load them from there.

   **Steps**:
   - **Compile the Applet**:
     - Clone the applet’s source code (e.g., from a GitHub repository or your own project).
     - Ensure you have the necessary dependencies (e.g., Rust, `cargo`, and COSMIC libraries like `libcosmic`). Install these in a user-controlled environment if needed (see toolbox/distrobox below).
     - Compile the applet using `cargo build --release` to generate the binary.
   - **Place in User Directory**:
     - Move the compiled binary to a user-writable location, such as `~/.local/lib/cosmic-applets/` or `~/.cosmic-applets/`.
     - Example:
       ```bash
       mkdir -p ~/.local/lib/cosmic-applets
       cp target/release/your-applet ~/.local/lib/cosmic-applets/
       ```
   - **Configure COSMIC to Load the Applet**:
     - COSMIC applets are loaded dynamically. Check COSMIC’s documentation or configuration files (e.g., `~/.config/cosmic/`) to specify custom applet paths.
     - You may need to modify the panel or dock configuration to include your applet. For example, edit the relevant COSMIC settings file or use the COSMIC Settings app if it supports adding custom applets.
     - Restart the COSMIC session:
       ```bash
       systemctl --user restart cosmic-session
       ```
   - **Verify**:
     - Check if the applet appears in the COSMIC panel or dock. If it doesn’t, ensure the applet is compatible with the COSMIC API and that the path is correctly specified.

   **Notes**:
   - COSMIC’s applet system is still in alpha, so documentation on custom applet loading may be sparse. Check the [COSMIC GitHub repository](https://github.com/pop-os/cosmic-epoch) for the latest guidance.[](https://github.com/pop-os/cosmic-epoch)
   - User-space installation avoids read-only restrictions but requires COSMIC to support loading applets from non-system paths.

#### 2. **Use a Container with Toolbox or Distrobox**
   Fedora Atomic encourages containerized workflows for development and custom software. Use `toolbox` or `distrobox` to create a mutable environment where you can compile and test applets.

   **Steps**:
   - **Install Toolbox or Distrobox**:
     - Toolbox is pre-installed on Fedora Atomic. If not, install it:
       ```bash
       sudo rpm-ostree install toolbox
       sudo systemctl reboot
       ```
     - Alternatively, install Distrobox for more flexibility:
       ```bash
       sudo rpm-ostree install distrobox
       sudo systemctl reboot
       ```
   - **Create a Container**:
     - Start a toolbox container:
       ```bash
       toolbox enter
       ```
     - Or create a Distrobox container with Fedora:
       ```bash
       distrobox create -i fedora:41 -n cosmic-dev
       distrobox enter cosmic-dev
       ```
   - **Install Development Tools**:
     - Inside the container, install Rust, `cargo`, and COSMIC dependencies:
       ```bash
       sudo dnf install rust cargo libcosmic-devel just libwayland-devel libxkbcommon-devel
       ```
     - Note: Dependency names may vary. Check the [COSMIC repository](https://github.com/pop-os/cosmic-epoch) for exact requirements.[](https://github.com/pop-os/cosmic-epoch)
   - **Compile the Applet**:
     - Clone and build your applet inside the container:
       ```bash
       git clone <your-applet-repo>
       cd <your-applet-repo>
       cargo build --release
       ```
   - **Test the Applet**:
     - Copy the compiled binary to the host’s user directory (e.g., `~/.local/lib/cosmic-applets/`) from the container:
       ```bash
       cp target/release/your-applet ~/.local/lib/cosmic-applets/
       ```
     - Exit the container and restart the COSMIC session as above.
   - **Optional: Export the Applet**:
     - If the applet works, you can package it as a Flatpak or system extension (see below) for easier distribution.

   **Notes**:
   - Containers provide a mutable environment, bypassing the read-only file system.
   - Use `toolbox` for simplicity or `distrobox` for advanced features like GUI integration.[](https://www.reddit.com/r/Fedora/comments/1d37kgv/hopping_onto_atomic/)
   - Ensure the container has access to the COSMIC runtime libraries on the host.

#### 3. **Layer the Applet as an RPM Package**
   If the applet needs to be installed system-wide, package it as an RPM and layer it using `rpm-ostree`. This requires a reboot but integrates the applet into the system.

   **Steps**:
   - **Create an RPM Package**:
     - Inside a toolbox/distrobox container, install RPM build tools:
       ```bash
       sudo dnf install rpmdevtools
       rpmdev-setuptree
       ```
     - Write a `.spec` file for your applet. Example:
       ```spec
       Name: cosmic-applet-yourapplet
       Version: 1.0
       Release: 1%{?dist}
       Summary: Custom COSMIC applet
       License: GPL-3.0
       Source0: %{name}-%{version}.tar.gz
       BuildRequires: rust cargo
       Requires: cosmic-desktop

       %description
       A custom applet for the COSMIC Desktop Environment.

       %prep
       %setup -q

       %build
       cargo build --release

       %install
       install -D -m 755 target/release/your-applet %{buildroot}%{_libdir}/cosmic-applets/your-applet

       %files
       %{_libdir}/cosmic-applets/your-applet

       %changelog
       * Wed May 14 2025 Your Name <you@example.com> - 1.0-1
       - Initial release
       ```
     - Build the RPM:
       ```bash
       rpmbuild -ba ~/rpmbuild/SPECS/cosmic-applet-yourapplet.spec
       ```
   - **Layer the RPM**:
     - Copy the RPM to the host and install it:
       ```bash
       rpm-ostree install ~/rpmbuild/RPMS/x86_64/cosmic-applet-yourapplet-1.0-1.fc41.x86_64.rpm
       ```
     - Reboot to apply:
       ```bash
       sudo systemctl reboot
       ```
   - **Verify**:
     - Check if the applet is loaded by COSMIC (e.g., in the panel or dock).
     - Use `rpm-ostree status` to confirm the package is layered.[](https://www.reddit.com/r/Fedora/comments/1d37kgv/hopping_onto_atomic/)

   **Notes**:
   - RPM layering is persistent but requires a reboot for each change.
   - This approach is suitable for stable applets but less flexible for development.

#### 4. **Use System Extensions (sysext)**
   Systemd system extensions (`sysext`) allow you to add files to the system without modifying the read-only file system. This is experimental but supported on Fedora Atomic.

   **Steps**:
   - **Compile the Applet**:
     - Use a toolbox/distrobox container to compile the applet as described above.
   - **Create a System Extension**:
     - Create a directory structure for the extension:
       ```bash
       mkdir -p cosmic-sysext/usr/lib/cosmic-applets
       cp target/release/your-applet cosmic-sysext/usr/lib/cosmic-applets/
       ```
     - Package the extension:
       ```bash
       tar -czf cosmic-sysext.tar.gz -C cosmic-sysext .
       ```
   - **Install the Extension**:
     - Move the extension to `/var/lib/extensions/`:
       ```bash
       sudo mv cosmic-sysext.tar.gz /var/lib/extensions/cosmic-sysext
       ```
     - Enable and refresh the extension:
       ```bash
       sudo systemctl enable --now systemd-sysext
       sudo systemd-sysext refresh
       ```
   - **Handle SELinux**:
     - If SELinux is enabled (default on Fedora), apply correct labels:
       ```bash
       sudo restorecon -R /var/lib/extensions
       ```
     - Alternatively, temporarily disable SELinux for testing (not recommended for production):
       ```bash
       sudo setenforce 0
       ```
   - **Restart COSMIC**:
     - Restart the session to load the applet:
       ```bash
       systemctl --user restart cosmic-session
       ```
   - **Verify**:
     - Check if the applet is loaded by COSMIC.

   **Notes**:
   - System extensions are a new feature and may have compatibility issues.[](https://github.com/pop-os/cosmic-epoch)[](https://fedoramagazine.org/whats-new-for-fedora-atomic-desktops-in-fedora-42/)
   - Ensure the applet’s dependencies are available on the host or bundled in the extension.

#### 5. **Package as a Flatpak**
   For a more portable and containerized approach, package the applet as a Flatpak, which is well-supported on Fedora Atomic.

   **Steps**:
   - **Set Up Flatpak Development**:
     - Inside a toolbox/distrobox container, install Flatpak tools:
       ```bash
       sudo dnf install flatpak-builder
       ```
   - **Create a Flatpak Manifest**:
     - Write a `org.cosmic.YourApplet.json` manifest. Example:
       ```json
       {
         "app-id": "org.cosmic.YourApplet",
         "runtime": "org.freedesktop.Platform//24.08",
         "sdk": "org.freedesktop.Sdk//24.08",
         "command": "your-applet",
         "finish-args": [
           "--share=ipc",
           "--socket=wayland",
           "--socket=fallback-x11"
         ],
         "modules": [
           {
             "name": "your-applet",
             "buildsystem": "simple",
             "build-commands": [
               "cargo build --release",
               "install -Dm755 target/release/your-applet /app/bin/your-applet"
             ],
             "sources": [
               {
                 "type": "git",
                 "url": "<your-applet-repo>",
                 "branch": "main"
               }
             ]
           }
         ]
       }
       ```
   - **Build and Install**:
     - Build the Flatpak:
       ```bash
       flatpak-builder --install build-dir org.cosmic.YourApplet.json
       ```
     - Install it on the host:
       ```bash
       flatpak install org.cosmic.YourApplet
       ```
   - **Configure COSMIC**:
     - Ensure COSMIC can load Flatpak-packaged applets (may require custom configuration or a wrapper script).
     - Restart the COSMIC session.

   **Notes**:
   - Flatpak is ideal for distribution but requires COSMIC to support Flatpak applets, which may not yet be implemented in the alpha stage.
   - Check the [COSMIC GitHub](https://github.com/pop-os/cosmic-epoch) for Flatpak integration status.[](https://github.com/pop-os/cosmic-epoch)

#### 6. **Modify a Custom Atomic Image**
   For advanced users, create a custom Fedora COSMIC Atomic image with your applet pre-installed using `bootc` or Universal Blue’s build system.

   **Steps**:
   - **Set Up Bootc**:
     - Install `bootc` in a container:
       ```bash
       sudo dnf install bootc
       ```
   - **Create a Containerfile**:
     - Example `Containerfile`:
       ```dockerfile
       FROM quay.io/fedora/fedora-bootc:41
       RUN dnf install -y cosmic-desktop
       COPY your-applet /usr/lib/cosmic-applets/your-applet
       RUN dnf clean all
       ```
     - Place the compiled applet binary in the build context.
   - **Build and Deploy**:
     - Build the image:
       ```bash
       podman build -t my-cosmic-atomic .
       ```
     - Rebase the system to the new image:
       ```bash
       sudo rpm-ostree rebase ostree-unverified-registry:localhost/my-cosmic-atomic
       sudo systemctl reboot
       ```
   - **Verify**:
     - Check if the applet is loaded by COSMIC.

   **Notes**:
   - This approach requires significant setup but is ideal for creating a reproducible system with your applet.[](https://fedoramagazine.org/building-your-own-atomic-bootc-desktop/)
   - Use Universal Blue’s `blue-build` for a simpler build process if preferred.[](https://www.reddit.com/r/Fedora/comments/1d37kgv/hopping_onto_atomic/)

### Troubleshooting Tips
- **Applet Not Loading**:
  - Verify the applet’s compatibility with the COSMIC API (check the [COSMIC repository](https://github.com/pop-os/cosmic-epoch) for API details).
  - Check logs for errors:
    ```bash
    journalctl --user -u cosmic-session
    ```
- **Dependency Issues**:
  - Ensure all required libraries (e.g., `libcosmic`, `libwayland`) are installed in the container or host.
  - Use `ldd` to check the applet’s dependencies:
    ```bash
    ldd ~/.local/lib/cosmic-applets/your-applet
    ```
- **SELinux Errors**:
  - If SELinux blocks the applet, adjust contexts or temporarily set SELinux to permissive mode for testing:
    ```bash
    sudo setenforce 0
    ```
  - Restore SELinux afterward:
    ```bash
    sudo setenforce 1
    ```
- **COSMIC Alpha Bugs**:
  - COSMIC is in alpha, so applets may fail due to bugs in the DE. Report issues to the [COSMIC GitHub](https://github.com/pop-os/cosmic-epoch/issues).[](https://github.com/ublue-os/cosmic)
- **Read-Only Errors Persist**:
  - Double-check that you’re installing to a user-writable directory or using a containerized approach.
  - Avoid `sudo` for user-space installations to prevent attempts to write to `/usr`.

### Recommendations
- **Preferred Approach**: Start with **user-space installation** (Option 1) or **toolbox/distrobox** (Option 2) for simplicity and flexibility during development.
- **For Production**: Use **RPM layering** (Option 3) or **Flatpak** (Option 5) for stable, system-wide deployment.
- **For Advanced Users**: Build a **custom image** (Option 6) if you need a fully customized system.
- **Backup**: Before making system changes (e.g., rebasing or layering), back up critical data, as Fedora Atomic’s rollback feature may not cover all scenarios.
- **Community Support**: Join the Fedora COSMIC SIG or Matrix server for help with applet development and Atomic-specific issues.[](https://news.itsfoss.com/fedora-cosmic-spin/)

### Additional Resources
- [COSMIC GitHub](https://github.com/pop-os/cosmic-epoch) for applet development and API details.[](https://github.com/pop-os/cosmic-epoch)
- [Fedora COSMIC Atomic Documentation](https://fedoraproject.org/atomic-desktops/cosmic/) for system specifics.[](https://fedoraproject.org/atomic-desktops/)
- [Fedora Atomic Desktops Guide](https://fedoramagazine.org/introducing-fedora-atomic-desktops/) for `rpm-ostree` and container workflows.[](https://fedoramagazine.org/introducing-fedora-atomic-desktops/)
- [Universal Blue Project](https://universal-blue.org/) for custom image builds.[](https://github.com/ublue-os/cosmic)

If you encounter specific errors (e.g., compilation failures or COSMIC configuration issues), share them, and I can provide more targeted assistance. Let me know if you need help with any step!
