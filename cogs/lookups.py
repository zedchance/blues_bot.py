import hiscore

from discord.ext import commands

class Lookups(commands.Cog):
    """ Lookup commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='level',
        description='Pulls a stat for a specific level',
        aliases=['lvl', 'levels', '-l'],
        case_insensitive=True)
    async def level_lookup(self, ctx, level, username):
        
        await ctx.send(f'')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Lookups(bot))