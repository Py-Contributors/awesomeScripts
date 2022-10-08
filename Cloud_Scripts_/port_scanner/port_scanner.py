import concurrent.futures
import argparse
import socket
import time

common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "TELNET",
    "25": "SMTP",
    "53": "DNS",
    "69": "TFTP",
    "80": "HTTP",
    "109": "POP2",
    "110": "POP3",
    "123": "NTP",
    "137": "NETBIOS-NS",
    "138": "NETBIOS-DGM",
    "139": "NETBIOS-SSN",
    "143": "IMAP",
    "156": "SQL-SERVER",
    "389": "LDAP",
    "443": "HTTPS",
    "546": "DHCP-CLIENT",
    "547": "DHCP-SERVER",
    "995": "POP3-SSL",
    "993": "IMAP-SSL",
    "2086": "WHM/CPANEL",
    "2087": "WHM/CPANEL",
    "2082": "CPANEL",
    "2083": "CPANEL",
    "3306": "MYSQL",
    "8443": "PLESK",
    "10000": "VIRTUALMIN/WEBMIN",
}


parser = argparse.ArgumentParser()
parser.add_argument("host", help="host IP")
parser.add_argument("--start", "-s", help="Start Port")
parser.add_argument("--end", "-e", help="End Port")
args = parser.parse_args()
host = args.host

if args.start:
    start_port = int(args.start)
else:
    start_port = 0

if args.end:
    end_port = int(args.end)
else:
    end_port = 65535  # No end port = we scan all

print("Scanning %s for open ports.\n" % host)


def scanner(port):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.settimeout(0.3)
    skt.connect((host, port))
    try:
        port_name = " (%s)" % common_ports.get(str(port), "")
        if port_name == " ()":
            port_name = ""
        ext_port_name = "%s%s" % (str(port), port_name)
    except KeyError:
        ext_port_name = str(port)
    print(" - Port {} is open".format(ext_port_name))


t1 = time.perf_counter()

ports = [j for j in range(start_port, end_port + 1)]

# 2x the deafult threads for 4 cores processor
with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
    executor.map(scanner, ports)

t2 = time.perf_counter()
print("Finished scannning for %d ports in %s seconds" % (len(ports) , str(t2 - t1)))
