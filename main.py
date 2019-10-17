from api_key import discord_key, owner_id

import discord
from discord.ext import commands

def get_prefix(client, message):
    prefixes = ['!blue ', '!b ']
    print("{0.author}: {0.content}".format(message))
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(command_prefix=get_prefix,
        description='!blue OSRS bot',
        owner_id=owner_id,
        case_insensitive=True)

cogs = ['cogs.basic']

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user.name}!")
    for cog in cogs:
        bot.load_extension(cog)
    return

bot.run(discord_key, bot=True, reconnect=True)