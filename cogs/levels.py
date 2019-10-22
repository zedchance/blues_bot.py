import discord
from discord.ext import commands

from helpers.hiscore import Hiscore
from calcs.experience import next_level_string, xp_to_next_level, xp_to_level
from helpers.urls import get_icon_url

class Levels(commands.Cog):
    """ Level commands used to pull stats from hiscore page.\n(Logout or hop to update hiscore page) """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='overall',
        description='Pulls the overall level for a specific username',
        aliases=['total'],
        case_insensitive=True)
    async def overall_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Overall", description=f'{safe_name}')
            embed.add_field(name="Level", value=f'**{int(user.overall_level):,}**', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.overall_rank):,}', inline=True)
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='attack',
        description='Pulls the attack level for a specific username',
        aliases=['att'],
        case_insensitive=True)
    async def attack_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Attack", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("attack")}')
            embed.add_field(name="Level", value=f'**{int(user.attack_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.attack_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.attack_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.attack_xp), "attack")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='defence',
        description='Pulls the defence level for a specific username',
        aliases=['defense', 'def'],
        case_insensitive=True)
    async def defence_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Defence", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("defence")}')
            embed.add_field(name="Level", value=f'**{int(user.defence_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.defence_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.defence_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.defence_xp), "defence")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='strength',
        description='Pulls the strength level for a specific username',
        aliases=['str'],
        case_insensitive=True)
    async def strength_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Strength", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("strength")}')
            embed.add_field(name="Level", value=f'**{int(user.strength_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.strength_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.strength_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.strength_xp), "strength")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='hitpoints',
        description='Pulls the hitpoints level for a specific username',
        aliases=['hp', 'health'],
        case_insensitive=True)
    async def hitpoints_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Hitpoints", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("hitpoints")}')
            embed.add_field(name="Level", value=f'**{int(user.hitpoints_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.hitpoints_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.hitpoints_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.hitpoints_xp), "hitpoints")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='ranged',
        description='Pulls the ranged level for a specific username',
        aliases=['range', 'rng'],
        case_insensitive=True)
    async def ranged_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Ranged", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("ranged")}')
            embed.add_field(name="Level", value=f'**{int(user.ranged_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.ranged_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.ranged_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.ranged_xp), "ranged")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='prayer',
        description='Pulls the prayer level for a specific username',
        aliases=['pray'],
        case_insensitive=True)
    async def prayer_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Prayer", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("prayer")}')
            embed.add_field(name="Level", value=f'**{int(user.prayer_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.prayer_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.prayer_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.prayer_xp), "prayer")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='magic',
        description='Pulls the magic level for a specific username',
        aliases=['mage'],
        case_insensitive=True)
    async def magic_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Magic", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("magic")}')
            embed.add_field(name="Level", value=f'**{int(user.magic_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.magic_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.magic_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.magic_xp), "magic")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='cooking',
        description='Pulls the cooking level for a specific username',
        aliases=['cook'],
        case_insensitive=True)
    async def cooking_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Cooking", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("cooking")}')
            embed.add_field(name="Level", value=f'**{int(user.cooking_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.cooking_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.cooking_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.cooking_xp), "cooking")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='woodcutting',
        description='Pulls the woodcutting level for a specific username',
        aliases=['wc'],
        case_insensitive=True)
    async def woodcutting_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Woodcutting", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("woodcutting")}')
            embed.add_field(name="Level", value=f'**{int(user.woodcutting_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.woodcutting_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.woodcutting_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.woodcutting_xp), "woodcutting")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='fletching',
        description='Pulls the fletching level for a specific username',
        aliases=['fletch'],
        case_insensitive=True)
    async def fletching_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Fletching", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("fletching")}')
            embed.add_field(name="Level", value=f'**{int(user.fletching_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.fletching_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.fletching_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.fletching_xp), "fletching")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='fishing',
        description='Pulls the fishing level for a specific username',
        aliases=['fish'],
        case_insensitive=True)
    async def fishing_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Fishing", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("fishing")}')
            embed.add_field(name="Level", value=f'**{int(user.fishing_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.fishing_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.fishing_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.fishing_xp), "fishing")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='firemaking',
        description='Pulls the firemaking level for a specific username',
        aliases=['fm'],
        case_insensitive=True)
    async def firemaking_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Firemaking", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("firemaking")}')
            embed.add_field(name="Level", value=f'**{int(user.firemaking_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.firemaking_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.firemaking_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.firemaking_xp), "firemaking")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='crafting',
        description='Pulls the crafting level for a specific username',
        aliases=['craft'],
        case_insensitive=True)
    async def crafting_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Crafting", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("crafting")}')
            embed.add_field(name="Level", value=f'**{int(user.crafting_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.crafting_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.crafting_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.crafting_xp), "crafting")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='smithing',
        description='Pulls the smithing level for a specific username',
        aliases=['smith'],
        case_insensitive=True)
    async def smithing_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Smithing", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("smithing")}')
            embed.add_field(name="Level", value=f'**{int(user.smithing_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.smithing_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.smithing_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.smithing_xp), "smithing")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='mining',
        description='Pulls the mining level for a specific username',
        aliases=['mine'],
        case_insensitive=True)
    async def mining_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Mining", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("mining")}')
            embed.add_field(name="Level", value=f'**{int(user.mining_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.mining_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.mining_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.mining_xp), "mining")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='herblore',
        description='Pulls the herblore level for a specific username',
        aliases=['herb'],
        case_insensitive=True)
    async def herblore_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Herblore", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("herblore")}')
            embed.add_field(name="Level", value=f'**{int(user.herblore_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.herblore_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.herblore_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.herblore_xp), "herblore")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='agility',
        description='Pulls the agility level for a specific username',
        aliases=['agil'],
        case_insensitive=True)
    async def agility_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Agility", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("agility")}')
            embed.add_field(name="Level", value=f'**{int(user.agility_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.agility_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.agility_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.agility_xp), "agility")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='thieving',
        description='Pulls the thieving level for a specific username',
        aliases=['thiev', 'thief'],
        case_insensitive=True)
    async def thieving_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Thieving", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("thieving")}')
            embed.add_field(name="Level", value=f'**{int(user.thieving_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.thieving_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.thieving_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.thieving_xp), "thieving")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='slayer',
        description='Pulls the slayer level for a specific username',
        aliases=['slay'],
        case_insensitive=True)
    async def slayer_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Slayer", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("slayer")}')
            embed.add_field(name="Level", value=f'**{int(user.slayer_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.slayer_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.slayer_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.slayer_xp), "slayer")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='farming',
        description='Pulls the farming level for a specific username',
        aliases=['farm'],
        case_insensitive=True)
    async def farming_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Farming", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("farming")}')
            embed.add_field(name="Level", value=f'**{int(user.farming_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.farming_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.farming_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.farming_xp), "farming")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='runecraft',
        description='Pulls the runecraft level for a specific username',
        aliases=['rc'],
        case_insensitive=True)
    async def runecraft_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Runecraft", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("runecraft")}')
            embed.add_field(name="Level", value=f'**{int(user.runecraft_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.runecraft_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.runecraft_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.runecraft_xp), "runecraft")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='hunter',
        description='Pulls the hunter level for a specific username',
        aliases=['hunt'],
        case_insensitive=True)
    async def hunter_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Hunter", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("hunter")}')
            embed.add_field(name="Level", value=f'**{int(user.hunter_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.hunter_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.hunter_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.hunter_xp), "hunter")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return
    
    @commands.command(name='construction',
        description='Pulls the construction level for a specific username',
        aliases=['con'],
        case_insensitive=True)
    async def construction_lookup(self, ctx, *username):
        async with ctx.typing():
            url_safe_name = '+'.join(username)
            safe_name = ' '.join(username)
            user = Hiscore(url_safe_name)
            embed = discord.Embed(title="Construction", description=f'{safe_name}')
            embed.set_thumbnail(url=f'{get_icon_url("construction")}')
            embed.add_field(name="Level", value=f'**{int(user.construction_level):,}**', inline=True)
            embed.add_field(name="XP", value=f'{int(user.construction_xp):,}', inline=True)
            embed.add_field(name="Rank", value=f'{int(user.construction_rank):,}')
            embed.set_footer(text=f'{next_level_string(int(user.construction_xp), "construction")}')
            await ctx.send(f'{ctx.message.author.mention}', embed=embed)
            return

# Cog setup
def setup(bot):
    bot.add_cog(Levels(bot))