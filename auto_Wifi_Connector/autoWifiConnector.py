# Auto Wifi Connector
# Process Of Working:
'''
1. Check the saved networks in the system.
2. Find active or available network from it.
3. Ask user to connect to which network out of those.
4. Disconnect present or current network if connected.
5. If connection fails or is denied, exit the program.
6. If its accessed, then connect.
7. Succesfully Connected!!!!

'''

import os
import sys

# Reading the command in the command prompt.
show_saved_network_cmd = os.popen("netsh wlan show profiles").read()
# Shows available network
show_available_network_cmd = os.popen("netsh wlan show network").read()
# Show the connections available to user in display screen
print("Available Networks are: \n", show_available_network_cmd)
# Ask for the preffered connection for the user
preffered_network_ssid = input("Enter preferred Wifi for your Connection: ")
# Disconnects the current connection
disconnect_current_network = os.popen("netsh wlan disconnect").read()

print(disconnect_current_network)

# If preferred id is in saved connection, then connect, else go and connect
if preffered_network_ssid not in show_saved_network_cmd:
    print("The network", preffered_network_ssid, " is not saved in the System")
    print("Connection establishment UNSUCCESSFUL")
    sys.exit()
else:
    print("The network", preffered_network_ssid, " is saved in the System")
    print("Connection establishment in Process")


# Check if the Network preferred is available or not
while True:
    if preffered_network_ssid in show_available_network_cmd:
        print("The preferred Network", preffered_network_ssid, "is Found")
        break


print("------Connecting------")
# Connect with the network
os.popen("netsh wlan connect name=" + '"' + preffered_network_ssid + '"')
