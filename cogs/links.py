from descriptions import version_number
from urls import hiscore_url, wiki_url, ge_url, rsbuddy_url

from discord.ext import commands

class Links(commands.Cog):
    """ Link commands to return URLs of common stuff """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hiscore',
        description='Returns a URL to a player\'s hiscore page',
        aliases=['hiscores', '-h'],
        case_insensitive=True)
    async def ping_command(self, ctx, username):
        await ctx.send(f'{hiscore_url}{username}')
        return
    
    @commands.command(name='wiki',
        description='Returns a URL to a wiki page',
        aliases=['-w'],
        case_insensitive=True)
    async def wiki_command(self, ctx, *search_description):
        url_safe = '+'.join(search_description)
        await ctx.send(f'{wiki_url}{url_safe}')
        return
    
    @commands.command(name='ge',
        description='Returns a URL to the official Grand Exchange page for an item',
        aliases=['-g'],
        case_insensitive=True)
    async def ge_command(self, ctx, *search_description):
        url_safe = '+'.join(search_description)
        await ctx.send(f'{ge_url}{url_safe}')
        return
    
    @commands.command(name='rsbuddy',
        description='Returns a URL to the RSBuddy page for an item',
        aliases=['-rsb'],
        case_insensitive=True)
    async def rsbuddy_command(self, ctx, *search_description):
        url_safe = '+'.join(search_description)
        await ctx.send(f'{rsbuddy_url}{url_safe}')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Links(bot))