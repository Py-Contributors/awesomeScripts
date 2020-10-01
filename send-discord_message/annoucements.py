# https://discordapp.com/api/webhooks/758774597415338025/usJ39_wEkWja9ynPB0J-C51IGJg4zXVhs9xHCi6jrxj6haUCQulDD5dqoRD6GlgTUmz8
import requests
from auth import WEBHOOK_URL

data = {"content": "Hello, World!", "username": "Notification_Bot"}
r = requests.post(WEBHOOK_URL, json=data)
print(r)
