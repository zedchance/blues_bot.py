import discord
from discord.ext import commands

from calcs.experience import next_level_string
from calcs.tasks import Tasks
from calcs.wines import Wines
from calcs.wintertodt import Wintertodt
from calcs.zeah import Zeah
from calcs.agility import Agility
from helpers.hiscore import Hiscore
from helpers.urls import get_icon_url

class Calculators(commands.Cog):
    """ Commonly used calculators """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tasks',
        description='''Slayer task calculator
        This calculator is more accurate at higher levels''',
        aliases=['task'],
        case_insensitive=True)
    async def tasks_command(self, ctx, num_of_tasks, *username):
        """ Calculates estimated slayer tasks remaining """
        async with ctx.typing():
            safe_username = ' '.join(username)
            user = Tasks(safe_username, num_of_tasks)
            embed = discord.Embed(title="Slayer Task Calculator", description=f'**{user.slayer_level}** slayer ({user.slayer_xp:,} xp) | {safe_username}')
            embed.set_thumbnail(url=get_icon_url("slayer"))
            embed.add_field(name="Average XP per task", value=f'{user.avg_xp_per_task():,}', inline=True)
            embed.add_field(name="Tasks needed to level up", value=f'{user.tasks_to_level_up()} ({user.xp_needed_to_level_up():,} xp)', inline=True)
            if (user.slayer_level < 99):
                embed.add_field(name="Tasks to level 99", value=f'{user.tasks_to_level_99()}', inline=True)
                embed.add_field(name="Estimated total tasks", value=f'{user.estimated_total_tasks()}', inline=True)
            embed.set_footer(text="This calculator is more accurate at higher slayer levels")
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

    @commands.command(name='wines',
        description='Wine cooking calculator',
        aliases=['wine'],
        case_insensitive=True)
    async def wines_command(self, ctx, *username):
        """ Calculates wines needed to level 99 """
        async with ctx.typing():
            safe_username = ' '.join(username)
            user = Wines(safe_username)
            embed = discord.Embed(title="Wine cooking calculator", description=f'**{user.cooking_level}** cooking ({user.cooking_xp:,} xp) | {safe_username}')
            embed.set_thumbnail(url=get_icon_url("cooking"))
            if (user.cooking_level < 99):
                embed.add_field(name="Wines to reach level 99", value=f'{user.wines_to_level_99():,}', inline=True)
                embed.add_field(name="Inventories", value=f'{user.invs_to_level_99():,}', inline=True)
            else:
                embed.add_field(name="Wines to reach 200m xp", value=f'{user.wines_to_200m():,}', inline=True)
                embed.add_field(name="Inventories", value=f'{user.invs_to_200m():,}', inline=True)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

    @commands.command(name='zeah',
        description='Zeah runecrafting calculator',
        aliases=['bloods', 'blood', 'souls', 'soul'],
        case_insensitive=True)
    async def zeah_command(self, ctx, *username):
        """ Blood and soul rune calculator """
        async with ctx.typing():
            safe_username = ' '.join(username)
            user = Zeah(safe_username)
            embed = discord.Embed(title="Zeah runecrafting calculator", description=f'**{user.runecraft_level}** Runecraft ({user.runecraft_xp:,} xp) | {safe_username}')
            embed.set_thumbnail(url=get_icon_url("runecraft"))
            embed.set_footer(text=f'{next_level_string(user.runecraft_xp, "runecraft")}')
            if (user.runecraft_level < 77):
                embed.add_field(name="Level too low", value="You need a runecraft level of at least 77 to make blood runes", inline=True)
            elif (user.runecraft_level < 90):
                embed.add_field(name="Bloods to level up", value=f'{user.bloods_to_level_up() + 1:,.0f}', inline=True)
                embed.add_field(name="Blood trips", value=f'{user.blood_trips_to_level_up() + 1:,.0f}', inline=True)
                embed.add_field(name="Bloods to level 99", value=f'{user.bloods_to_level_99() + 1:,.0f}', inline=True)
                embed.add_field(name="Blood trips to 99", value=f'{user.blood_trips_to_level_99() + 1:,.0f}', inline=True)
            else:
                embed.add_field(name="Bloods to level up", value=f'{user.bloods_to_level_up() + 1:,.0f}', inline=True)
                embed.add_field(name="Blood trips", value=f'{user.blood_trips_to_level_up() + 1:,.0f}', inline=True)
                embed.add_field(name="Souls to level up", value=f'{user.souls_to_level_up() + 1:,.0f}', inline=True)
                embed.add_field(name="Soul trips", value=f'{user.soul_trips_to_level_up() + 1:,.0f}', inline=True)
                if (user.runecraft_level < 99):
                    embed.add_field(name="Bloods to level 99", value=f'{user.bloods_to_level_99() + 1:,.0f}', inline=True)
                    embed.add_field(name="Blood trips to 99", value=f'{user.blood_trips_to_level_99() + 1:,.0f}', inline=True)
                    embed.add_field(name="Souls to level 99", value=f'{user.souls_to_level_99() + 1:,.0f}', inline=True)
                    embed.add_field(name="Soul trips to 99", value=f'{user.soul_trips_to_level_99() + 1:,.0f}', inline=True)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='rooftop',
        description='Rooftop agility course calculator',
        aliases=[],
        case_insensitive=True)
    async def rooftop_command(self, ctx, *username):
        """ Rooftop agility course calculator """
        async with ctx.typing():
            safe_username = ' '.join(username)
            user = Agility(safe_username)
            embed = discord.Embed(title="Rooftop agility calculator", description=f'**{user.agility_level}** Agility ({user.agility_xp:,} xp) | {safe_username}')
            embed.set_thumbnail(url=get_icon_url("agility"))
            if (user.course == None):
                embed.add_field(name="Level too low", value="You need at least 10 agility to use the Draynor rooftop course", inline=False)
            else:
                embed.add_field(name="XP needed to level up", value=f'{user.xp_needed_to_level_up():,.0f}', inline=True)
                embed.add_field(name=f'Laps to level up', value=f'{user.laps_to_level_up():,.0f} on {user.course}', inline=True)
                embed.add_field(name=f'Laps until {user.next_course}', value=f'{user.laps_to_next_course():,.0f}', inline=True)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)

    @commands.command(name='wintertodt',
        description='Calculates estimated Wintertodt kill count',
        aliases=['wt'],
        case_insensitive=True)
    async def wintertodt_command(self, ctx, *username):
        """ Wintertodt calculator """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            wt = Wintertodt(url_safe_name)
            embed = discord.Embed(title="Wintertodt calculator", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("firemaking")}')
            if int(wt.firemaking_level) < 50:
                embed.add_field(name="Level too low", value=f'You need at least **50** firemaking to attempt Wintertodt.\n'
                                                            f'You currently only have level **{wt.firemaking_level}**')
            else:
                embed.add_field(name="Level", value=f'**{int(wt.firemaking_level):,}**', inline=True)
                embed.add_field(name="XP", value=f'{int(wt.firemaking_xp):,}', inline=True)
                embed.add_field(name="Wintertodt kill count", value=f'{int(wt.kc_wintertodt):,}')
                embed.add_field(name="Average XP per kill", value=f'{wt.average():,} xp')
                embed.add_field(name="Kills to level up", value=f'{wt.kills_to_level_up():,.0f}')
                embed.add_field(name="Kills to level 99", value=f'{wt.kills_to_level_99():,} (~{wt.estimated_total_kills():,} total)')
            embed.set_footer(text=f'{next_level_string(int(wt.firemaking_xp), "firemaking")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

# Cog setup
def setup(bot):
    bot.add_cog(Calculators(bot))