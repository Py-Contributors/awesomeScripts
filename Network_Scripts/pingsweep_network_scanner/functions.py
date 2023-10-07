import platform
from datetime import datetime
import subprocess


def instructions():
    print("""
    1. Enter an IP range for the ping sweep.
    2. Enter the range to start ping from.
    3. Enter the range to end ping at.

    Example: -192.168.0
             -2
             -8
    Script will scan from 192.168.0.2 to 192.168.0.8 \n""")


def network_info():
    subnet_ip = input('Enter the SUBNET IP: ')
    first_host = int(input('Enter Starting Range: '))
    last_host = int(input('Enter Ending Range: ')) + 1
    return subnet_ip, first_host, last_host


def network_scan():
    subnet_ip, first_host, last_host = network_info()
    time1 = datetime.now()
    live_hosts = []

    for ip in range(first_host, last_host):
        addr = f"{subnet_ip}.{ip}"
        command = f"ping -n 1 -w 2500 {addr}" if platform.system() == 'Windows' else f"ping -c 1 -W 2 {addr}"
        response = subprocess.run(command, capture_output=True, text=True, shell=True)

        if "TTL" in response.stdout or "ttl" in response.stdout:
            live_hosts.append((addr, 'Live'))

    time2 = datetime.now()
    total = time2 - time1
    print("\nScanning completed in", total)

    return live_hosts
