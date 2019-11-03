import discord
from discord.ext import commands

from helpers.ge import GrandExchange
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
        description='Use to lookup items on the Grand Exchange',
        aliases=['-g', 'price'],
        case_insensitive=True)
    async def ge_command(self, ctx, *search_description):
        """ Responds with information about an item from the Grand Exchange """
        safe_name = ' '.join(search_description)
        ge = GrandExchange(safe_name)
        embed = discord.Embed(title=ge.name, description=ge.description)
        embed.set_thumbnail(url=ge.icon)
        embed.add_field(name='Price', value=f'**{ge.current_price}** gp')
        embed.add_field(name='Today\'s trend', value=f'**{ge.todays_price_change}** change today, trending {ge.todays_price_trend}')
        embed.set_footer(text=f'30d: {ge.day30_change}, 90d: {ge.day90_change}, 180d: {ge.day180_change}')
        # Graph
        ge.generate_graph()
        file = discord.File('assets/graph.png')
        embed.set_image(url='attachment://assets/graph.png')
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        # TODO make this respond with file only if attach_files permission is true
        await ctx.send(file=file)
        file.close()
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