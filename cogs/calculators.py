from discord.ext import commands

from calcs.tasks import Tasks

class Calculators(commands.Cog):
    """ Commonly used calculators """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tasks',
        description='Slayer task calculator',
        aliases=['task'],
        case_insensitive=True)
    async def tasks_command(self, ctx, num_of_tasks, *username):
        """ Calculates estimated tasks remaining """
        safe_username = ' '.join(username)
        user = Tasks(safe_username, num_of_tasks)
        msg = f'{user.slayer_level} Slayer ({user.slayer_xp:,} xp) | {safe_username}'
        avg = f'{user.avg_xp_per_task():,} average xp per task'
        to_level_up = f'{user.tasks_to_level_up()} tasks to level up'
        to_level_99 = f'{user.tasks_to_level_99()} tasks to level 99'
        last_task = f'{user.estimated_total_tasks()} estimated total tasks'
        await ctx.send(f'{msg}\n{avg}\n{to_level_up}\n{to_level_99}\n{last_task}')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Calculators(bot))