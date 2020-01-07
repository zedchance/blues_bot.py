from discord.ext import commands

from helpers.descriptions import version_number


class Basic(commands.Cog):
    """ Basic commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='version',
                      description='Bot version',
                      aliases=['--version', '-v'],
                      case_insensitive=True)
    async def version_command(self, ctx):
        """ Shows bot version number """
        await ctx.send(
            f'{ctx.message.author.mention}\n**!blue** *version {version_number}*\nRecent changes here:\nhttps://github.com/zedchance/blues_bot.py/commits/master')
        return

    @commands.command(name='bug',
                      description='Provides a link to the bug/issue page',
                      aliases=['issue'],
                      case_insensitive=True)
    async def bug_command(self, ctx, *message):
        """ Links to bug/issue page """
        msg = ' '.join(message)
        await ctx.send(
            f'{ctx.message.author.mention}\nPlease report all issues and bugs here:\nhttps://github.com/zedchance/blues_bot.py/issues')
        return


# Cog setup
def setup(bot):
    bot.add_cog(Basic(bot))
