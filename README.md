# Development Notes

### Device 1: Jade 1

Username: jade1
Password: naima

Device 2: Jade 2

Username: jade2
Password: naima

# Flashing PI Image:

You must have the Raspberry Pi Imager application installed on your device before proceeding

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

# Development Workflow

Currently utilizing the Remote-SSH plugin in Visual Studio. It allows you to connect to the device and edit the files and directories directly.

# Setup

## To add the pi to your list of devices:

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

## Assigning a static IP Address to the PI
Ran into an issue of constantly having to edit the config file for the Remote-SSH extention in VS-Code. By assisgning a static IP (only for dev devices), a new IP is not assigned every startup.

1. SSH into the PI
2. Set the static IP for the USB gadget
>sudo nmcli connection modify "USB Gadget (client)"\
>ipv4.addresses 192.168.2.2/24\
>ipv4.method manual
3. Set DNS
>sudo nmcli connection modify "USB Gadget (client)"\
>ipv4.dns "1.1.1.1 8.8.8.8"
4. Restart PI
















---
# Old Readme...

## Chimera Jade Software
This repo contains the firmware and software for controlling the chimera ruby

## Setup Instructions:
1. Install Python and LXMF
> sudo apt update && sudo apt install python3-pip python3-dev
> pip3 install --upgrade pip
> pip3 install rns lxmf
2. Clone this Repository
	Clone this repository in the home directory

3. Install Reticulum Config
	Place the configuration file found at /reticulum/config into ~/.reticulum/config

4. Start Reticulum
	Start reticulum and check its status by running:

## Start communication client
rnsd &

## Check current network status
rnstatus
5. TODO