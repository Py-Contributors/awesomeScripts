# TODO - transfer, casino, etc commands

import ssl
import discord
from discord.ext import commands, tasks
from itertools import cycle

from pymongo import MongoClient

import os
import asyncio
import sys

# modules for database 
import json
from setup import path_db, TOKEN

# modules for wiki and wolfram queries
import wolframalpha
import wikipedia
import requests

# Standard modules
import random
import math
import time
import aiohttp

# mongoDB Client
DB_CLIENT = MongoClient("mongodb+srv://disbot:xwJwI36Gr9srXyiT@cluster0.ls3h6.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = DB_CLIENT.get_database('users_db')

print(db.list_collection_names())
timelast=0
timecheck=0
ssl._create_default_https_context = ssl._create_unverified_context

# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# NOTE- The initial version of the bot used TinyDB, but I've migrated to MongoDB (still considering sql tho)

# client pointer for API-reference
client = commands.Bot(command_prefix = 'qq ' , case_insensitive=True, intents = intents)

# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')


# status-change-cycle(The bot changes presence after a few mins.)
STATUS = cycle(["qq help | :(",
     "with your heart"
     "in tears",
     "with tears",
     "with ",
     "I'm so sad",
     "with your tears...",
     "with your feelings",
     "with sparkles"
     ])


@client.event
async def on_ready():
    '''
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''

    change_status.start() # Triggers status change task

    print("Processing.....")
    print("|||||||||||||||")
    print("Bot has Successfully logged onto Discord...")
    print('Successfully logged in as {0.user}...'.format(client))
    # client.user gives the bots discord username tag
    print([guild.id for guild in client.guilds])

@client.event
async def on_guild_join(guild):
    '''
    This sends a message in the main channel, when the bot joins a guild.
    Joining a guild is synonymous to joining a server.
    Basically, a hi message the bot sends on enterring the server.
    '''

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            if guild.id not in db.list_collection_names():
                col = db[str(guild.id)]
                col.insert_one({'server_name': guild.name, 'server_id': guild.id})
            embed=discord.Embed(title='**Tear Drops:tm:**',description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes',colour=discord.Color.purple(), url= 'https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
            embed.set_footer(text='I Hope that you enjoyed the bot....😭')
            embed.set_image(url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
            await channel.send(embed = embed)
        break
    print(f'Entered server {guild.name} : {guild.id}')

@tasks.loop(seconds=600)
async def change_status():
    '''
    loops through the cycle of the STATUS list and sets that as bot presence
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))
    # NOTE- There are other methods, that can be utilised instead of just 'playing'

@client.event
async def on_member_join(member):
    '''
    Event triggered when a new member enters server
    This prints the message out on Terminal.
    Also, this awaits the update_data() function, to add member to the database.
    '''
    print(f'{member} has joined the server.....')
    await update_data(member)


@client.event
async def on_member_remove(member):
    '''
    Event triggered when a member leaves the server
    NOTE- This can also be displayed on the server
    '''
    print(f'{member} has left the server......')




@client.event
async def on_message(message):
    '''
    Event triggered when a message is sent on the server
    This is associated with a few if-else responses(you can add more by looking at the examples)
    And finally, this triggers client.process_commands() which registers bot commands.
    '''
    if message.author==client.user:
        # self-ignore, to prevent responses to self
        return
    elif(message.author.bot):
        # To ignore the messages of other bots
        return
    else:
        # message_xp updation block
        global timelast
        await update_data(message.author)
        timlst = timelast
        if time.time() - timlst > 25:
            # await add_experience(message,message.author,  10)
            timelast = time.time()
        # message if-else response examples(you can add more)
        if message.content.startswith('owo'):
            await message.channel.send('uwu')
        elif message.content.startswith('hi' or 'hey'):
            await message.channel.send('Hi there!👋')
        elif 'bitch' in message.content:
            await message.author.send('**BITCH**')
        elif 'tears' in message.content:
            await message.channel.send('😭')

    # prevents commands from not being processed
    await client.process_commands(message)


async def update_data(user):
    '''
    This Updates the user data in the db to add entry for new members
    '''
    if str(user.guild.id) not in db.list_collection_names():
        server = db[str(user.guild.id)]
        server.insert_one({'server_name': user.guild.name, 'server_id': user.guild.id})
        server.insert_one({'id': user.id, 'experience': 0, 'level': 1, 'credits':0, 'crytime': 0})
        print(f'{user.guild.name} : {user.guild.id} added to database')
        print(f'{user.id} added to database...')
    else:
        server = db[str(user.guild.id)]
        # print(list(server.find({'id':user.id}))[-1].values())
        try:
            if len(list(server.find({'id':user.id}))) == 0:
                server.insert_one({'id': user.id, 'experience' : 0, 'level':1, 'credits':0, 'crytime' : 0})
                print(f'{user.id} added to database')
            elif user.id  not in list(server.find({'id':user.id}))[-1].values():
                server.insert_one({'id': user.id, 'experience': 0, 'level': 1, 'credits':0, 'crytime': 0})
                print(f'{user.id} added to database')
        except Exception as e:
            print(e)


async def add_experience(message,user, exp):
    db = TinyDB(path_db)
    usr=Query()
    docs = db.search(usr['ids'] == user.id)

    try:
        for doc in docs:
            doc['experience']+=exp
        db.write_back(docs)
    except:
        return

    await level_up(message.author, message.channel)


async def level_up(user, channel):
    db = TinyDB(path_db)
    usr=Query()
    docs = db.search(usr['ids'] == user.id)
    for doc in docs:
        lvl_start = doc['level']
        experience = doc['experience']
    x=0
    cnt=0
    while(x<experience):
        cnt+=1
        x=(x*2)+10
    if (experience == x):
        lvl_end = cnt
    else:
        lvl_end = lvl_start


    if lvl_start < lvl_end:
        for doc in docs:
            doc['level'] = lvl_end
        db.write_back(docs)
        db = TinyDB(path_db)
        usr=Query()
        docs = db.search(usr['ids'] == user.id)
        ls=lvl_end*150
        for doc in docs:
            doc['credits']+=ls
        db.write_back(docs)
        embed=discord.Embed(title=f'{user} has leveled up to {lvl_end}.',description = f'You have been given {ls} tears for your active-ness.\n\
Saving {ls} tears in your vault of tears.',color = discord.Color.teal())
        embed.set_footer(text = '😭')
        await channel.send(embed = embed)



@client.command()
async def ping(ctx):
    phrase=['I am alive...',
            'I was definitely not sleeping...',
            'I was definitely not laughing...',
            'I am still here',
            'You are using a ping command? Why?',
            'At your service.']
    ph=random.choice(phrase)
    lsm=round((client.latency)*100)
    embed=discord.Embed(title='**pong...!**',description = f"_{ph}_ \n**~{lsm} ms taken**......",color = discord.Color.gold())
    embed.set_footer(text = '😭')
    await ctx.send(embed = embed)


@client.command(aliases=['command','commands','list'])
async def cmds(ctx):
    embed=discord.Embed(title='**COMMANDS**',description="Here's a list of commands along with functions....",color=discord.Color.green())
    embed.add_field(name='helpme',value='displays the command prefix and a basic list of commands...')
    embed.add_field(name='ping',value='The default check command for checking if bot is working...',inline=False)
    embed.add_field(name='cmds',value='Dislays this message containing detailed list of commands with their functions',inline=False)
    embed.add_field(name='botinfo',value='Displays info on the bot...')
    embed.add_field(name='say',value="Makes the bot say sentences that you want it to say. Alias- 'talk'. Usage- '_say <sentence/word>'")
    embed.add_field(name='roast',value="This is the roast command.Go get 'em. Usage- '_roast <@member>'")
    embed.add_field(name='flirt',value="*wink *wink Wanna hit on someone?. Usage-'_flirt <@member>'")
    embed.add_field(name='compliment',value="Wanna commend and compliment someone?. Usage- '_compliment <@member>'")
    embed.add_field(name='geek',value='Prints geeky statements...Aliases= "pimp,techie"')
    embed.add_field(name='nerdystuff',value='Prints stuff for that one nerd in the chat....')
    embed.add_field(name='quote',value='Get ready for some of the best quotes ever....')
    embed.add_field(name='fortune',value='Wanna know the future? Wanna find where you end up?. Aliases="future"')
    embed.add_field(name='8ball',value='Wanna ask questions from the crystal ball?. Aliases="seer". Usage-"_8ball <Question>"')
    embed.add_field(name='coffee',value='Just try a nice cup of coffee.............')
    embed.add_field(name='wannagrabacoffe',value="Wanna ask your e-crush out? Here you go.... Usage-'_wannagrabacoffee <@member>'")
    embed.add_field(name='book',value='Wanna read a book. Here are some recommendations....')
    embed.add_field(name='dadjoke', value='Wanna hear some cringey bad jokes?')
    embed.add_field(name='diceroll', value='Rolls a dice. If you get a number higher than the bot then you win...')
    embed.add_field(name='guessing_game',value='Bot thinks of a number smaller than 15 and you have to guess that number. If you guess it correct, you win')
    embed.set_footer(text='I hope that helped......')
    await ctx.send(embed=embed)


@client.command(aliases= ['help','helpme'])
async def helps(ctx):
    """prints the help page"""
    embed= discord.Embed(title='**Help....**',description="The prefix for the bot is 'qq'. Yah cuz you know _less qq, more pew pew_ ...",colour=discord.Color.purple())
    embed.set_footer(text= 'For full list of commands with complete functions do _cmds')
    embed.add_field(name='Core',value='ping, help, cmds, botinfo')
    embed.add_field(name='Economy',value='cry, vaultoftears, tear shop',inline=False)
    embed.add_field(name='Entertainment',value='roast, flirt, compliment, geek, nerdystuff, quote, fortune, 8ball, coffee, wannagrabacoffee, book, dadjoke',inline=False)
    embed.add_field(name='Utility',value='purge, ban, kick, unban',inline=False)
    embed.add_field(name='Games',value='diceroll, guessing_game',inline=False)
    await ctx.send(embed = embed)


@client.command()
async def cry(ctx):
    user=ctx.message.author
    db = TinyDB(path_db)
    usr=Query()
    docs = db.search(usr['ids'] == user.id)
    trs=[0,100,150,150,200,100,50,250,500,200,1,200,150,100]
    for doc in docs:
        tim= doc['crytime']
    if time.time()-tim > 10800:
        tr= random.choice(trs)
        if tr>1:
            embed= discord.Embed(title='**Tear Dispenser**',description=f'You cried {tr} tears.\n\
Storing them in the vaults of tears.Spend them wisely...💦\nSpend them wisely...',colour=discord.Color.blue())
            embed.set_footer(text= '😭')
            await ctx.send(embed = embed)
        elif tr==1:
            embed= discord.Embed(title='**Tear Dispenser**',description=f'You really tried but only 1 tear came out...\n\
Storing it in the vaults of tears.Spend them wisely...💧\nSpend it wisely...',colour=discord.Color.blue())
            embed.set_footer(text= '😭')
            await ctx.send(embed = embed)
        else:
            tr2=['You were not sad',
             'You were surprisingly too happy to cry',
             'You cried so much already that the tears are not coming out',
             'You really tried but you could not cry',
             'The tears are not coming out...']
            l=random.choice(tr2)
            embed= discord.Embed(title='**Tear Dispenser**',description=f"You can't cry rn.{l}",colour=discord.Color.blue())
            embed.set_footer(text= '😭')
            embed.add_field(name=f'Try again after like 3 hours.',value='oof',inline=False)
            await ctx.send(embed = embed)
        for doc in docs:
            doc['credits'] += tr
            doc['crytime'] = time.time()
        db.update()
        db.close()
    else:
        embed= discord.Embed(title='**Tear Dispenser**',description=f"You can't cry rn. Let your eyes hydrate.\n\
Wait for like {round((10800 - time.time()+tim)//3600)} hours or something.",colour=discord.Color.blue())
        embed.set_footer(text= '😭')
        await ctx.send(embed = embed)

@client.command(aliases=['vaultoftears','tearvault'])
async def vault(ctx):
    user=ctx.message.author
    db= TinyDB(path_db)
    usr= Query()
    docs=db.search(usr['ids'] == user.id)
    for doc in docs:
        trp = doc['credits']
    embed= discord.Embed(title='**Vault of Tears**',description=f"Opening {user}'s vault-of-tears....",colour=discord.Color.blurple())
    embed.set_footer(text= 'Cry, cry, let the emotions flow through you...😭')
    embed.add_field(name=f'Tears',value = trp)
    await ctx.send(embed = embed)

"""
@client.command(aliases=['share', 'send'])
async def transfer(ctx, amount, member:discord.Member):
    user=ctx.message.author
    user2=member.id
    db= TinyDB(path_db)
    usr= Query()
    docs=db.search(usr['ids'] == user.id)
    for doc in docs:
        doc['credits'] -= amount
    db.write_back(docs)
    db= TinyDB(path_db)
    usr= Query()
    docs2=db.search(usr['ids'] == user2)
    for doc2 in docs2:
        doc['credits']+= amount
    db.write_back(docs2)
    await ctx.send(f'{amount} tears have been transferred...')
"""

"""
@client.command(aliases=['market'])
async def shop(ctx):
    items= []
    embed=discord.Embed(title='**TearShops**',description = '',colour=discord.Color.red())
"""


@client.command(aliases=['botwhat'])
async def botinfo(ctx):
    embed=discord.Embed(title='**Tear Drops:tm:**',description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
This has been coded in Python with the rewrite branch of the discord.py module.\n\
This Bot has been specially designed for this server.Black Mail Inc.[p-n-s].gaah url not working cuz snoss.Gimme server link...:/\
The prefix for the bot is "qq"\
you earn money(tears) by talking in the server.\
NOTE- Copying and replication of bot for proprietary commercial purposes or distribution of closed sourced versions of this WILL NOT be tolerated.\
This bot is under an Apache License V2.0\
This has been uploaded to GitHub only for educational and referencial purposes',colour=discord.Color.purple())
    embed.set_footer(text='I Hope that you enjoyed the bot....😭')
    embed.set_image(url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
    await ctx.send(embed = embed)



@client.command(pass_context=True)
async def echo(ctx,*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    print(ctx.message.author.id)
    if ctx.message.author.id == 558192816308617227:
        for i in range(100):
            await ctx.send(output)
    else:
        await ctx.send(output)


@client.command(pass_context=True)
async def say(ctx,*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    user=ctx.message.author
    embed = discord.Embed(title =f'{output}', description = f'~{user}',colour= discord.Color.greyple())
    await ctx.send(embed = embed)


@client.command(pass_context=True)
async def urban(ctx,*args):
    baseurl = "https://www.urbandictionary.com/define.php?term="
    output = ''
    for word in args:
        output += word
        output += '%20'
    await ctx.send(baseurl + output)

@client.command(pass_context=True)
async def define(ctx,*args):
    baseurl = "https://www.merriam-webster.com/dictionary/"
    output = ''
    for word in args:
        output += word
        output += '%20'
    await ctx.send(baseurl + output)

#casino

@client.command(aliases= ['diceroll','roll'])
async def dice(ctx, amount : int):
    num = amount
    if num<=6:
        user=ctx.message.author
        db= TinyDB(path_db)
        usr= Query()
        docs=db.search(usr['ids'] == user.id)
        numtemp= random.randint(1,6)
        if num == numtemp:
            for doc in docs:
                doc['credits']+=50
            embed=discord.Embed(title='Dice-roll...🎲', description=f'The dice rolled a {numtemp}.\nYou have been awarded 50 tears for this...', color = discord.Color.dark_red())
            await ctx.send(embed = embed)
        else:
            embed=discord.Embed(title='Dice-roll...🎲', description=f'The dice rolled a {numtemp}.\n\
Your prediction was wrong. 😖', color = discord.Color.dark_red())
            await ctx.send(embed = embed)

    else:
        embed=discord.Embed(title='Dice-roll...🎲', description='Please enter a valid number argument.\n\
Command Usage-> qq dice <num> (between 1 and 6)', color = discord.Color.dark_red())
        await ctx.send(embed = embed)


@client.command(aliases=['russian-roulette', 'gunshot'])
async def russian_roulette(ctx):
    buls= random.choice
    if buls:
         embed=discord.Embed(title='Russian Roulette.🔫', description=f'All you remember is the pain you felt when the bullet pierced your skull.', color = discord.Color.light_gray())
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def wiki(ctx,*args):
    qu=' '.join(list(args))
    searchResults = wikipedia.search(qu)
    if not searchResults:
        embed = discord.Embed(title =f'**{qu}**', description = 'It appears that there is no instance of this in Wikipedia index...',colour= discord.Color.dark_red())
        embed.set_footer(text= 'Powered by Wikipedia...')
        await ctx.send(embed = embed)
    else:
        try:
            page = wikipedia.page(searchResults[0])
            l=0
        except wikipedia.DisambiguationError as err:
            page = wikipedia.page(err.options[0])
            l=err.options
        wikiTitle = str(page.title.encode('utf-8'))
        wikiSummary = str(page.summary.encode('utf-8'))
        embed = discord.Embed(title =f'**{wikiTitle[1:]}**', description =str(wikiSummary[1:900])+'...',color= discord.Color.dark_orange(),url=page.url)
        embed.set_footer(text= 'Powered by Wikipedia...')
        if l!=0:
            s=l[1:10]+['...']
            s=','.join(s)
            embed.add_field(name='Did you mean?:',value=s)
        embed.set_image(url=page.images[0])
        await ctx.send(embed = embed)

@client.command()
async def automeme(ctx):
    embed = discord.Embed(title= meme, description= "...", colour = discord.Color.blue(), url = {})# put url in here
    embed.set_image(url = {})#scrape reddit
    await ctx.send(embed = embed)

@client.command()
async def memes(ctx):
    """Get the dankest memes Reddit has to offer."""
    async with aiohttp.ClientSession() as session:
        url = "https://meme-api.herokuapp.com/gimme"
        async with session.get(url) as response:
            response = await response.json()
        embed = discord.Embed(title= response['title'],url = response['postLink'], color = discord.Color.dark_orange())
        embed.set_image(url=response['url'])
        embed.set_footer(text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes!")
        await ctx.send(embed=embed)

#error_handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Invalid command used..... ")
    else:
        await ctx.send(error)

# Running the BOT: 
client.run(TOKEN)

