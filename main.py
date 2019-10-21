import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

from helpers.api_key import discord_key, owner_id
from helpers.descriptions import bot_description, version_number

def get_prefix(client, message):
    prefixes = ['!blue ', '!b ']
    if message.content.startswith("!b ") or message.content.startswith("!blue "):
        print(f'{message.channel} - {message.author}: {message.content}')
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(command_prefix=get_prefix,
        description=bot_description,
        owner_id=owner_id,
        case_insensitive=True)

cogs = ['cogs.links', 'cogs.levels', 'cogs.calculators', 'cogs.scores']

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user.name}!")
    for cog in cogs:
        print("Loading", cog)
        bot.load_extension(cog)
    print("Cogs loaded")
    status = discord.Game(name='!b help to show commands')
    await bot.change_presence(activity=status)
    return

@bot.event
async def on_command_error(ctx, error):
    """ Simply replies with error message, shows error message if I make an error """
    msg = f'Something went wrong.\nUse `!b bug` to report issues'
    print(error)
    if ctx.author.id == owner_id:
        await ctx.send(f'{error}')
    else:
        await ctx.send(f'{msg}\nPinging <@{owner_id}>')
    return

@bot.command(name='reload',
    description='Reloads bot',
    aliases=['-r'],
    hidden=True,
    case_insensitive=True)
async def reload(ctx):
    """ Reloads cogs while bot is still online """
    if ctx.author.id != owner_id:
        return
    for cog in cogs:
        bot.unload_extension(cog)
    for cog in cogs:
        print("Reloading", cog)
        bot.load_extension(cog)
    await ctx.send("Cogs reloaded")

@bot.command(name='version',
    description='Bot version',
    aliases=['--version', '-v'],
    hidden=True,
    case_insensitive=True)
async def version_command(ctx):
    """ Shows bot version number """
    await ctx.send(f'{ctx.message.author.mention}\n**!blue** *version {version_number}*\nRecent changes here:\nhttps://github.com/zedchance/blues_bot.py/commits/master')
    return
    
@bot.command(name='bug',
    description='Provides a link to the bug/issue page',
    aliases=['issue'],
    case_insensitive=True)
async def bug_command(ctx, *message):
    """ Links to bug/issue page """
    msg = ' '.join(message)
    await ctx.send(f'{ctx.message.author.mention}\nPlease report all issues and bugs here:\nhttps://github.com/zedchance/blues_bot.py/issues')
    return

bot.run(discord_key, bot=True, reconnect=True)