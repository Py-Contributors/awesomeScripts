# TODO - transfer, casino, etc commands

import ssl
import discord
from discord.ext import commands, tasks
from itertools import cycle

from pymongo import MongoClient


# modules for database
from setup import TOKEN, USER_NAME, MONGODB_PASS

# modules for wiki and wolfram queries
# import wolframalpha
import wikipedia
# import requests

# Standard modules
import random
import time
import aiohttp

# mongoDB Client
link = "ls3h6.mongodb.net/<dbname>?retryWrites=true&w=majority"
DB_CLIENT = MongoClient(f"mongodb+srv://{USER_NAME}:{MONGODB_PASS}@cluster0.{link}")
db = DB_CLIENT.get_database('users_db')

print(db.list_collection_names())
timelast = 0
timecheck = 0
buls = 0
ssl._create_default_https_context = ssl._create_unverified_context

# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# NOTE- The initial version of the bot used TinyDB, but I've migrated to MongoDB (still considering sql tho)

# client pointer for API-reference
client = commands.Bot(command_prefix='qq ', case_insensitive=True, intents=intents)

# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')


# status-change-cycle(The bot changes presence after a few mins.)
STATUS = cycle([
    "qq help | :(",
    "with your heart"
    "in tears",
    "with tears",
    "with ",
    "I'm so sad",
    "with your tears...",
    "with your feelings",
    "with sparkles"])


@client.event
async def on_ready():
    '''
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''

    change_status.start()  # Triggers status change task

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
        git_link = 'https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/'
        bot_icon = 'https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png'
        if channel.permissions_for(guild.me).send_messages:
            if guild.id not in db.list_collection_names():
                col = db[str(guild.id)]
                col.insert_one({'server_name': guild.name, 'server_id': guild.id})
            embed = discord.Embed(
                title='**Tear Drops:tm:**',
                description='A dynamic bot for _crying_, entertainment,\
economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license,\
I request you to not start a commercial bot with the same name "Tear Drops"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub\
for educational and referencial purposes',
                colour=discord.Color.purple(),
                url=git_link)
            embed.set_footer(text='I Hope that you enjoyed the bot....😭')
            embed.set_image(url=bot_icon)
            await channel.send(embed=embed)
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
    if message.author == client.user:
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
            await add_experience(message, message.author, 10)
            timelast = time.time()
        # message if-else response examples(you can add more)
        if message.content.startswith('owo'):
            await message.channel.send('uwu')
        elif message.content.startswith('hi' or 'hey'):
            await message.channel.send('Hi there!👋')
        elif 'bitch' in message.content:
            await message.author.send('**BIRCH**')  # dms
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
        server.insert_one({'id': user.id, 'experience': 0, 'level': 1, 'credits': 0, 'crytime': 0})
        print(f'{user.guild.name} : {user.guild.id} added to database')
        print(f'{user.id} added to database...')
    else:
        server = db[str(user.guild.id)]
        # print(list(server.find({'id':user.id}))[-1].values())
        try:
            if len(list(server.find({'id': user.id}))) == 0:
                server.insert_one({'id': user.id, 'experience': 0, 'level': 1, 'credits': 0, 'crytime': 0})
                print(f'{user.id} added to database')
            elif user.id not in list(server.find({'id': user.id}))[-1].values():
                server.insert_one({'id': user.id, 'experience': 0, 'level': 1, 'credits': 0, 'crytime': 0})
                print(f'{user.id} added to database')
        except Exception as e:
            print(e)


async def add_experience(message, user, exp):
    """Adds xp to the user in the database, and calls the level up function"""
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    exp = stats[-1]['experience'] + exp
    new_stats = {"$set": {'experience': exp}}
    server.update_one(stats[-1], new_stats)
    print(f'Added xp {exp} to {user.id} in {user.guild.name}')
    await level_up(message.author, message.channel)


async def level_up(user, channel):
    """Takes care of checking the level-up parameters to boot ppl to next level when sufficient xp obtained"""
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    lvl_start = stats[-1]['level']
    print(lvl_start)
    experience = stats[-1]['experience']
    x = 35
    cnt = 1
    while (x < experience):
        x = 2 * x + 10
        cnt += 1

    if experience >= x:
        lvl_end = cnt - 1
    else:
        lvl_end = lvl_start
    print(lvl_end)

    if lvl_start < lvl_end:
        new_stats = {"$set": {'level': lvl_end}}
        server.update_one(stats[-1], new_stats)
        ls = lvl_end * 150
        server = db[str(user.guild.id)]
        stats = list(server.find({'id': user.id}))
        cred = stats[-1]['credits'] + ls
        new_stats = {"$set": {'credits': cred}}
        server.update_one(stats[-1], new_stats)
        embed = discord.Embed(title=f'{user} has leveled up to {lvl_end}.', description=f'You have been given\
{ls} tears for your active-ness.\n\
Saving {ls} tears in your vault of tears.', color=discord.Color.teal())
        embed.set_footer(text='😭')
        await channel.send(embed=embed)


@client.command()
async def ping(ctx):
    """The bots ping command"""
    phrase = ['I am alive...',
              'I was definitely not sleeping...',
              'I was definitely not laughing...',
              'I am still here',
              'You are using a ping command? Why?',
              'At your service.']
    ph = random.choice(phrase)
    lsm = round((client.latency) * 100)
    embed = discord.Embed(title='**pong...!**',
                          description=f"_{ph}_ \n**~{lsm} ms taken**......",
                          color=discord.Color.gold())
    embed.set_footer(text='😭')
    await ctx.send(embed=embed)


@client.command(aliases=['command', 'commands', 'list'])
async def cmds(ctx):
    """
    lists all the commands in the bot
    NOTE- To be edited
    """
    text = "Here's a list of commands along with functions...."
    embed = discord.Embed(title='**COMMANDS**', description=text, color=discord.Color.green())
    embed.add_field(name='helpme',
                    value='displays the command prefix and a basic list of commands...')
    embed.add_field(name='ping',
                    value='The ping command for pinging...', inline=False)
    embed.add_field(name='cmds',
                    value='Dislays this message', inline=False)
    embed.add_field(name='botinfo',
                    value='Displays info on the bot...')
    embed.add_field(name='say',
                    value="Makes the bot say stuff. Usage- '_say <sentence/word>'")
    embed.add_field(name='roast',
                    value="This is the roast command.Go get 'em. Usage- '_roast <@member>'")
    embed.add_field(name='flirt',
                    value="*wink *wink Wanna hit on someone?. Usage-'_flirt <@member>'")
    embed.add_field(name='compliment',
                    value="Wanna commend and compliment someone?. Usage- '_compliment <@member>'")
    embed.add_field(name='geek',
                    value='Prints geeky statements...Aliases= "pimp,techie"')
    embed.add_field(name='nerdystuff',
                    value='Prints stuff for that one nerd in the chat....')
    embed.add_field(name='quote',
                    value='Get ready for some of the best quotes ever....')
    embed.add_field(name='fortune',
                    value='Wanna know the future? Aliases="future"')
    embed.add_field(name='8ball',
                    value='Wanna ask questions from the crystal ball?. Aliases="seer". Usage-"_8ball <Question>"')
    embed.add_field(name='coffee',
                    value='Just try a nice cup of coffee....')
    embed.add_field(name='wannagrabacoffe',
                    value="Wanna ask your e-crush out? Here you go.... Usage-'_wannagrabacoffee <@member>'")
    embed.add_field(name='book',
                    value='Wanna read a book. Here are some recommendations....')
    embed.add_field(name='dadjoke',
                    value='Wanna hear some cringey bad jokes?')
    embed.add_field(name='diceroll',
                    value='Rolls a dice. If you get a number higher than the bot then you win...')
    embed.add_field(name='guessing_game',
                    value='Bot thinks of a number smaller than 15 and you have to guess that number.\
If you guess it correct, you win')
    embed.set_footer(text='I hope that helped......')
    await ctx.send(embed=embed)


@client.command(aliases=['help', 'helpme'])
async def helps(ctx):
    """
    prints the help page
    NOTE- To be edited.
    """
    embed = discord.Embed(title='**Help....**', description="The prefix for the bot is 'qq'.\
Yah cuz you know _less qq, more pew pew_ ...", colour=discord.Color.purple())
    embed.set_footer(text='For full list of commands with complete functions do _cmds')
    embed.add_field(name='Core', value='ping, help, cmds, botinfo')
    embed.add_field(name='Economy', value='cry, vaultoftears, tear shop', inline=False)
    embed.add_field(name='Entertainment', value='roast, flirt, compliment, geek, nerdystuff, quote, fortune,\
8ball, coffee, wannagrabacoffee, book, dadjoke', inline=False)
    embed.add_field(name='Utility', value='purge, ban, kick, unban', inline=False)
    embed.add_field(name='Games', value='diceroll, guessing_game', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def cry(ctx):
    '''credit gain command for crying'''
    user = ctx.message.author
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    trs = [0, 100, 150, 150, 200, 100, 50, 250, 500, 200, 1, 200, 150, 100]
    tim = stats[-1]['crytime']
    if time.time() - tim > 10800:
        tr = random.choice(trs)
        if tr > 1:
            embed = discord.Embed(title='**Tear Dispenser**',
                                  description=f'You cried {tr} tears.\n\
Storing them in the vaults of tears.Spend them wisely...💦\nSpend them wisely...',
                                  color=discord.Color.blue())
            embed.set_footer(text='😭')
            await ctx.send(embed=embed)
        elif tr == 1:
            embed = discord.Embed(title='**Tear Dispenser**',
                                  description='You really tried but only 1 tear came out...\n\
Storing it in the vaults of tears.Spend them wisely...💧\nSpend it wisely...',
                                  color=discord.Color.blue())
            embed.set_footer(text='😭')
            await ctx.send(embed=embed)
        else:
            tr2 = [
                'You were not sad',
                'You were surprisingly too happy to cry',
                'You cried so much already that the tears are not coming out',
                'You really tried but you could not cry',
                'The tears are not coming out...']
            message = random.choice(tr2)
            embed = discord.Embed(title='**Tear Dispenser**',
                                  description=f"You can't cry rn.{message}",
                                  color=discord.Color.blue())
            embed.set_footer(text='😭')
            embed.add_field(name='Try again after like 3 hours.', value='oof', inline=False)
            await ctx.send(embed=embed)
        cred = tr + stats[-1]['credits']
        new_stats = {"$set": {'credits': cred, 'crytime': time.time()}}
        server.update_one(stats[-1], new_stats)
    else:
        embed = discord.Embed(title='**Tear Dispenser**', description=f"You can't cry rn. Let your eyes hydrate.\n\
Wait for like {round((10800 - time.time()+tim)//3600)} hours or something.", color=discord.Color.blue())
        embed.set_footer(text='😭')
        await ctx.send(embed=embed)


@client.command(aliases=['vaultoftears', 'tearvault'])
async def vault(ctx):
    '''Gives the users economy balance'''
    user = ctx.message.author
    server = db[str(user.guild.id)]
    stats = server.find({'id': user.id})
    trp = list(stats)[-1]['credits']
    embed = discord.Embed(
        title='**Vault of Tears**',
        description=f"Opening {user}'s vault-of-tears....",
        colour=discord.Color.blurple())
    embed.set_footer(text='Cry, cry, let the emotions flow through you...😭')
    embed.add_field(name='Tears', value=trp)
    await ctx.send(embed=embed)


@client.command()
async def level(ctx):
    '''Gives the users level'''
    user = ctx.message.author
    server = db[str(user.guild.id)]
    stats = server.find({'id': user.id})
    lvl = list(stats)[-1]['level']
    embed = discord.Embed(title='**Depression-Level**',
                          description="._.",
                          colour=discord.Color.blurple())
    embed.set_footer(text='Cry, cry, let the emotions flow through you...😭')
    embed.add_field(name='Level', value=lvl)
    await ctx.send(embed=embed)


"""
@client.command(aliases=['share', 'send'])
async def transfer(ctx, amount, member:discord.Member):
    '''transfer command'''
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
    '''market command'''
    items= []
    embed=discord.Embed(title='**TearShops**',description = '',colour=discord.Color.red())
"""


@client.command(aliases=['botwhat'])
async def botinfo(ctx):
    icon = 'https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png'
    git_url = 'https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/'
    '''Gives info about the bot'''
    embed = discord.Embed(title='**Tear Drops:tm:**',
                          description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression.\
Come let\'s cry together 😢\
The prefix for the bot is _"qq"_,\
cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_\
(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license,\
 I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes',
                          colour=discord.Color.purple(), url=git_url)
    embed.set_image(url=icon)
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def echo(ctx, *args):
    '''echos the words'''
    output = ''
    for word in args:
        output += word
        output += ' '
    print(ctx.message.author.id)
    if ctx.message.author.id == 558192816308617227:
        for i in range(3):
            await ctx.send(output)
    else:
        await ctx.send(output)


@client.command(pass_context=True)
async def say(ctx, *args):
    """Gives the user's statement a nice richtext quote format"""
    output = ''
    for word in args:
        output += word
        output += ' '
    user = ctx.message.author
    embed = discord.Embed(title=f'{output}',
                          description=f'~{user}',
                          colour=discord.Color.greyple())
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def urban(ctx, *args):
    '''searches urban dictionary for words'''
    baseurl = "https://www.urbandictionary.com/define.php?term="
    output = ''
    for word in args:
        output += word
        output += '%20'
    await ctx.send(baseurl + output)


@client.command(pass_context=True)
async def define(ctx, *args):
    '''searches merriam-webster for meanings of words'''
    baseurl = "https://www.merriam-webster.com/dictionary/"
    output = ''
    for word in args:
        output += word
        output += '%20'
    await ctx.send(baseurl + output)

# casino


@client.command(aliases=['diceroll', 'roll'])
async def dice(ctx, amount: int):
    '''dice-guess game'''
    num = amount
    if num <= 6:
        user = ctx.message.author
        server = db[str(user.guild.id)]
        stats = list(server.find({'id': user.id}))
        cred = stats[-1]['credits']
        numtemp = random.randint(1, 6)
        if num == numtemp:
            cred += 50
            newstats = {"$set": {'credits': cred}}
            server.update_one(stats[-1], newstats)
            embed = discord.Embed(title='Dice-roll...🎲',
                                  description=f'The dice rolled a {numtemp}.\n\
You have been awarded 50 tears for this...',
                                  color=discord.Color.dark_red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Dice-roll...🎲',
                                  description=f'The dice rolled a {numtemp}.\n\
Your prediction was wrong. 😖',
                                  color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title='Dice-roll...🎲',
                              description='Please enter a valid number argument.\n\
Command Usage-> qq dice <num> (between 1 and 6)',
                              color=discord.Color.dark_red())
        await ctx.send(embed=embed)


@client.command(aliases=['russian-roulette', 'gunshot'])
async def russian_roulette(ctx):
    '''starts fun russian roulette game'''
    global buls
    if buls >= 6:
        buls = 0
        embed = discord.Embed(title='Russian Roulette.🔫',
                              description='All you remember is the pain you felt when the bullet pierced your skull.',
                              color=discord.Color.light_gray())
    else:
        buls += 1
        embed = discord.Embed(
            title='Russian Roulette.🔫',
            description='You live to fight another day',
            color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def wiki(ctx, *args):
    '''Displays wikipedia info about given arguments'''
    qu = ' '.join(list(args))
    searchResults = wikipedia.search(qu)
    if not searchResults:
        embed = discord.Embed(title=f'**{qu}**',
                              description='It appears that there is no instance of this in Wikipedia index...',
                              colour=discord.Color.dark_red())
        embed.set_footer(text='Powered by Wikipedia...')
        await ctx.send(embed=embed)
    else:
        try:
            page = wikipedia.page(searchResults[0])
            pg = 0
        except wikipedia.DisambiguationError as err:
            page = wikipedia.page(err.options[0])
            pg = err.options
        wikiTitle = str(page.title.encode('utf-8'))
        wikiSummary = str(page.summary.encode('utf-8'))
        embed = discord.Embed(title=f'**{wikiTitle[1:]}**',
                              description=str(wikiSummary[1:900]) + '...',
                              color=discord.Color.dark_orange(),
                              url=page.url)
        embed.set_footer(text='Powered by Wikipedia...')
        if pg != 0:
            s = pg[1:10] + ['...']
            s = ','.join(s)
            embed.add_field(name='Did you mean?:', value=s)
        embed.set_image(url=page.images[0])
        await ctx.send(embed=embed)


@client.command(aliases=['meme'])
async def memes(ctx):
    """Get the dankest memes Reddit has to offer."""
    async with aiohttp.ClientSession() as session:
        url = "https://meme-api.herokuapp.com/gimme"
        async with session.get(url) as response:
            response = await response.json()
        embed = discord.Embed(title=response['title'],
                              url=response['postLink'],
                              color=discord.Color.dark_orange())
        embed.set_image(url=response['url'])
        embed.set_footer(text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes!")
        await ctx.send(embed=embed)

# error_handling


@client.event
async def on_command_error(ctx, error):
    # TODO- Error Handling
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used..... ")
    else:
        await ctx.send(error)

# Running the BOT:
client.run(TOKEN)
