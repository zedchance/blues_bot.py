from discord.ext import commands

from calcs.tasks import Tasks
from calcs.wines import Wines

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
        safe_username = ' '.join(username)
        user = Tasks(safe_username, num_of_tasks)
        msg = f'Slayer calculator\n**{user.slayer_level}** slayer ({user.slayer_xp:,} xp) | {safe_username}'
        avg = f'{user.avg_xp_per_task():,} average xp per task'
        to_level_up = f'{user.tasks_to_level_up()} tasks to level up ({user.xp_needed_to_level_up():,} xp)'
        to_level_99 = f'{user.tasks_to_level_99()} tasks to level 99'
        last_task = f'{user.estimated_total_tasks()} estimated total tasks'
        await ctx.send(f'{msg}\n{avg}\n{to_level_up}\n{to_level_99}\n{last_task}')
        return

    @commands.command(name='wines',
        description='Wine cooking calculator',
        aliases=['wine'],
        case_insensitive=True)
    async def wines_command(self, ctx, *username):
        """ Calculates wines needed to level 99 """
        safe_username = ' '.join(username)
        user = Wines(safe_username)
        msg = f'Wine calculator\n**{user.cooking_level}** cooking ({user.cooking_xp:,} xp) | {safe_username}'
        remaining = f'{user.wines_to_level_99():,} wines needed to reach level 99 ({user.invs_to_level_99():,} inventories)'
        await ctx.send(f'{msg}\n{remaining}')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Calculators(bot))