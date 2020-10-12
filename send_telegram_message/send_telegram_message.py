'''
Script to send message using Telegram
Yorozuya3 <yorozuya3@protonmail.com>
Licensed under MIT license
'''

import argparse
import configparser
from telethon import TelegramClient


def main():
    """Main function to send telegram message"""
    # Usage python send_telegram_message.py "username, number or id" "message"
    parser = argparse.ArgumentParser(description='Send message to telegram user from terminal')
    parser.add_argument('user', type=str, help='Telegram username, number or id')
    parser.add_argument('msg', type=str, help='Message to send to user')
    parser.add_argument('api_id', type=str, default=None, nargs='?',
                        help="Your api id from https://my.telegram.org, under API Development")
    parser.add_argument('api_hash', type=str, default=None, nargs='?',
                        help="Your api hash from https://my.telegram.org, under API Development")
    args = parser.parse_args()

    api_id = args.api_id
    api_hash = args.api_hash
    config = configparser.ConfigParser()
    config.read('config.ini')
    if api_id is None:
        api_id = config['API']['ID']

    if api_hash is None:
        api_hash = config['API']['HASH']

    async def send_message():
        await client.send_message(args.user, args.msg)

    with TelegramClient('session', api_id, api_hash) as client:
        client.loop.run_until_complete(send_message())


if __name__ == '__main__':
    main()
