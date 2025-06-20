# Chimera Jade Software

This repo contains the firmware and software for controlling the chimera ruby

---
## Setup Instructions:

### 1. Install Python and LXMF
```bash
sudo apt update && sudo apt install python3-pip python3-dev
pip3 install --upgrade pip
pip3 install rns lxmf
```

### 2. Clone this Repository
Clone this repository in the home directory
### 3. Install Reticulum Config 

Place the configuration file found at /reticulum/config into ~/.reticulum/config

### 4. Start Reticulum
Start reticulum and check its status by running:
```bash
# Start communication client
rnsd &

# Check current network status
rnstatus
```

### 5. TODO
