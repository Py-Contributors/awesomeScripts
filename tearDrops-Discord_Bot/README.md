# Tear Drops

[![built-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Vyvy-vi/)
<p>
<a href="https://raw.githubusercontent.com/Py-Contributors/awesomeScripts/master/LICENSE"><img src="https://img.shields.io/github/license/Py-Contributors/awesomeScripts?style=for-the-badge" alt="MIT license"></a>
<a href="https://discord.gg/JfbK3bS"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
</p>

A discord bot wrapped around the theme of tears and crying.
In concept, the idea is absurd but that's more of a reason to make this. :)
The bot uses tears as an economy and you can "cry" to get daily credit tears.

NOTE- It is recommended that you add your own discord token while running the bot.
[The token provided in the bot is a 'mock' token and might not work after some time]

- [Invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=627772985872220161&permissions=379968&scope=bot)
- To test the bot join this [Support Server](https://discord.gg/8HsG4Pj)
   *NOTE- Bot is not active 24x7 as it is hosted on a server that is busy doing protein analysis for covid-19. To get a sample, join* [TearDropsSupport](https://discord.gg/Q4hxrDF) and ping **@Tissue**

## Hosting the bot on your own machine:
- NOTE: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our the py-awesomescripts server). 
- Clone this repo using `git clone`
- cd into the bot folder.
- Add obtained **token** into the setup.py file line-1. token = "your **token**"
- Install discord.py module:
  ```
    python -m pip install discord.py
  ```
- Install requirements from requirements.txt
  ```
    pip install -r requirements.txt
  ```
- Run the bot using: `python main.py`
- Enjoy! (don't forget to add your own bot into your discord server by generating an invite link from the discord developers application page in [OAuth2 section](https://discord.com/developers/applications/) and choose application and check Oauth2 section)
- You may do bug-reporting or ask for help in the AwesomeScripts server or on the SupportServer... or just open an issue on this repo.

## Requirements:
- python 3
- discord(rewrite branch)
- asyncio(inbuilt with python3.4)
- sqlite3
- wolframalpha
- wikipedia
- requests
- sys

## TODO- This isn't complete yet, more functionality will be added in say like a week or so
