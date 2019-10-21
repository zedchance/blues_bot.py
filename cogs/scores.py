from discord.ext import commands

from helpers.hiscore import Hiscore

class Scores(commands.Cog):
    """ Score commands used to pull stats from hiscore page.
    This includes LMS, Bounty Hunter, and clue scrolls.
    (Logout or hop to update hiscore page) """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='bounty',
        description='Pulls bounty hunter scores for a specific username',
        aliases=['bh'],
        case_insensitive=True)
    async def bounty_lookup(self, ctx, *username):
        """ Shows bounty hunter scores and rank """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            msg = f'{safe_name} | Bounty Hunter scores'
            if user.bounty_hunter_hunter_score == '-1':
                hunter = f'\nYou have never played as hunter'
            else:
                hunter = f'\n**{int(user.bounty_hunter_hunter_score):,}** Hunter score (Rank {int(user.bounty_hunter_hunter_rank):,})'
            if user.bounty_hunter_rogue_rank == '-1':
                rogue = f'\nYou have never played as rogue'
            else:
                rogue = f'\n**{int(user.bounty_hunter_rogue_score):,}** Rogue score (Rank {int(user.bounty_hunter_rogue_rank):,})'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}{hunter}{rogue}')
            return
    
    @commands.command(name='lms',
        description='Pulls LMS scores for a specific username',
        aliases=[],
        case_insensitive=True)
    async def lms_lookup(self, ctx, *username):
        """ Shows LMS scores and rank """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            msg = f'{safe_name} | Last Man Standing scores'
            if user.lms_score == '-1':
                lms = f'\nYou have never played LMS'
            else:
                lms = f'\n**{int(user.lms_score):,}** score (Rank {int(user.lms_rank):,})'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}{lms}')
            return
    
    @commands.command(name='clues',
        description='Pulls LMS scores for a specific username',
        aliases=['clue', 'scrolls'],
        case_insensitive=True)
    async def clue_lookup(self, ctx, *username):
        """ Shows clue scrolls for user """
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            msg = f'{safe_name} | Clue scrolls'
            if user.all_clues_rank == '-1':
                all = f'\nYou haven\'t solved any clue scrolls'
            else:
                all = f'\n{int(user.all_clues_score):<9,} Total clues    (Rank {int(user.all_clues_rank):,})'
            if user.beginner_clues_rank == '-1':
                beginner = f''
            else:
                beginner = f'\n{int(user.beginner_clues_score):<9,} Beginner clues (Rank {int(user.beginner_clues_rank):,})'
            if user.easy_clues_rank == '-1':
                easy = f''
            else:
                easy = f'\n{int(user.easy_clues_score):<9,} Easy clues     (Rank {int(user.easy_clues_rank):,})'
            if user.medium_clues_rank == '-1':
                medium = f''
            else:
                medium = f'\n{int(user.medium_clues_score):<9,} Medium clues   (Rank {int(user.medium_clues_rank):,})'
            if user.hard_clues_rank == '-1':
                hard = f''
            else:
                hard = f'\n{int(user.hard_clues_score):<9,} Hard clues     (Rank {int(user.hard_clues_rank):,})'
            if user.elite_clues_rank == '-1':
                elite = f''
            else:
                elite = f'\n{int(user.elite_clues_score):<9,} Elite clues    (Rank {int(user.elite_clues_rank):,})'
            if user.master_clues_rank == '-1':
                master = f''
            else:
                master = f'\n{int(user.master_clues_score):<9,} Master clues   (Rank {int(user.master_clues_rank):,})'
            await ctx.send(f'{ctx.message.author.mention}\n{msg}```{all}{beginner}{easy}{medium}{hard}{elite}{master}```')
            return

# Cog setup
def setup(bot):
    bot.add_cog(Scores(bot))