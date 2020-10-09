'''
Script to send message using Telegram
Yorozuya3 <yorozuya3@protonmail.com>
Licensed under MIT license
'''

from telethon import TelegramClient
import argparse
import configparser

# Usage python send_telegram_message.py "username, number or id" "message"
parser = argparse.ArgumentParser(description='Send message to telegram user from terminal')
parser.add_argument('user', type=str, help='Telegram username, number or id')
parser.add_argument('msg', type=str, help='Message to send to user')
parser.add_argument('api_id', type=str, help="Your api id from https://my.telegram.org, under API Development", default=None, nargs='?') 
parser.add_argument('api_hash', type=str, help="Your api hash from https://my.telegram.org, under API Development", default=None, nargs='?') 
args = parser.parse_args()

api_id = args.api_id
api_hash = args.api_hash
config = configparser.ConfigParser()
config.read('config.ini')
if api_id is None: 
    api_id = config['API']['ID']

if api_hash is None: 
    api_hash = config['API']['HASH']

async def main():
    await client.send_message(args.user, args.msg)

with TelegramClient('session', api_id, api_hash) as client:
    client.loop.run_until_complete(main())

