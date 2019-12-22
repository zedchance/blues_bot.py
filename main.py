import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

from helpers.api_key import discord_key, owner_id
from helpers.descriptions import bot_description, version_number, wrong_message, user_not_found_message
from helpers.hiscore import UserNotFound, MissingUsername

def get_prefix(client, message):
    prefixes = ['!blue ', '!b ']
    if message.content.startswith("!b ") or message.content.startswith("!blue "):
        print(f'{message.channel} - {message.author}: {message.content}')
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(command_prefix=get_prefix,
        description=bot_description,
        owner_id=owner_id,
        case_insensitive=True)

bot.remove_command('help')
cogs = ['cogs.links', 'cogs.levels', 'cogs.calculators', 'cogs.scores', 'cogs.embed_help.help']

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
async def on_message(message):
    # Handles when the user doesn't type a command
    if message.content == '!b' or message.content == '!blue':
        channel = message.channel
        embed = discord.Embed(title='!blue', description='Type `!b help` for a list of commands.')
        await channel.send(embed=embed)
        return
    # Pass message onto the rest of the commands
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    """ Simply replies with error message, shows error message if I make an error """
    print(error)
    msg = f'{wrong_message}'
    error = getattr(error, 'original', error)
    # Exceptions
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        msg += f'{error}\nType `!b help` for a list of commands'
    elif isinstance(error, UserNotFound):
        msg += f'{error}'
    elif isinstance(error, MissingUsername):
        msg += f'{error}'
    # All other errors
    else:
        msg += f'To see all commands type `!b help`\nUse `!b bug` if you continue to have issues\nOwner has been notified of error.'
    # If its me that makes the error, show the message
    if ctx.author.id == owner_id:
        await ctx.send(f'```{error}```')
    # Otherwise reply with error message and PM me details
    else:
        await ctx.send(msg)
        admin = bot.get_user(owner_id)
        embed = discord.Embed()
        embed.add_field(name="Location", value=f'{ctx.guild}/{ctx.channel.mention} - {ctx.author}')
        embed.add_field(name="User input", value=f'{ctx.message.content}', inline=False)
        embed.add_field(name="Error message", value=f'```{error}```', inline=False)
        await admin.send(embed=embed)
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
    embed = discord.Embed(title="!blue", description="Old School Runescape bot written in Python")
    embed.add_field(name="Version Number", value=f'*{version_number}*')
    embed.add_field(name="Recent changes", value=f'https://github.com/zedchance/blues_bot.py/commits/master')
    await ctx.send(f'{ctx.message.author.mention}', embed=embed)
    return
    
@bot.command(name='bug',
    description='Links to the issue page for the bot',
    aliases=['issue'],
    hidden=True,
    case_insensitive=True)
async def bug_command(ctx):
    """ Use to submit bugs/issues """
    embed = discord.Embed(title="Bugs/issues", description="Use the following link to submit issues with the bot")
    embed.add_field(name="Link", value=f'https://github.com/zedchance/blues_bot.py/issues')
    await ctx.send(f'{ctx.message.author.mention}', embed=embed)
    return

bot.run(discord_key, bot=True, reconnect=True)