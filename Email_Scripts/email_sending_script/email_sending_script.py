import ssl
import smtplib
import mimetypes
import re
import getpass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

PORT = 465


def check_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email.strip())):
        return True
    else:
        return False


print("Welcome to Email sending script!\n \
    Read the README.md file for more details\n\n")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    while True:
        # checking sender's email and exit from middle of program
        senders_email = input("Enter the sender's \
            gmail email('' to exit): ").lower()
        if senders_email == '':
            break
        while not check_email(senders_email):
            senders_email = input("Enter the sender's gmail email \
                correctly('' to exit): ").lower()
        password = getpass.getpass(prompt="Enter the sender's \
            gmail password: ")
        try:
            server.login(senders_email, password)
            print("Login sucessfull!\n\n")
        except Exception:
            print("Login was unsucessfull! Try again! \n\n")
            continue
        recivers_email = input("Enter the reciever(s) email. \
            Seperate be comma(',')('' to exit): ").lower()
        if recivers_email == '':
            break
        while not all(map(lambda x: check_email(x),
                      recivers_email.split(","))):
            recivers_email = input("Enter the reciever(s) email correctly. \
                Seperate by comma(',')('' to exit): ")
        subject = input("Enter e-mail subject: ")
        message = input("Enter e-mail body: ")
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["To"] = recivers_email
        msg["From"] = senders_email
        msg.attach(MIMEText(message, "plain"))
        Attachement = input("\nDo you want to add attachment?(Y/N): ")
        Attachement = Attachement.strip().lower()
        if Attachement == "y":
            numberOfAttachment = input("How many attachements to add:")
            numberOfAttachment = int(numberOfAttachment)
            for i in range(numberOfAttachment):
                path = input(f"Enter absolute path to the attachment {i+1}: ")
                filename = ""
                ctype, encoding = mimetypes.guess_type(path)
                if ctype is None or encoding is not None:
                    ctype = "application/octet-stream"
                maintype, subtype = ctype.split("/", 1)
                if maintype == "text":
                    fb = open(path)
                    files = MIMEText(fb.read(), _subtype=subtype)
                    filename = fb.name
                    fb.close()
                elif maintype == "image" or maintype == "audio":
                    fb = open(path, "rb")
                    files = MIMEImage(fb.read(), _subtype=subtype)
                    filename = fb.name
                    fb.close()
                else:
                    fp = open(path, "rb")
                    files = MIMEBase(maintype, subtype)
                    files.set_payload(fp.read())
                    filename = fp.name
                    fp.close()
                encoders.encode_base64(files)
                files.add_header("Content-Disposition",
                                 "attachment", filename=filename)
                msg.attach(files)
        server.send_message(msg)
        print("Email sent!\n\n")
        choice = input("Send another email?(y/n): ").strip().lower()
        if choice != 'y':
            break
