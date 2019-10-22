import discord
from discord.ext import commands

from helpers.descriptions import version_number
from helpers.urls import hiscore_url, wiki_url, ge_url, rsbuddy_url, cml_url, cml_sig
from helpers.tracker import Tracker

class Links(commands.Cog):
    """ Link commands to return URLs of common stuff """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hiscore',
        description='Returns a URL to a player\'s hiscore page',
        aliases=['hiscores', '-h'],
        case_insensitive=True)
    async def ping_command(self, ctx, *username):
        """ Links to hiscore page for a user """
        url_safe = '+'.join(username)
        await ctx.send(f'{ctx.message.author.mention}\n{hiscore_url}{url_safe}')
        return
    
    @commands.command(name='wiki',
        description='Returns a URL to a wiki page',
        aliases=['-w'],
        case_insensitive=True)
    async def wiki_command(self, ctx, *search_description):
        """ Links to wiki page for a search """
        url_safe = '+'.join(search_description)
        await ctx.send(f'{ctx.message.author.mention}\n{wiki_url}{url_safe}')
        return
    
    @commands.command(name='ge',
        description='Returns a URL to the official Grand Exchange page for an item',
        aliases=['-g'],
        case_insensitive=True)
    async def ge_command(self, ctx, *search_description):
        """ Links to the Grand Exchange website for a search """
        url_safe = '+'.join(search_description)
        await ctx.send(f'{ctx.message.author.mention}\n{ge_url}{url_safe}')
        return
    
    @commands.command(name='rsbuddy',
        description='Returns a URL to the RSBuddy page for an item',
        aliases=['-rsb'],
        case_insensitive=True)
    async def rsbuddy_command(self, ctx, *search_description):
        """ Links to the RSBuddy page of a search """
        url_safe = '+'.join(search_description)
        await ctx.send(f'{ctx.message.author.mention}\n{rsbuddy_url}{url_safe}')
        return
    
    @commands.command(name='sig',
        description='Updates your xp tracker page and shows signature',
        aliases=['cml', 'tracker'],
        case_insensitive=True)
    async def cml_command(self, ctx, *username):
        """ Crystal Math Labs xp tracker signature """
        async with ctx.typing():
            url_safe = '+'.join(username)
            user = Tracker(url_safe)
            imageURL = cml_sig + url_safe
            embed = discord.Embed()
            embed.set_image(url=imageURL)
            await ctx.send(f'{ctx.message.author.mention}\n{cml_url}{url_safe}', embed=embed)

# Cog setup
def setup(bot):
    bot.add_cog(Links(bot))