from discord.ext import commands

from descriptions import version_number

class Basic(commands.Cog):
    """ Basic commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='version',
        description='Bot version',
        aliases=['--version', '-v'],
        case_insensitive=True)
    async def ping_command(self, ctx):
        await ctx.send(f'**!blue** *version {version_number}*')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Basic(bot))