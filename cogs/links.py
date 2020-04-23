import logging
import asyncio
import requests
from datetime import datetime
from bs4 import BeautifulSoup

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
        if url_safe == "":
            url = "https://oldschool.runescape.wiki/"
        else:
            url = wiki_url + url_safe
        time = datetime.now()
        timezone = pytz.timezone("America/Los_Angeles")
        pst_time = timezone.localize(time)
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        embed = discord.Embed(timestamp=pst_time)
        try:
            description = soup.find(property="og:description")["content"]
            embed.description = description
        except TypeError:
            embed = discord.Embed(title="Oops......",
                                  description="Something went wrong with your request, please make sure to check the"
                                              " spelling or try again later.",
                                  timestamp=pst_time)
            await ctx.send(ctx.message.author.mention)
            return await ctx.send(embed=embed)
        try:
            title = soup.find(property="og:title")["content"]
            embed.title = title
        except TypeError:
            pass
        try:
            image = soup.find(property="og:image")["content"]
            embed.set_image(url=image)
        except TypeError:
            pass
        embed.url = url
        await ctx.send(ctx.message.author.mention)
        return await ctx.send(embed=embed)

    @commands.command(name='price',
                      description='Use to lookup items on the Grand Exchange',
                      aliases=['-g', 'ge'],
                      case_insensitive=True)
    async def ge_command(self, ctx, *search_description):
        """ Responds with information about an item from the Grand Exchange """
        safe_name = ' '.join(search_description).lower()
        url_safe_name = safe_name.replace(' ', '+')
        ge = GrandExchange(safe_name)
        async with ctx.typing():
            await ge.fetch()
        time = datetime.now()
        timezone = pytz.timezone("America/Los_Angeles")
        pst_time = timezone.localize(time)
        if ge.multiple_results:
            embed = discord.Embed(title="Grand Exchange",
                                  description=f'There are multiple results for `{safe_name}`',
                                  url=f'{ge_url}{url_safe_name}',
                                  timestamp=pst_time)
            embed.add_field(name="Results", value=ge.get_possible_matches_str())
            await ctx.send(embed=embed)

            def check(msg):
                return msg.content in [str(i) for i in range(1, len(ge.matches) + 1)]\
                       and msg.channel == ctx.channel\
                       and msg.author == ctx.message.author

            try:
                choice = await ctx.bot.wait_for('message', check=check, timeout=10)
            except asyncio.TimeoutError:
                logging.info(f'Timeout on choice from {ctx.message.author}.')
            else:
                name = f'{ge.matches[int(choice.content) - 1]["name"].lower()}'
                await ctx.send(f'!b price {name}')
                async with ctx.typing():
                    await ctx.invoke(self.ge_command, name)
        else:
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
            other_info = f'High alch: {ge.high_alch} gp \u2022 {ge.buy_limit} buy limit'
            if ge.is_members:
                embed.set_footer(text=f'{other_info}\nMembers item', icon_url=members_icon)
            else:
                embed.set_footer(text=f'{other_info}\nNon members item')
            # Graph
            ge.generate_graph()
            file = discord.File('assets/graph.png', filename='graph.png')
            embed.set_image(url='attachment://graph.png')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed, file=file)
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

    @commands.command(name='news',
                      description='Latest OSRS news',
                      aliases=['latest'],
                      case_insensitive=True)
    async def news_command(self, ctx):
        """ Latest OSRS news """
        async with ctx.typing():
            news = News()
            embed = discord.Embed(title=news.title)
            embed.set_thumbnail(url=news.image)
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
        if len(list(monster)) < 3:
            return await ctx.send("Sorry, invalid input. Minimum of 3 characters required.")
        loaded_monster = load_monster_from_api(monster.lower())
        if loaded_monster is not False:
            if len(loaded_monster) == 1:
                loaded_monster = loaded_monster[0]
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
                results = ""
                for index, x in enumerate(loaded_monster):
                    results += f"`{index + 1}` {x.name} \n"
                time = datetime.now()
                timezone = pytz.timezone("America/Los_Angeles")
                pst_time = timezone.localize(time)
                embed = discord.Embed(title="Monsters",
                                      description=f'There are multiple results for `{monster}`',
                                      timestamp=pst_time)
                embed.add_field(name="Results", value=results + f"\nReply with a number for more information.")
                await ctx.send(embed=embed)

                def check(m):
                    return m.content in [str(i) for i in range(1, len(loaded_monster) + 1)] \
                           and m.channel == ctx.channel and ctx.author == m.author
                try:
                    choice = await ctx.bot.wait_for('message', timeout=10.0, check=check)
                except asyncio.TimeoutError:
                    return await ctx.send("Request timed out.")
                if choice:
                    name = f'{loaded_monster[int(choice.content) - 1].name.lower()}'
                    await ctx.send(f'!b monster {name}')
                    async with ctx.typing():
                        return await ctx.invoke(self.monster_command, name)
        else:
            return await ctx.send("Sorry, we could not find that monster.")


# Cog setup
def setup(bot):
    bot.add_cog(Links(bot))
