try:
    from discord_webhook import DiscordWebhook
except ImportError:
    from pip._internal import main as pip

    pip(["install", "--user", "discord-webhook"])
    from discord_webhook import DiscordWebhook
from auth import WEBHOOK_URL

webhook = DiscordWebhook(url=WEBHOOK_URL, content="Here is the content")
response = webhook.execute()

# documentation :- https://github.com/lovvskillz/python-discord-webhook