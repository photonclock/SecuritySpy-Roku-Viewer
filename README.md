# **Security Spy Viewer for Roku**

## **Installation Instructions (Sideloading)**

This app is not available in the public Roku Channel Store. You must install it using Roku's Developer Mode.

### **Prerequisites**

* A Roku device connected to the same network as your computer.  
* The Security\_Spy\_Viewer.zip file from the [Releases page](https://github.com/photonclock/SecuritySpy-Roku-Viewer/releases/latest).

### **Step 1: Enable Developer Mode**

1. Turn on your Roku device and TV.  
2. On your Roku remote, enter the following sequence rapidly:  
   * **Home** (x3)  
   * **Up** (x2)  
   * **Right**  
   * **Left**  
   * **Right**  
   * **Left**  
   * **Right**  
3. Select **Enable installer and restart** on the screen that appears.  
4. Review the license agreement and set a **password** for the rokudev user.  
5. The Roku will reboot.

### **Step 2: Access the Installer**

1. Once the Roku restarts, go to **Settings \> Network \> About** to find the device's **IP Address**.  
2. Open a web browser on your computer and navigate to http://\<ROKU\_IP\_ADDRESS\> (e.g., http://192.168.1.50).  
3. Log in with the username rokudev and the password you created in Step 1\.

### **Step 3: Upload the Application**

1. Click the **Upload** button in the web interface.  
2. Select the Security\_Spy\_Viewer.zip file.  
3. Once the file is uploaded, click **Install**.  
4. The application will immediately launch on your TV.

## **Configuration**

Enter the **Configure** page from the main menu.

**IP and PORT**

* Enter the IP address and Port of your Security Spy server.

**HTTPS mode**

* **true** \= Use HTTPS (you will need a valid and properly configured SSL certificate installed on your Security Spy server, or a reverse proxy).  
* **false** \= Use HTTP (your auth string will be sent in the clear \- safe-ish within a secured LAN, but unsafe via the internet).

**Auth String**

Enter the base64 encoded version of your username:password, as described in the [Security Spy Web Server Spec](https://bensoftware.com/securityspy/web-server-spec.html)

I recommend setting up an alternate user+password in **Security Spy \> Web \> Accounts**, with the permission type for the user limited to "View", e.g.:

* User: rokutv  
* Password: your_password

To convert your username:password to a base64 string, you can do this in Terminal (macOS/Linux):

```echo -n "rokutv:your_password" | base64```

**Tip:** It is easier to use the **Roku Mobile App** on your smartphone to enter this long string.

1. Copy the auth string to your phone's clipboard.  
3. Open the Roku Mobile App and connect to your Roku device or use QR code Roku may display.  
3. Paste the string directly into the text field on the TV.  
   (Note: Don't forget to include the \== that typically occurs at the end of a base64 encoded string.)

**Refresh Rate**

* Click OK to toggle the value.  
* Start with refresh rate \= 1 FPS, and go up from there.  
* I've only tested this with 8 cameras.  
* My testing suggests going no higher than **4x the number of cameras** you have, but your mileage may vary.  
* If you have 16/32/64 cameras, I have no idea how it will perform. Let me know\!

**Maintain Aspect**  

* Click OK to toggle the value.
* **true** \= Camera source aspect ratio is maintained (may have black bars).  
* **false** \= Camera image stretches to fill the tiles.

**TV Resolution**

* Click OK to toggle the value.  
* If you have an HD Roku TV, choose **1920**.  
* If you have a 4K Roku TV, choose **3840**.  
* If you want to optimize bandwidth, you can choose **640** or **1280** to request lower resolution streams from the server.

**Show debug borders**

* Click OK to toggle the value.  
* **true** \= Draws blue/green borders around frames as requests are sent to Security Spy and received, to indicate load status (use only with refresh rate \= 1 or 2 FPS for debugging).  
* **false** \= Off (Recommended).

**Select Cameras**

* Takes you to a grid where you can choose which cameras will be included in the view.

**Once cameras are chosen:**

* Select **Start Stream**.

### **Build from source**

If you clone the repo and want to create your own zip file to upload to Roku:

* Select these files/folders:

* * manifest
* * source
* * images
* * components

* Right-click the selection in the Finder and choose "Compress" to make a ZIP archive.
* Upload the ZIP via the Roku web installer and choose "Replace with ZIP"
* The app will be updated and relaunched with your changes

### **Notes**

* If you exit the app, it remains installed on your home screen, usually at the bottom of the list of apps and channels (easiest way to navigate to it from home is to go right to channels, then up a few clicks to reach the bottom of the app list).  
* Security Spy is the property of [bensoftware.com](https://www.bensoftware.com).  
* Icons in this repo came from the Security Spy application package. Hopefully Ben is cool with that.   
* Absolutely no warranties. Use at your own risk.
