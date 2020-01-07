from datetime import datetime

import discord
import pytz
from discord.ext import commands

from helpers.ge import GrandExchange
from helpers.monsters import load_monster_from_api, parse_monster_drops
from helpers.news import News
from helpers.urls import hiscore_url, wiki_url, ge_url, rsbuddy_url, members_icon, news_icon


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
        embed.add_field(name='Today\'s trend',
                        value=f'**{ge.todays_price_change}** change today, trending *{ge.todays_price_trend}*')
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

    @commands.command(name='news',
                      description='Latest OSRS news',
                      aliases=['latest'],
                      case_insensitive=True)
    async def news_command(self, ctx):
        """ Latest OSRS news """
        async with ctx.typing():
            news = News()
            embed = discord.Embed(title=news.title)
            embed.set_thumbnail(url=news_icon)
            embed.add_field(name=f'Latest post - {news.articles[0][2]}',
                            value=f'[**{news.articles[0][0]}**]({news.articles[0][3]})\n'
                                  f'{news.latest_article_text}',
                            inline=False)
            for i in range(1, 4):
                embed.add_field(name=news.articles[i][2], value=f'**[{news.articles[i][0]}]({news.articles[i][3]})**\n'
                                                                f'{news.articles[i][1]}')
            embed.set_footer(text=f'Latest post: {news.articles[0][4]}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

    @commands.command(name='monster',
                      description='Lookup osrs monsters.',
                      aliases=['qs'],
                      case_insensitive=True)
    async def monster_command(self, ctx, *monster):
        """ Looks up a monster """
        monster = " ".join(monster)
        loaded_monster = load_monster_from_api(monster.lower())
        if loaded_monster is not False:
            stats = f"`Combat level:` {loaded_monster.combat_level} \n"
            stats += f"`Hitpoints:` {loaded_monster.hitpoints} \n"
            stats += f"`Max hit:` {loaded_monster.max_hit} \n"
            stats += f"`Aggressive:` {'Yes' if loaded_monster.aggressive else 'No'} \n"
            stats += f"`Attack speed:` {loaded_monster.attack_speed} ticks \n"
            stats += f"`Weakness:` {'None' if len(loaded_monster.weakness) == 0 else ', '.join([x.capitalize() for x in loaded_monster.weakness])} \n "
            stats += f"`Attack style:` {', '.join([x.capitalize() for x in loaded_monster.attack_type])} \n"
            embed = discord.Embed(title=loaded_monster.name, url=loaded_monster.wiki_url)
            embed.add_field(name="Members only", value="Yes" if loaded_monster.members else "No", inline=True)
            embed.add_field(name="Examine", value=loaded_monster.examine, inline=True)
            embed.add_field(name="Detailed", value=stats, inline=False)
            embed.set_footer(text=f"Released: {loaded_monster.release_date}")
            loaded_monster_drops = parse_monster_drops(loaded_monster.drops)
            if len(loaded_monster_drops) > 0:
                drops = [f"`{drop['name']}:` {drop['rarity_string']}" for drop in loaded_monster_drops[:5]]
                embed.add_field(name="Rarest drops", value="\n".join(drops))
            return await ctx.send(embed=embed)
        else:
            return await ctx.send("Sorry, we could not find that monster.")


# Cog setup
def setup(bot):
    bot.add_cog(Links(bot))
