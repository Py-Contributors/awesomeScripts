#!/usr/bin/python
from socket import *
import sys
import argparse
import os
from threading import Thread
from ftplib import FTP
import ftplib
import subprocess
import getpass
import shutil
import pam
import time

from contextlib import contextmanager
state = 1
serverPort = 12009
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")


def auth():
    global state
    sauth = 1
    while (sauth == 1):
        username = connectionSocket.recv(1024).decode()
        print(username)
        password = connectionSocket.recv(1024).decode()
        print(password)
        if (not pam.authenticate(username, password)):
            connectionSocket.send(("failed").encode())
            sauth = 1
            state = 0
            # connectionSocket.close()
        else:
            connectionSocket.send(("success").encode())
            state = 1
            sauth = 0


def lss(sentence):
    cmd = "dir"
    prs = subprocess.Popen(('ls -al'), shell=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (result, error) = prs.communicate()
    rc = prs.wait()
    connectionSocket.send(result.encode())


def cwdd(sentence):
    connectionSocket.send(os.getcwd().encode())


def cdd(sentence):
    os.chdir(sentence[1])
    cwd = os.getcwd()
    connectionSocket.send(cwd.encode())
    print("Current directory:", cwd)


def mkdirr(sentence):
    if not os.path.exists(sentence[1]):
        os.mkdir(sentence[1])
        string = 'Directory' + ' ' + sentence[1] + ' ' + 'Created'
    else:
        string = 'Directory' + ' ' + sentence[1] + ' ' + 'already exists'
    connectionSocket.send(string.encode())


def renamee(sentence):
    os.rename(sentence[1], sentence[2])
    string = 'Filename changed to:' + ' ' + sentence[2]
    connectionSocket.send(string.encode())


def removee(sentence):
    try:
        os.rmdir(sentence[1])
        string = sentence[1] + ' ' + 'removed'
    except:
        try:
            shutil.rmtree(sentence[1])
            string = sentence[1] + ' ' + 'removed'
        except:
            string = "Error in command"
    connectionSocket.send(string.encode())


def gette(sentence):
    b = os.path.getsize(sentence[1])
    string = sentence[0] + ' ' + sentence[1] + ' ' + str(b)
    connectionSocket.send(string.encode())
    server3Port = 12006
    server3Socket = socket(AF_INET, SOCK_STREAM)
    server3Socket.bind(('', server3Port))
    server3Socket.listen(1)
    connection3Socket, addr = server3Socket.accept()
    f = open(sentence[1], "rb+")
    n = (b) / (1024)
    i = (b) % (1024)
    while n != 0:
        o = f.read(1024)
        connection3Socket.send(o)
        n = n - 1
    o = f.read(i)
    connection3Socket.send(o)
    f.close()
    tmp = connectionSocket.recv(1000).decode()
    connection3Socket.close()


def putt(sentence):
    string = sentence[0] + ' ' + sentence[1]
    connectionSocket.send(string.encode())
    server2Port = 12003
    server2Socket = socket(AF_INET, SOCK_STREAM)
    server2Socket.bind(('', server2Port))
    server2Socket.listen(1)
    connection2Socket, addr = server2Socket.accept()
    sentence = connection2Socket.recv(2048).decode()
    sentence = sentence.split()
    b = int(sentence[2])
    tt = open(sentence[1], "wb+")
    n = 0
    i = (b) % (1024)
    while n < (b - i):
        ll = connection2Socket.recv(1024)
        tt.write(ll)
        n = n + len(ll)
    while n < b:
        ll = connection2Socket.recv(1)
        tt.write(ll)
        n = n + 1
    tt.close()
    tmp = connectionSocket.recv(1000).decode()
    connection2Socket.close()


def tmp():
    global state
    while (state == 1):
        #connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        osentence = sentence
        sentence = sentence.split()
        b = len(sentence)
        if (b == 0):
            continue
        print(b)
        e = "Error in command"
        if (sentence[0] == "ls" or sentence[0] == "dir"):
            try:
                print(sentence)
                lss(sentence[0])
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!ls":
            try:
                print(sentence)
                string = "lisst"
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "bye":
            try:
                print(sentence)
                string = "bye"
                connectionSocket.send(string.encode())
                time.sleep(3)
                connectionSocket.close()
                state = 0

            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "pwd":
            try:
                print(sentence)
                cwdd(sentence[0])
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!pwd":
            try:
                print(sentence)
                string = "path"
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "cd":
            try:
                print(sentence)
                cdd(sentence)
            except:
                connectionSocket.send(e.encode())
        elif (sentence[0] == "!cd" or sentence[0] == "lcd"):
            try:
                print(sentence)
                string = 'cdd' + ' ' + sentence[1]
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "prom":
            try:
                print(sentence)
                string = "prom"
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "hash":
            try:
                print(sentence)
                string = "hash"
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "mkdir":
            try:
                print(sentence)
                mkdirr(sentence)
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!mkdir":
            try:
                print(sentence)
                string = 'mkdr' + ' ' + sentence[1]
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "rename":
            try:
                print(sentence)
                renamee(sentence)
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!rename":
            try:
                print(sentence)
                string = 'renm' + ' ' + sentence[1] + ' ' + sentence[2]
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "rmdir":
            print(sentence)
            removee(sentence)

        elif sentence[0] == "!rmdir":
            try:
                print(sentence)
                string = 'removedr' + ' ' + sentence[1]
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())

        elif sentence[0] == "delete":
            try:
                print(sentence)
                os.remove(sentence[1])
                string = sentence[1] + " " + "removed"
                connectionSocket.send(string.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!delete":
            try:
                print(sentence)
                connectionSocket.send(osentence.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "mdelete":
            try:
                print(sentence)
                d = 1
                while (d < b):
                    os.remove(sentence[d])
                    d = d + 1
                connectionSocket.send(osentence.encode())
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "!mdelete":
            try:
                print(sentence)
                connectionSocket.send(osentence.encode())
            except:
                connectionSocket.send(e.encode())

        elif sentence[0] == "get":
            try:
                print(sentence)
                gette(sentence)
            except:
                connectionSocket.send(e.encode())
        elif sentence[0] == "put":
            try:
                print(sentence)
                putt(sentence)
            except:
                connectionSocket.send(e.encode())

        else:
            s = "-"
            s = s.join(sentence)
            connectionSocket.send(s.encode())


i = 1
while (1):
    connectionSocket, addr = serverSocket.accept()
    auth()
    tmp()
    print("{} = i".format(i))
    i += 1
