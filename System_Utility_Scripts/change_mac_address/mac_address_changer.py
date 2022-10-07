from argparse import ArgumentParser
import re
from subprocess import PIPE, STDOUT, Popen, call

# setting up argparse
parser = ArgumentParser(description="temporarily change the macaddress of \
        an interface")
parser.add_argument('interface', help="interface name you want the change \
        the mac address")
parser.add_argument('macaddress', help="New Mac address 5F:39:1F:F8:C1:E9")
args = parser.parse_args()

# setting up global variables
interface = args.interface
macaddress = args.macaddress


def check_mac_address(interface):
    '''
    returns try if mac address is valid else raise and print an error
    '''
    command = 'ifconfig ' + str(interface) + '| grep ether'
    interface_check = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT)
    # decoding bytes object to a string
    output = interface_check.communicate()[0].decode("utf-8")
    interface_RE = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if interface_RE:
        return interface_RE.group(0)
    else:
        raise ValueError("The interface doesnt work")
        return


def change_mac_address(interface, macaddress):
    '''
    changes the macaddress
    '''
    try:
        # bringing the interface down
        call(['ifconfig', interface, "down"])
        # change the address
        call(['ifconfig', interface, 'hw', 'ether', macaddress])
        # bringing the interface up
        call(['ifconfig', interface, "up"])
    except Exception as e:
        raise ValueError(f"Error: {e} \nThe interface doesnt work")
        return


if __name__ == "__main__":
    if check_mac_address(interface):
        change_mac_address(interface, macaddress)
        # check if macaddress changed
        if macaddress == check_mac_address(interface):
            print(f"MAC ADDRESS CHANGE TO {macaddress}")
        else:
            print("MAC ADDRESS DIDNT CHANGE")
