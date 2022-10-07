from socket import *
import sys
import argparse
import os
from threading import Thread
from ftplib import FTP
import ftplib
import subprocess
import getpass
import pam

state = 1
promo = 1
hashy = 0
argumentList = sys.argv
serverName = argumentList[1]
# serverName = '127.0.0.1'
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def authentication():
	global state
	cauth = 1
	while (cauth == 1):
		username = raw_input("Username: ")
		clientSocket.send(username.encode())
		password = getpass.getpass(prompt="Enter the Password: ")
		clientSocket.send(password.encode())
		conn = clientSocket.recv(1024)
		if (conn == "success"):
			state = 1
			cauth = 0
			print("Connection Authenticated")
		else:
			state = 0
			cauth = 1
			print("Connection failed to Authenticate")
			# clientSocket.close()


def listt(modifiedSentence):
	cmd = "dir"
	process = subprocess.Popen(
	    'ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(result, error) = process.communicate()
	rc = process.wait()
	print(result)


def pathh(modifiedSentence):
	pt = os.getcwd()
	print(pt)

def cdd(modifiedSentence):
	os.chdir(modifiedSentence[1])
	cwd = os.getcwd()
	string = 'Current directory:' + ' ' + cwd
	print(string)

def mkdrr(modifiedSentence):
	if not os.path.exists(modifiedSentence[1]):
		os.mkdir(modifiedSentence[1])
		string = 'Directory' + ' ' + modifiedSentence[1] + ' ' + 'Created'
	else:
		string = 'Directory' + ' ' + modifiedSentence[1] + ' ' + 'already exists'
	print(string)

def renmm(modifiedSentence):
	os.rename(modifiedSentence[1], modifiedSentence[2])
	string = 'Filename changed to:' + ' ' + modifiedSentence[2]
	print(string)

def remvdir(modifiedSentence):
	try:
		os.rmdir(modifiedSentence[1])
		string = modifiedSentence[1] + ' ' + 'removed'
	except:
		try :
			shutil.rmtree(modifiedSentence[1])
			string = modifiedSentence[1] + ' ' + 'removed'
		except :
			string = "Error in command"	 
	print(string)
	

	
def gett(modifiedSentence):
	b = int(modifiedSentence[2])
	t = open(modifiedSentence[1], "wb+")
	server3Name = argumentList[1]
	# server3Name = '127.0.0.1'
	server3Port = 12006
	client3Socket = socket(AF_INET, SOCK_STREAM)
	client3Socket.connect((server3Name,server3Port))
	n = 0
	i = (b) % (1024)
	while n < (b - i) :
		l = client3Socket.recv(1024)
		t.write(l)
		if(hashy == 1):
			print("#"),
		n = n + len(l)
	while n < b :
		l = client3Socket.recv(1)
		t.write(l)
		n = n + 1
	if(hashy == 1):
		print(" ")	
	t.close()
	string = modifiedSentence[1] + ' ' + 'transfered successfully'
	print(string)
	client3Socket.close()
	clientSocket.send("close".encode())


def putt(modifiedSentence):
	b = os.path.getsize(modifiedSentence[1])
	string = modifiedSentence[0] + ' ' + modifiedSentence[1] + ' ' + str(b)
	server2Name = argumentList[1]
	# server2Name = '127.0.0.1'
	server2Port = 12003
	client2Socket = socket(AF_INET, SOCK_STREAM)
	client2Socket.connect((server2Name,server2Port))
	client2Socket.send(string.encode())
	ff = open(modifiedSentence[1], "rb+")
	n = (b) / (1024)
	i = (b) % (1024)
	while n != 0 :
		oo = ff.read(1024)
		client2Socket.send(oo)
		if(hashy == 1):
			print("#"),
		n = n - 1
	oo = ff.read(i)		
	client2Socket.send(oo)
	if(hashy == 1):
		print(" ")
	ff.close()
	string = modifiedSentence[1] + ' ' + 'transfered successfully'
	print(string)
	client2Socket.close()
	clientSocket.send("close".encode())
	
cmnd = [ "ls" , "dir" ,"quit" , "bye" , "exit" , "!ls" , "pwd" , "!pwd" , "cd" , "!cd" , "lcd" , "prom" , "hash" , "mkdir" , "mdelete" , "!mkdir" , "rename" , "!rename" , "rmdir" , "!mdelete" , "!rmdir" , "delete" , "!delete" , "get" , "put" , "mget" , "mput" ]

def fuuun(sentence) :
	global state
	clientSocket.send(sentence.encode())
	modifiedSentence = clientSocket.recv(2147483645)
	
	MSentence = modifiedSentence.decode()
	modifiedSentence = modifiedSentence.split()
	le = len(modifiedSentence)
	e = "Error in command"
	try :
		if modifiedSentence[0] == "lisst":
			try:
				listt(modifiedSentence)
        		except:
        	  		print(e)
		if (modifiedSentence[0] == "help" or modifiedSentence[0] == "?"):
			try:
				for i in range(len(cmnd)):
					if ((i + 1) % 5 == 0):
						print(cmnd[i])
					else:
						print(str(cmnd[i])+ "\t\t"),
				print(" ")
        		except :
        	  		print(e)
		elif modifiedSentence[0] == "prom":
        		global promo
			if(promo == 1):
				promo = 0;
				print("prom turn OFF")
			else:
				promo = 1;
				print("prom turn ON")
		elif modifiedSentence[0] == "hash":
        		global hashy
			if(hashy == 1):
				hashy = 0;
				print("hash turn OFF")
			else:
				hashy = 1;
				print("hash turn ON")
        	elif (modifiedSentence[0] == "bye" or modifiedSentence[0] == "quit" or modifiedSentence[0] == "exit"):
			try:
				clientSocket.close()
				print("Good bye..")
				state = 0
        		except :
        	  		print(e)  		
        	elif modifiedSentence[0] == "path":
			try :
		        	pathh(modifiedSentence)
        		except :
        	  		print(e)	
        	elif modifiedSentence[0] == "cdd":
			try :
				cdd(modifiedSentence)
			except :
        	  		print(e)
          		
		elif modifiedSentence[0] == "mkdr":
			try:
				mkdrr(modifiedSentence)	
			except:
          			print(e)	
		elif modifiedSentence[0] == "renm":
			try :
				renmm(modifiedSentence)	
			except :
        	  		print(e)	
		elif modifiedSentence[0] == "removedr":	
			remvdir(modifiedSentence)
			
		elif modifiedSentence[0] == "mdelete":
			try :
				d = 1
				while(d < le):
					string = modifiedSentence[d] + ' ' + 'removed'
					print(string)
					d = d + 1;
			except :
          			print(e)		
			
		elif modifiedSentence[0] == "!mdelete":
			try :
				d = 1
				while(d < le):
					os.remove(modifiedSentence[d])
					string = modifiedSentence[d] + ' ' + 'removed'
					print(string)
					d = d + 1;
			except :
          			print(e)	
          	elif modifiedSentence[0] == "!delete":
			try :
				os.remove(modifiedSentence[1])
				string = modifiedSentence[1] + ' ' + 'removed'
				print(string)
			except :
          			print(e)							
		elif modifiedSentence[0] == "get":
			gett(modifiedSentence)

		elif modifiedSentence[0] == "put":
			putt(modifiedSentence)
    		      		   			
		else :
			print(MSentence)
		
	except :
		print(MSentence)			

		
authentication()
while(state == 1):
	# clientSocket.connect((serverName,serverPort))
	sentence = raw_input("ftp> ")
	df = sentence.split()
	si = len(df)
	if (si == 0):
		continue
	if(df[0] == "mput") :
		x = 1;
		while(x < si):
			ser = "put" + " " + df[x]
			serr = ser.split()
			print(ser)
			x = x + 1;
			if(promo == 1):
				print("do you want to transfer (y/n): ")
				ans = raw_input("")
				if(ans[0] == "n" or ans[0] == "N") :
					continue
			fuuun(ser)
			
			
	elif(df[0] == "mget") :
		y = 1;
		while(y < si):
			ser = "get" + " " + df[y]
			serr = ser.split()
			print(ser)
			y = y + 1;
			if(promo == 1):
				print("do you want to transfer (y/n): ")
				ans = raw_input("")
				if(ans[0] == "n" or ans[0] == "N") :
					continue
			fuuun(ser)
					
	
	else :
		fuuun(sentence)		
	
