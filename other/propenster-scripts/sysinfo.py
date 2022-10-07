"""
This Script gets some system info of the user's device....
Script Date: Sept, 27, 2020
Author: Propenster
Site: github.com/propenster


Sorry it's going to be a whole messy dump sorry!


"""

import os
import sys
import getpass

# Get os name
print(f"System: {os.name}")
print(f"Platform: {sys.platform}")

# Get environment
print(f"Environment: {os.environ}")
print(f"GET PASS User Info: {getpass.getuser()}")


# Get current working directory
print(f"CWD: {os.getcwd()}")

# Ensure to put a key...parameter..
key = "home"
print(f"Env: {os.getenv(key, default=None)}")

# get group id of the current process...
# not available for windows ..
# only for Unix systems
print(f"Group ID: {os.getgid()}")

# return the current processe' effective user ID
print(os.getguid())
# returns current process real user ID for UNIX
print(os.getuid)

# Get the currently logged in User
# For Unix and Windows...
print(f"User Login: {os.getlogin()}")
# OR


# Return information about the operating system
####
print("\n\n\n\n\n\n\n")
print(f"More OS info: {os.uname()}")

print("\n\nThank you for stopping by...")
