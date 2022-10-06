import socks
import socket
import requests


def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


# seed link of dark web
url = "http://facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion"


# establing a proxy connection for dark web scraping
socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                      addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket
socket.getaddrinfo = getaddrinfo

res = requests.get(url)
with open('download.html', 'wb') as f:  # storing the scraped html content
    f.write(res.content)
