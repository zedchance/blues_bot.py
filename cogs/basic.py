from discord.ext import commands

class Basic(commands.Cog):
    """ Basic commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='version',
        description='Bot version',
        aliases=['--version', '-v'],
        case_insensitive=True)
    async def ping_command(self, ctx):
        version_number = "0.3 (20191017)"
        await ctx.send(f'**!blue** *version {version_number}*')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Basic(bot))