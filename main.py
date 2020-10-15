import logging
import discord
import pytz
from discord.ext import commands, tasks
from datetime import datetime

from helpers.api_key import discord_key, owner_id, error_channel_id
from helpers.descriptions import bot_description, wrong_message
from helpers.ge import MissingQuery, NoResults
from helpers.hiscore import UserNotFound, MissingUsername, HiscoreUnavailable
from helpers.tracker import NoDataPoints, NoUsername
from helpers.version import get_version

logging.basicConfig(filename='bot.log',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.INFO)


def get_prefix(client, message):
    prefixes = ['!blue ', '!b ']
    if message.content.startswith("!b ") or message.content.startswith("!blue "):
        logging.info(f'[{message.guild}/{message.channel}] {message.author}: {message.content}')
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(command_prefix=get_prefix,
                   description=bot_description,
                   owner_id=owner_id,
                   case_insensitive=True)

bot.remove_command('help')
cogs = ['cogs.links', 'cogs.levels', 'cogs.calculators', 'cogs.scores', 'cogs.embed_help.help',
        'cogs.refresh']


@bot.event
async def on_ready():
    logging.info(f'Logged on as {bot.user.name}!')
    for cog in cogs:
        logging.info(f'Loading {cog}')
        bot.load_extension(cog)
    logging.info("Cogs loaded")
    print(f'Up and running as {bot.user.name}')
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
    logging.error(f'{type(error).__name__}: {error}')
    error = getattr(error, 'original', error)
    msg = ''
    # Exceptions
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass
    elif isinstance(error, UserNotFound) or isinstance(error, NoDataPoints) or isinstance(error, NoResults)\
            or isinstance(error, HiscoreUnavailable) or isinstance(error, NoUsername):
        msg += f'{error}\n'
    elif isinstance(error, MissingUsername) or isinstance(error, MissingQuery):
        msg += f'{error}\n' \
               f'Type `!b help {ctx.command}` to see the usage for the command.\n'
    elif isinstance(error, commands.MissingRequiredArgument):
        msg += f'Not all of the command\'s arguments were met.\n' \
               f'You are missing the `{error.param}` argument.\n' \
               f'Type `!b help {ctx.command}` to see the usage for the command.\n'
    # All other errors
    else:
        msg += f'To see all commands type `!b help`\n' \
               f'Owner has been notified of error. '
    # Reply with error message
    if msg != '':
        embed = discord.Embed(title=f'{bot.user.name}')
        embed.add_field(name="Something went wrong", value=msg)
        embed.add_field(name="If you continue to have problems",
                        value=f'Type `!b bug` to be linked to the issues page',
                        inline=False)
        await ctx.send(embed=embed)
    # Log the error in the errors channel
    error_channel = bot.get_channel(error_channel_id)
    time = datetime.now()
    timezone = pytz.timezone("America/Los_Angeles")
    pst_time = timezone.localize(time)
    embed = discord.Embed(title=f'{bot.user.name}', timestamp=pst_time)
    embed.add_field(name="Location", value=f'{ctx.guild}/{ctx.channel.mention} - {ctx.author}')
    embed.add_field(name="User input", value=f'`{ctx.message.content}`', inline=False)
    embed.add_field(name="Error message", value=f'```{type(error).__name__}: {error}```', inline=False)
    embed.add_field(name="Cause (if any)", value=f'{error.__cause__}', inline=False)
    await error_channel.send(embed=embed)
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
        logging.info(f'Reloading {cog}')
        bot.load_extension(cog)
    await ctx.send("Cogs reloaded")


@bot.command(name='version',
             description='Bot version',
             aliases=['--version', '-v'],
             hidden=True,
             case_insensitive=True)
async def version_command(ctx):
    """ Shows bot version number """
    version = get_version()
    embed = discord.Embed(title="!blue", description="Old School Runescape bot written in Python")
    embed.add_field(name="Version Number", value=version)
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


@bot.command(name='vote',
             description='Upvote/invite the bot on top.gg',
             aliases=['invite'],
             hidden=True,
             case_insensitive=True)
async def vote_command(ctx):
    """ Links to the bot's top.gg page """
    embed = discord.Embed(title="**!blue**", description="Vote for the bot or invite to your own channel!")
    embed.add_field(name="Link", value=f'https://top.gg/bot/532782540897910784')
    await ctx.send(f'{ctx.message.author.mention}', embed=embed)
    return


bot.run(discord_key, bot=True, reconnect=True)
