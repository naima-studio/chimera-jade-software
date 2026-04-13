###Device Information

**Device 1:** Jade 1

Username: jade1
Password: naima

**Device 2:** Jade 2

Username: jade2
Password: naima

#####**Flashing PI Image:**

__You must have the Raspberry Pi Imager application installed on your device before proceeding__

1. Clone the Repository
	https://github.com/raspberrypi/rpi-imager/tree/main/doc/local_json
2. Navigate to the Directory
	.../rpi-imager/doc/local_json
3. Run Script
	./create_local_json.py --online --capabilities usb_otg --device-capabilities usb_otg
4. Open in file manager and click on the file
	create_local_json.py - (this will open your Raspberry Pi Imager)
5. Continue with setup process. Durring this, add:
	- A user and password
	- Enable SSH
	- Enable USB Gadget Mode
6. After PI image has been flashed
	Boot the pi and once it is completed, reboot the pi. 
7. Plug in your usb cable to the non-power input on the pi.

> Now you're good to go with SSH over USB. Here is the link[https://www.raspberrypi.com/news/usb-gadget-mode-in-raspberry-pi-os-ssh-over-usb/] to the original article with these directions. 

###**Development Workflow**

Currently utilizing the __Remote-SSH__ plugin in Visual Studio. It allows you to connect to the device and edit the files and directories directly.

####Setup

To add the pi to your list of devices:

1. Know your devices IP, User, and Password information. 
2. Have your PI connected via wifi or usb and have SSH enabled and running.
3. Edit the Configuration file of the Remote-SSH and add (example):
   - Host jade1
    	HostName 192.168.2.2
    	User jade1
    	IdentityFile ~/.ssh/id_rsa
    	ServerAliveInterval 30
    	ServerAliveCountMax 3
4. It will then connect to the PI and you should be able to develop on it from here directly.

