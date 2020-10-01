import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email import encoders
from email.mime.base import MIMEBase
import mimetypes


port= 465

print("Welcome to Email sending script!\nRead the README.md file for more details\n\n")


senders_email = input("Enter the sender's gmail: ")
recivers_email = input("Enter the reciever's gmail: ")
password = input("Enter the serder's gmail password: ")
context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(senders_email,password)
        print("Login sucessfull!")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = recivers_email
        msg['From'] = senders_email
        msg.attach(MIMEText(message, 'plain'))
        Attachement = input("Do you want to add attachement?(Y/N): ")
        if(Attachement == 'y' or Attachement == 'Y'):
            numberOfAttachment = int(input("How many attachement do you want to add: "))
            for i in range(numberOfAttachment):
                path = input(f'Enter absolute path to the attachement {i+1}: ')
                filename = ''
                ctype, encoding  = mimetypes.guess_type(path)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    fb = open(path)
                    files = MIMEText(fp.read(),_subtype=subtype)
                    filename = fb.name
                    fb.close()
                elif maintype == 'image':
                    fb = open(path,'rb')
                    files = MIMEImage(fb.read(),_subtype=subtype)
                    filename = fb.name
                    fb.close()
                elif maintype == 'audio':
                    fp = open(path, 'rb')
                    files = MIMEAudio(fp.read(), _subtype=subtype)
                    filename = fp.name
                    fp.close()
                else:
                    fp = open(path, 'rb')
                    files = MIMEBase(maintype, subtype)
                    files.set_payload(fp.read())
                    filename = fp.name
                    fp.close()
                    encoders.encode_base64(files)
                files.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(files)
        server.send_message(msg)
        print("Email sent sucessfully!")
    except: 
        print("Login was unsucessfull! read the README.md file for instruction")
   
