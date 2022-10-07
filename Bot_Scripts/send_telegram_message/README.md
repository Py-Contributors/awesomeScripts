# Send telegram messages
Small client to send telegram messages. For using it, you must get your own api-id and api-hash from https://my.telegram.org, under API Development. You can set it in config.ini or use it as arguments. 

usage: send_telegram_message.py [-h] user msg [api_id] [api_hash]

Send message to telegram user from terminal

positional arguments:
  user        Telegram username, number or id
  msg         Message to send to user
  api_id      (Optional) Your api id from https://my.telegram.org, under API Development
  api_hash    (Optional) Your api hash from https://my.telegram.org, under API Development

optional arguments:
  -h, --help  show this help message and exit

