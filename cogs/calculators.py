from discord.ext import commands

from calcs.experience import next_level_string
from calcs.tasks import Tasks
from calcs.wines import Wines
from calcs.zeah import Zeah
from calcs.agility import Agility

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
            msg = f'Slayer calculator\n**{user.slayer_level}** slayer ({user.slayer_xp:,} xp) | {safe_username}'
            avg = f'{user.avg_xp_per_task():,} average xp per task'
            to_level_up = f'{user.tasks_to_level_up()} tasks to level up ({user.xp_needed_to_level_up():,} xp)'
            to_level_99 = f'{user.tasks_to_level_99()} tasks to level 99'
            last_task = f'{user.estimated_total_tasks()} estimated total tasks'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{avg}\n{to_level_up}\n{to_level_99}\n{last_task}')
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
            msg = f'Wine calculator\n**{user.cooking_level}** cooking ({user.cooking_xp:,} xp) | {safe_username}'
            remaining = f'{user.wines_to_level_99():,} wines needed to reach level 99 ({user.invs_to_level_99():,} inventories)'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{remaining}')
            return
    
    # TODO Make this work with virtual levels
    @commands.command(name='zeah',
        description='Zeah runecrafting calculator',
        aliases=['bloods', 'blood', 'souls', 'soul'],
        case_insensitive=True)
    async def zeah_command(self, ctx, *username):
        """ Blood and soul rune calculator """
        async with ctx.typing():
            safe_username = ' '.join(username)
            user = Zeah(safe_username)
            msg = f'Zeah runecraft calculator | {safe_username}\n**{user.runecraft_level}** Runecraft ({user.runecraft_xp:,} xp)'
            xp = f'{next_level_string(user.runecraft_xp, "runecraft")}'
            if (user.runecraft_level < 77):
                await ctx.send(f'{ctx.message.author.mention}\n{msg}\nYou must have at least 77 runecraft for blood runes and 90 for soul runes')
            elif (user.runecraft_level < 90):
                bloods_needed = f'{user.bloods_to_level_up() + 1:,.0f} bloods to level up ({user.blood_trips_to_level_up() + 1:,.0f} trips)'
                bloods_to_99 = f'{user.bloods_to_level_99() + 1:,.0f} bloods to level 99 ({user.blood_trips_to_level_99() + 1:,.0f} trips)'
                await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{xp}\n{bloods_needed}\n{bloods_to_99}')
            else:
                bloods_needed = f'{user.bloods_to_level_up() + 1:,.0f} bloods to level up ({user.blood_trips_to_level_up() + 1:,.0f} trips)'
                souls_needed = f'{user.souls_to_level_up() + 1:,.0f} souls to level up ({user.soul_trips_to_level_up() + 1:,.0f} trips)'
                if (user.runecraft_level < 99):
                    bloods_to_99 = f'{user.bloods_to_level_99() + 1:,.0f} bloods to level 99 ({user.blood_trips_to_level_99() + 1:,.0f} trips)'
                    souls_to_99 = f'{user.souls_to_level_99() + 1:,.0f} souls to level 99 ({user.soul_trips_to_level_99() + 1:,.0f} trips)'
                    await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{xp}\n{bloods_needed}\n{bloods_to_99}\n{souls_needed}\n{souls_to_99}')
                else:
                    await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{xp}\n{bloods_needed}\n{souls_needed}')
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
            msg = f'Rooftop agility calculator\n**{user.agility_level}** Agility ({user.agility_xp:,} xp) | {safe_username}'
            if (user.course == None):
                calc = f'You need at least level 10 agility to access Draynor rooftop course'
                next = ''
            else:
                calc = f'{user.laps_to_level_up():,.0f} laps on {user.course} to level up ({user.xp_needed_to_level_up():,.0f} xp needed)'
                if user.determine_course() == 'Ardougne':
                    ending = 'level 99'
                else:
                    ending = 'next course'
                next = f'\n{user.laps_to_next_course():,.0f} laps until {ending}'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{calc}{next}')

# Cog setup
def setup(bot):
    bot.add_cog(Calculators(bot))