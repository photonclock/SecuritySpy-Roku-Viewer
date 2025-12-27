# Security Spy Viewer for Roku

## Installation Instructions (Sideloading)

This app is not available in the public Roku Channel Store. You must install it using Roku's Developer Mode.

### Prerequisites
* A Roku device connected to the same network as your computer.
* The `Security_Spy_Viewer.zip` file from the [Releases page](https://github.com/photonclock/SecuritySpy-Roku-Viewer/releases/latest).

### Step 1: Enable Developer Mode
1.  Turn on your Roku device and TV.
2.  On your Roku remote, enter the following sequence rapidly:
    * **Home** (x3)
    * **Up** (x2)
    * **Right**
    * **Left**
    * **Right**
    * **Left**
    * **Right**
3.  Select **Enable installer and restart** on the screen that appears.
4.  Review the license agreement and set a **password** for the `rokudev` user.
5.  The Roku will reboot.

### Step 2: Access the Installer
1.  Once the Roku restarts, go to **Settings > Network > About** to find the device's **IP Address**.
2.  Open a web browser on your computer and navigate to `http://<ROKU_IP_ADDRESS>` (e.g., `http://192.168.1.50`).
3.  Log in with the username `rokudev` and the password you created in Step 1.

### Step 3: Upload the Application
1.  Click the **Upload** button in the web interface.
2.  Select the `Security_Spy_Viewer.zip` file.
3.  Once the file is uploaded, click **Install**.
4.  The application will immediately launch on your TV.

**Note:** If you exit the app, it remains installed on your home screen, usually at the bottom of the list of apps and channels (easiest way to navigate to it from home is to go right to channels, then up a few clicks to reach the bottom of the app list. Sideloaded apps may be removed if you enable Developer Mode on a different Roku device linked to the same account, or if the "dev" key expires (which is rare for local testing).