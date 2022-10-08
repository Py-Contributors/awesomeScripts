# Email sending script using imaplib


## Features of the program:
1. You can delete multiple emails in a sequence.
2. You can even delete mail from a given username.


## Instruction
- There's a check on the account using encryption authentication

-Username: Gmail username
-Password: Gmail password
-Label: If you have a label that holds the emails, specify here.
-Sender: The target sender you want to delete
Usage: python delete_emails.py

# How to delete mail received:
import imaplib
import email
from email.header import decode_header

account credentials
username = "youremailaddress"
password = "password"

create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
authenticate
imap.login(username, password)

select the mailbox I want to delete in
if you want SPAM, use imap.select("SPAM") instead
imap.select("INBOX")

search for specific mails by sender
status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')

to get mails by subject
status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')

to get mails after a specific date
status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
 to get mails before a specific date
status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')

to get all mails
status, messages = imap.search(None, "ALL")

permanently remove mails that are marked as deleted
from the selected mailbox (in this case, INBOX)
imap.expunge()
close the mailbox
imap.close()
logout from the account
imap.logout()
