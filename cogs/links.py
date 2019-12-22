from datetime import datetime
import pytz
import discord
from discord.ext import commands
from discord.permissions import Permissions

from helpers.ge import GrandExchange
from helpers.urls import hiscore_url, wiki_url, ge_url, rsbuddy_url, cml_url, cml_sig, members_icon
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

    @commands.command(name='price',
        description='Use to lookup items on the Grand Exchange',
        aliases=['-g', 'ge'],
        case_insensitive=True)
    async def ge_command(self, ctx, *search_description):
        """ Responds with information about an item from the Grand Exchange """
        safe_name = ' '.join(search_description)
        url_safe_name = '+'.join(search_description)
        ge = GrandExchange(safe_name)
        time = datetime.now()
        timezone = pytz.timezone("America/Los_Angeles")
        pst_time = timezone.localize(time)
        embed = discord.Embed(title=ge.name, description=ge.description, url=f'{ge_url}{url_safe_name}',
                              timestamp=pst_time)
        if ge.todays_price_trend == 'positive':
            embed.color = discord.Colour.dark_green()
        elif ge.todays_price_trend == 'negative':
            embed.color = discord.Colour.dark_red()
        embed.set_thumbnail(url=ge.icon)
        embed.add_field(name='Price', value=f'**{ge.current_price}** gp', inline=False)
        embed.add_field(name='Today\'s trend', value=f'**{ge.todays_price_change}** change today, trending *{ge.todays_price_trend}*')
        embed.add_field(name="Change", value=f'**{ge.day30_change}** over the last month\n'
                                             f'**{ge.day90_change}** over the last 3 months\n'
                                             f'**{ge.day180_change}** over the last 6 months')
        if ge.is_members:
            embed.set_footer(text="Members item", icon_url=members_icon)
        else:
            embed.set_footer(text="Non members item")
        await ctx.send(f'{ctx.message.author.mention}', embed=embed)
        # Graph
        # TODO make this respond with file only if attach_files permission is true
        print("YO", discord.Permissions.attach_files)
        if discord.Permissions.attach_files:
            ge.generate_graph()
            file = discord.File('assets/graph.png')
            await ctx.send(file=file)
            file.close()
        else:
            msg = discord.Embed(title="Missing permissions", description="Bot needs 'Attach files' permissions")
            await ctx.send(embed=msg)
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

# Cog setup
def setup(bot):
    bot.add_cog(Links(bot))