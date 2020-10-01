from scapy.all import *
import socket
import datetime
import os
from geoip import geolite2
import time

def network_monitoring(pkt):

	time = datetime.datetime.now()
	
	if pkt.haslayer(TCP):

		if socket.gethostbyname(socket.gethostname()) == pkt[IP].dst :
			print(str("[")+str(time)+str("]")+" "+"TCP-IN:{}".format(len(pkt[TCP]))+" Bytes"+""+"SRC-MAC:" +str(pkt.src)+" "+ "DST-MAC:"+str(pkt.dst)+" "+"SRC-PORT:"+str(pkt.sport)+" "+"DST-PORT:"+str(pkt.dport)+""+"SRC-IP:"+str(pkt[IP].src )+" "+"DST-IP:"+str(pkt[IP].dst )+" " +"Location:"+geolite2.lookup(pkt[IP].src).timezone)

		if socket.gethostbyname(socket.gethostname()) == pkt[IP].src :
			print(str("[")+str(time)+str("]")+" "+"TCP-OUT:{}".format(len(pkt[TCP]))+" Bytes"+""+"SRC-MAC:" +str(pkt.src)+" "+ "DST-MAC:"+str(pkt.dst)+" "+"SRC-PORT:"+str(pkt.sport)+" "+"DST-PORT:"+str(pkt.dport)+""+"SRC-IP:"+str(pkt[IP].src )+" "+"DST-IP:"+str(pkt[IP].dst )+" " +"Location:"+geolite2.lookup(pkt[IP].src).timezone)


	if pkt.haslayer(UDP):

		if socket.gethostbyname(socket.gethostname()) == pkt[IP].dst :
			print(str("[")+str(time)+str("]")+" "+"UDP-IN:{}".format(len(pkt[TCP]))+" Bytes"+""+"SRC-MAC:" +str(pkt.src)+" "+ "DST-MAC:"+str(pkt.dst)+" "+"SRC-PORT:"+str(pkt.sport)+" "+"DST-PORT:"+str(pkt.dport)+""+"SRC-IP:"+str(pkt[IP].src )+" "+"DST-IP:"+str(pkt[IP].dst )+" " +"Location:"+geolite2.lookup(pkt[IP].src).timezone)

		if socket.gethostbyname(socket.gethostname()) == pkt[IP].src :
			print(str("[")+str(time)+str("]")+" "+"UDP-OUT:{}".format(len(pkt[TCP]))+" Bytes"+""+"SRC-MAC:" +str(pkt.src)+" "+ "DST-MAC:"+str(pkt.dst)+" "+"SRC-PORT:"+str(pkt.sport)+" "+"DST-PORT:"+str(pkt.dport)+""+"SRC-IP:"+str(pkt[IP].src )+" "+"DST-IP:"+str(pkt[IP].dst )+" " +"Location:"+geolite2.lookup(pkt[IP].src).timezone)


if __name__ == '__main__':
	sniff(prn=network_monitoring)