import discord
from discord.ext import commands

from helpers.api_key import discord_key, owner_id
from helpers.descriptions import bot_description

def get_prefix(client, message):
    prefixes = ['!blue ', '!b ']
    if message.content.startswith("!b ") or message.content.startswith("!blue "):
        print("{0.author}: {0.content}".format(message))
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(command_prefix=get_prefix,
        description=bot_description,
        owner_id=owner_id,
        case_insensitive=True)

cogs = ['cogs.basic', 'cogs.links', 'cogs.levels', 'cogs.calculators', 'cogs.scores']

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user.name}!")
    for cog in cogs:
        print("Loading", cog)
        bot.load_extension(cog)
    print("Cogs loaded")
    return

# @bot.event
# async def on_command_error(ctx, error):


bot.run(discord_key, bot=True, reconnect=True)