# Periodically performed tasks

import logging
import discord
from discord.ext import commands, tasks


class Refresh(commands.Cog):
    """ Tasks to be periodically performed """

    def __init__(self, bot):
        self.bot = bot
        self.refresh_presence.start()

    @tasks.loop(minutes=30.0)
    async def refresh_presence(self):
        """ Refreshes the presence of the bot """
        logging.info("Refreshing bot's presence")
        status = discord.Activity(name=f'for !b in {str(len(self.bot.guilds))} servers', type=3)
        return await self.bot.change_presence(activity=status)


# Cog setup
def setup(bot):
    bot.add_cog(Refresh(bot))
