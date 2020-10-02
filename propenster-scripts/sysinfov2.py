"""
Now, Let's use lib_platform
to get practical, refined info about our system....

Script Date: Sept, 27th, 2020
Author: Propenster

"""

import lib_platform
import wmi

# Returns windows, or Unix or Cent-Os etc
print(f"System Info: {lib_platform.system}")

# Get LoggedIn Username
print(f"User: {lib_platform.username}")
# Get hostname
print(f"Hostname: {lib_platform.hostname}")

# Check if the user is Admin on the system...
print(f"User: {lib_platform.is_user_admin}")

# Get User Home
print(f"User Home: {lib_platform.path_userhome}")

###
###
# Using wmi for windows only...

# Initialize a Window Management Interface instance....
c = wmi.WMI()
# Get the current system....
sysinfo = c.Win32_ComputerSystem()[0]

# Now dump stuff
print("\n\n\n")
print("Getting Windows System Information")
print("...\t...\t...")
print(f"System Manufacturer (HP, Lenovo, DELL etc): {sysinfo.Manufacturer}")
print(f"System Model: {sysinfo.Model}")
print(f"System Name: {sysinfo.Name}")
print(f"Number of Processors: {sysinfo.NumberOfProcessors}")
print(f"System Type: {sysinfo.SystemType}")
print(f"System Family: {sysinfo.SystemFamily}")

# Be more dynamic
print(
    "User:  %s is currently logged in on a %s laptop - %s"
    % (lib_platform.username, sysinfo.Manufacturer, sysinfo.Name)
)
