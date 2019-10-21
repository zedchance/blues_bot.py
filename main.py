import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

from helpers.api_key import discord_key, owner_id
from helpers.descriptions import bot_description, version_number, wrong_message

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
    status = discord.Activity(name='for !b help', type=3)
    await bot.change_presence(activity=status)
    return

@bot.event
async def on_command_error(ctx, error):
    """ Simply replies with error message, shows error message if I make an error """
    msg = f'{wrong_message}\nTo see all commands type `!b help`\nUse `!b bug` if you continue to have issues\nOwner has been notified of error.'
    print(error)
    if ctx.author.id == owner_id:
        await ctx.send(f'```{error}```')
    else:
        await ctx.send(msg)
        admin = bot.get_user(owner_id)
        await admin.send(f'{ctx.guild}/{ctx.channel} - {ctx.author}:\n\"{ctx.message.content}\"\n```{error}```\n')
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
    description='Submits a bug report to the admin of the bot',
    aliases=['issue'],
    case_insensitive=True)
async def bug_command(ctx, *message):
    """ Use to submit bugs/issues """
    msg = ' '.join(message)
    if msg == '':
        await ctx.send(f'{ctx.message.author.mention} please enter a message after `!b bug`')
    else:
        admin = bot.get_user(owner_id)
        await ctx.send(f'{ctx.message.author.mention}\nYour bug has been filed\n\"{msg}\"\nIf you continue to have problems please report all issues and bugs here:\nhttps://github.com/zedchance/blues_bot.py/issues')
        await admin.send(f'Bug report from {ctx.author}\n\"{msg}\"')
    return

bot.run(discord_key, bot=True, reconnect=True)