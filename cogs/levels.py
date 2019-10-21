from discord.ext import commands

from helpers.hiscore import Hiscore
from calcs.experience import next_level_string, xp_to_next_level, xp_to_level

class Levels(commands.Cog):
    """ Level commands used to pull stats from hiscore page.\n(Logout or hop to update hiscore page) """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='overall',
        description='Pulls the overall level for a specific username',
        aliases=['total'],
        case_insensitive=True)
    async def overall_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Overall\n'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}**{int(user.overall_level):,}** ({int(user.overall_xp):,} xp)')
        return
    
    @commands.command(name='attack',
        description='Pulls the attack level for a specific username',
        aliases=['att'],
        case_insensitive=True)
    async def attack_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Attack'
        level = f'**{int(user.attack_level):,}** ({int(user.attack_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.attack_xp), "attack")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='defence',
        description='Pulls the defence level for a specific username',
        aliases=['defense', 'def'],
        case_insensitive=True)
    async def defence_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Defence'
        level = f'**{int(user.defence_level):,}** ({int(user.defence_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.defence_xp), "defence")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='strength',
        description='Pulls the strength level for a specific username',
        aliases=['str'],
        case_insensitive=True)
    async def strength_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Strength'
        level = f'**{int(user.strength_level):,}** ({int(user.strength_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.strength_xp), "strength")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='hitpoints',
        description='Pulls the hitpoints level for a specific username',
        aliases=['hp', 'health'],
        case_insensitive=True)
    async def hitpoints_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Hitpoints'
        level = f'**{int(user.hitpoints_level):,}** ({int(user.hitpoints_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.hitpoints_xp), "hitpoints")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='ranged',
        description='Pulls the ranged level for a specific username',
        aliases=['range', 'rng'],
        case_insensitive=True)
    async def ranged_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Ranged'
        level = f'**{int(user.ranged_level):,}** ({int(user.ranged_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.ranged_xp), "ranged")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='prayer',
        description='Pulls the prayer level for a specific username',
        aliases=['pray'],
        case_insensitive=True)
    async def prayer_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Prayer'
        level = f'**{int(user.prayer_level):,}** ({int(user.prayer_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.prayer_xp), "prayer")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='magic',
        description='Pulls the magic level for a specific username',
        aliases=['mage'],
        case_insensitive=True)
    async def magic_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Magic'
        level = f'**{int(user.magic_level):,}** ({int(user.magic_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.magic_xp), "magic")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='cooking',
        description='Pulls the cooking level for a specific username',
        aliases=['cook'],
        case_insensitive=True)
    async def cooking_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Cooking'
        level = f'**{int(user.cooking_level):,}** ({int(user.cooking_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.cooking_xp), "cooking")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='woodcutting',
        description='Pulls the woodcutting level for a specific username',
        aliases=['wc'],
        case_insensitive=True)
    async def woodcutting_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Woodcutting'
        level = f'**{int(user.woodcutting_level):,}** ({int(user.woodcutting_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.woodcutting_xp), "woodcutting")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='fletching',
        description='Pulls the fletching level for a specific username',
        aliases=['fletch'],
        case_insensitive=True)
    async def fletching_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Fletching'
        level = f'**{int(user.fletching_level):,}** ({int(user.fletching_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.fletching_xp), "fletching")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='fishing',
        description='Pulls the fishing level for a specific username',
        aliases=['fish'],
        case_insensitive=True)
    async def fishing_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Fishing'
        level = f'**{int(user.fishing_level):,}** ({int(user.fishing_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.fishing_xp), "fishing")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='firemaking',
        description='Pulls the firemaking level for a specific username',
        aliases=['fm'],
        case_insensitive=True)
    async def firemaking_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Firemaking'
        level = f'**{int(user.firemaking_level):,}** ({int(user.firemaking_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.firemaking_xp), "firemaking")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='crafting',
        description='Pulls the crafting level for a specific username',
        aliases=['craft'],
        case_insensitive=True)
    async def crafting_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Crafting'
        level = f'**{int(user.crafting_level):,}** ({int(user.crafting_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.crafting_xp), "crafting")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='smithing',
        description='Pulls the smithing level for a specific username',
        aliases=['smith'],
        case_insensitive=True)
    async def smithing_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Smithing'
        level = f'**{int(user.smithing_level):,}** ({int(user.smithing_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.smithing_xp), "smithing")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='mining',
        description='Pulls the mining level for a specific username',
        aliases=['mine'],
        case_insensitive=True)
    async def mining_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Mining'
        level = f'**{int(user.mining_level):,}** ({int(user.mining_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.mining_xp), "mining")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='herblore',
        description='Pulls the herblore level for a specific username',
        aliases=['herb'],
        case_insensitive=True)
    async def herblore_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Herblore'
        level = f'**{int(user.herblore_level):,}** ({int(user.herblore_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.herblore_xp), "herblore")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='agility',
        description='Pulls the agility level for a specific username',
        aliases=['agil'],
        case_insensitive=True)
    async def agility_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Agility'
        level = f'**{int(user.agility_level):,}** ({int(user.agility_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.agility_xp), "agility")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='thieving',
        description='Pulls the thieving level for a specific username',
        aliases=['thiev', 'thief'],
        case_insensitive=True)
    async def thieving_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Thieving'
        level = f'**{int(user.thieving_level):,}** ({int(user.thieving_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.thieving_xp), "thieving")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='slayer',
        description='Pulls the slayer level for a specific username',
        aliases=['slay'],
        case_insensitive=True)
    async def slayer_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Slayer'
        level = f'**{int(user.slayer_level):,}** ({int(user.slayer_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.slayer_xp), "slayer")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='farming',
        description='Pulls the farming level for a specific username',
        aliases=['farm'],
        case_insensitive=True)
    async def farming_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Farming'
        level = f'**{int(user.farming_level):,}** ({int(user.farming_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.farming_xp), "farming")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='runecraft',
        description='Pulls the runecraft level for a specific username',
        aliases=['rc'],
        case_insensitive=True)
    async def runecraft_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Runecraft'
        level = f'**{int(user.runecraft_level):,}** ({int(user.runecraft_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.runecraft_xp), "runecraft")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='hunter',
        description='Pulls the hunter level for a specific username',
        aliases=['hunt'],
        case_insensitive=True)
    async def hunter_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Hunter'
        level = f'**{int(user.defence_level):,}** ({int(user.defence_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.defence_xp), "defence")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return
    
    @commands.command(name='construction',
        description='Pulls the construction level for a specific username',
        aliases=['con'],
        case_insensitive=True)
    async def construction_lookup(self, ctx, *username):
        url_safe_name = '+'.join(username)
        safe_name = ' '.join(username)
        user = Hiscore(url_safe_name)
        msg = f'{safe_name} | Construction'
        level = f'**{int(user.construction_level):,}** ({int(user.construction_xp):,} xp)'
        up_msg = f'{next_level_string(int(user.construction_xp), "construction")}'
        await ctx.send(f'{ctx.message.author.mention}\n{msg}\n{level}\n{up_msg}')
        return

# Cog setup
def setup(bot):
    bot.add_cog(Levels(bot))