"""



Created by Arnav Deep ( https://arnav-deep.github.io/ ).
Connect through my website for queries.

This is a script that pings to check if a server is running or not and
sends emails alerts when the server goes down.
whenever the server is inactive.

Three main functions —
    1. checkinternet: Checks whether internet connection is available or not.
    2. sendmails: Sends mails with a message to list of mail ids.
    3. checkservers: Pings the respective servers and triggers sendmails
                        function if a server is reported to be down.

Two global variables —
    1. mail_list: A list of strings containing email IDs for the mailing list.
                    Add emails as a string to the list. Go to line 204.
    2. ls_servers: A list of a pair of elements in the form of "[server,port]".
                    The server must be a string a the port must be a number.
                    It is not necessary to add a port. Make sure the elements
                    in ls_servers are in the form of list, even if ports
                    are absent. Add servers ad ports, go to line 208.



"""

import socket
import time
import datetime
import smtplib
import ssl


# Socket connections and ping website/server.
# No edit required
def pingaddress(server):
    serverip = server[0]
    if len(server) == 2:
        serverport = str(server[1])
    else:
        serverport = ""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if len(server) == 2:
            unit_result = sock.connect_ex((server[0], server[1]))
        else:
            unit_result = sock.connect_ex((server[0], 80))
        sock.close()
        return unit_result
    except socket.gaierror:
        print("Connection problem with '" + serverip + ":" + serverport
              + "'.\nCheck whether the website/server entered exists or not.")
        exit()


# Check internet connectivity. No edits required here.
# Frequency of pinging can be changed from here. Details in line comments.
def checkinternet():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dtprint = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        if sock.connect_ex(("google.com", 80)) != 0:
            print("Internet connectivity lost at: %s" % dtprint
                  + "Trying again.\n")

            # A small delay of 60 seconds to recheck for internet again.
            # Change the frequency here as per your own use.
            # Inputs only in seconds.
            time.sleep(60)
            checkinternet()
    except socket.gaierror:
        print("Internet connectivity lost at: %s\n" % dtprint
              + "Trying again.\n")
        time.sleep(60)
        checkinternet()


# Sending mail function. Details mentioned in line comments.
# Add your email and password for gmail.
# Edit the message as per your choice.
def sendmails(serverinfo):
    serverip = serverinfo[0]
    if len(serverinfo) == 2:
        serverport = str(serverinfo[1])
    else:
        serverport = ""
    smtp_server = "smtp.gmail.com"
    port = 465

    # add your email here. Make sure to enable access to email by
    # turning on access of less secure apps from this link -
    # "https://myaccount.google.com/lesssecureapps".
    # NOTE: If you do not want to enable access to less secure apps,
    # go through the following doc on how to proceed -
    # "https://developers.google.com/gmail/api/quickstart/python"
    sender_email = ""

    # enter Gmail account password here.
    password = ""

    if len(sender_email) == 0 or len(password) == 0:
        print("Gmail account email ID and password not entered.\n"
              + "Stopping Execution.")
        exit()

    dtprint = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    context = ssl.create_default_context()

    # edit message as required. "Subject:" saves the subject of the email.
    message = "Subject: Website down [" + serverport + "]\n\n" + \
              "http://" + serverip + ":" + serverport + \
              "/ is down. Please check.\n\n" + \
              "The website went down at around " + dtprint + "."

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            for receiver in mail_list:
                server.sendmail(sender_email, receiver, message)
            print("=====================================> "
                  + "Mail sent to the mailing list for server: "
                  + serverip + ":" + serverport
                  + " at time - " + dtprint + "\n")
            server.close()
        except smtplib.SMTPAuthenticationError:
            print("Check Username and password.\n"
                  + "If both are correct then enable access to less secure "
                  + "apps from the link below —\n"
                  + "https://myaccount.google.com/lesssecureapps\n"
                  + "Read the docs below if you do not want to enable access "
                  + "to secure apps. —\n"
                  + "https://developers.google.com/gmail/api/quickstart/python")
            exit()


# Ping the server list provided. No edits required here.
# Frequency of pinging can be changed from here. Details in line comments.
def checkservers():
    num_servers = len(ls_servers)
    ls_result = []
    dtprint = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    for i in range(num_servers):
        unit_result = pingaddress(ls_servers[i])
        ls_result.append(unit_result)

    failed = False

    for i in range(num_servers):
        result = ls_result[i]
        server = ls_servers[i][0]
        if len(ls_servers[i]) == 2:
            port = ls_servers[i][1]
        else:
            port = ""

        # Server is active.
        if result == 0:
            print("%s: %s:%s is working fine" % (dtprint, server, port))

        # Server is down.
        else:

            # A small delay of 120 seconds to recheck the server that
            # was reported down again. This will help in keeping your
            # inbox clean if by chance the server went down for only
            # a small amount of time. Change the time limit here as
            # per your own use.
            # Inputs only in seconds.
            time.sleep(120)

            # Check the server again and ignore sending mail if
            # the server is back up.
            unit_result = pingaddress(ls_servers[i])

            # Server back up again. Mail won't be sent.
            if unit_result == 0:
                continue

            # Server still down. Mail will be sent.
            else:
                print("***************************************************\n"
                      + "%s: %s:%s Website is down\n" % (dtprint, server, port)
                      + "****************************************************\n")
                failed = True
                sendmails(ls_servers[i])

    # A small delay of 300 seconds to wait to check ping the servers again.
    # Change the frequency here as per your own use.
    # Inputs only in seconds.
    time.sleep(300)

    # Further delay of 900 seconds if server was down so as to not
    # clutter inbox with mails. Change the delay as per your use.
    # Inputs only in seconds.
    if failed:
        time.sleep(900)


# List of all emails in the form of string. Details in line 18.
# Example: mail_list = ['abc@xyz.c', 'ab123@bh.ko.jp'].
mail_list = ['abc@yahoo.com']

# List of pairs of servers and ports. A List of lists. Details in line 20.
# Adding port is not necessary. It is just a feature for local servers.
# server must be in the form of string and port(optional) is an integer.
# Adding "https://" is not required.
# Example: ls_servers = [['google.com'], ['192.163.89.23', 8001]].
ls_servers = [['google.com']]

if __name__ == "__main__":
    if mail_list and ls_servers:
        while True:
            checkinternet()
            checkservers()
    else:
        print("Note: List of servers and emails are empty.\n"
              + "Add some values in the lists to run the script.")
