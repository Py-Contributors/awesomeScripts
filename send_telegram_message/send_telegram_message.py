'''
Script to send message using Telegram
Yorozuya3 <yorozuya3@protonmail.com>
Licensed under MIT license
'''

from telethon import TelegramClient, sync
import argparse

#Usage python send_telegram_message.py "username, number or id" "message"
parser = argparse.ArgumentParser(description='Send message to telegram user from terminal')
parser.add_argument('user', type=str, help='Telegram username, number or id')
parser.add_argument('msg', type=str, help='Message to send to user')
args = parser.parse_args()

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 
api_hash = ''
client = TelegramClient('session_name', api_id, api_hash)
client.start()
client.send_message(args.user, args.msg)
