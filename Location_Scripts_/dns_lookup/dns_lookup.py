import socket


def ip_lookup(hostname):
    return str(socket.gethostbyname(hostname))


def hostname_lookup(ip):
    return str(socket.gethostbyaddr(ip)[0])


def dns_lookup(txt, func):
    while True:
        request = str(input("Please input a " + txt + ": "))
        try:
            if txt == 'ip':
                print("The hostname for that IP address is: " + func(request))
                return
            else:
                print("The IP address for that hostname is: " + func(request))
                return
        except Exception as e:
            print(str(e))
            print("Please make sure you are inputing a valid " + txt)
            try_again = input("Do you want to try again (y/n): ")
            try_again = try_again.lower()
            if try_again != 'y':
                return


def ip_lookup1():
    dns_lookup("hostname", ip_lookup)


def hostname_lookup1():
    dns_lookup("ip", hostname_lookup)


def handle_choice():
    print("1: Find IP address based on a website/hostname")
    print("2: Find website/hostname based on IP address")
    choice = str(input("Select an option (1 or 2): "))
    if choice == "1":
        ip_lookup1()
    else:
        hostname_lookup1()


handle_choice()
