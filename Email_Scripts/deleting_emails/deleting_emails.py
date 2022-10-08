import imaplib
import sys

args = dict([arg.split('=') for arg in sys.argv[1:]])

print("Log into Gmail with username: %s\n" % args['username'])
server = imaplib.IMAP4_SSL('imap.gmail.com')
connection_message = server.login(args['username'], args['pw'])
print(connection_message)

if args.get('label'):
    print("Using label: %s" % args['label'])
    server.select(args['label'])
else:
    print("Using inbox")
    server.select("inbox")

print("Searching emails from %s" % args['sender'])
result_status, email_ids = server.search(None, '(FROM "%s")' % args['sender'])
email_ids = email_ids[0].split()

if len(email_ids) == 0:
    print("No emails found, finishing...")

else:
    print("%d Emails found, sending to trash folder..." % len(email_ids))
    server.store('1:*', '+X-GM-LABELS', '\\Trash')
    server.expunge()

print("Done deleting.")
