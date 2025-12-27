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

### **Instructions:** 

Enter the Configure page

Enter **IP** and **PORT** of your Security Spy server

HTTPS mode: 
true = https (you will need a valid and properly configured SSL certificate installed on your server)
false = http

Auth String: 
Enter the base64 encoded version of your username:password, as described in the [Security Spy Web Server Spec](https://bensoftware.com/securityspy/web-server-spec.html)

I recommend setting up an alternate user/password in Security Spy > Web > Accounts, with the permission type for the user limited to "View", ie:
`user: rokutv`
`Password: your_password`

To convert your "username:password" to a base64 string, you can do this in Terminal:
`echo -n "rokutv:your_password" | base64`

If your Roku offers the feature to scan the screen with a QR code so you can use your phone to enter the auth string text, do it. Get the auth string on your phone, copy it to the clipboard, connect to the Roku via the QR code, then paste the string. It's a lot easier than typing it in with the remote. Don't forget to include the "==" that typically occurs at the end of a base64 encoded string.

# Refresh Rate: #
Click OK to toggle the value. 
I've only tested this with 8 cameras. 
I recommend setting this to no higher than 4x the number of cameras you have, but your mileage may vary. If you have 16/32/64 cameras, I have no idea how it will perform. Please let me know! Recommendation: Start with refresh rate=1, and go up from there.

# Maintain Aspect: #
Click OK to toggle the value. true = camera source aspect should be maintained, false = cameras will stretch to fill tiles

# TV Resolution: #
Click OK to toggle the value. If you have an HD Roku TV, choose 1920. If you have a "4K" Roku TV, choose 3840. If you want to optimize bandwidth, you can choose 640 or 1280 to lower the resolution of the incoming camera streams.

# Show debug borders: #
Click OK to toggle the value.
true = draw blue/green borders around frames as the requests are sent to Security Spy to indicate load status (use only with refresh rate = 1 or 2 FPS)
false = off (recommended)

# Select Cameras: #
Takes you to a page where you can choose which cameras will be included.

Once cameras are chosen, choose **"Start Stream"**

# Notes: #

If you exit the app, it remains installed on your home screen, usually at the bottom of the list of apps and channels (easiest way to navigate to it from home is to go right to channels, then up a few clicks to reach the bottom of the app list.

Security Spy is the property of [bensoftware.com](https://www.bensoftware.com).
Icons in this repo came from the Security Spy application package.
Absolutely no warranties. Use at your own risk.
