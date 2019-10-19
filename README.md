# !blue

A Discord bot for pulling *Old School Runescape* hiscores, generating useful links, 
and common calculators.

## Use
Each command starts with `!blue` or `!b`. Summon a list of the bots commands by typing `!blue help`.  
`!blue help [command]` to see how to use the command  
`!blue help [Category]` to see a description of the category

## Commands
### Help
`!b help`. The help command shows a list of all available commands. 

You can call `!b help` with a command name after to 
show information on how to use each command.  
For example: `!b help attack`  
```
Pulls the attack level for a specific username

!b [attack|att] [username...]
```

### Levels
`!b help Levels` shows all the available commands.
```
Level commands used to pull stats from hiscore page.
(Logout or hop to update hiscore page) 

Commands:
  agility      
  attack       
  construction 
  cooking      
  crafting     
  defence      
  farming      
  firemaking   
  fishing      
  fletching    
  herblore     
  hitpoints    
  hunter       
  magic        
  mining       
  overall      
  prayer       
  ranged       
  runecraft    
  slayer       
  smithing     
  strength     
  thieving     
  woodcutting  

Type !b help command for more info on a command.
You can also type !b help category for more info on a category.
```

For example `!b attack bluetrane` returns:
```
bluetrane | Attack
99 (13,474,967 xp)
```

Or `!b total zezima`
```
zezima | Overall
1,465 (27,957,906 xp)
```

## Calculators
`!b help Calcs` can be used to see all available calculators with short descriptions.
```
Commonly used calculators 

Commands:
  tasks Calculates estimated slayer tasks remaining 
  wines Calculates wines needed to level 99 
  zeah  Blood and soul rune calculator 

Type !b help command for more info on a command.
You can also type !b help category for more info on a category.
```

For example `!b wines zezima` returns
```
Wine calculator
80 cooking (1,986,131 xp) | zezima
55,241 wines needed to reach level 99 (3,945 inventories)
```

## Links
The bot can return useful URLs for an easy way to share/lookup a link.
`!b help Links` shows a list of available commands.
```
Link commands to return URLs of common stuff 

Commands:
  ge      Links to the Grand Exchange website for a search 
  hiscore Links to hiscore page for a user 
  rsbuddy Links to the RSBuddy page of a search 
  wiki    Links to wiki page for a search 

Type !b help command for more info on a command.
You can also type !b help category for more info on a category.
```

For example `!b wiki rune plate` returns
```
https://oldschool.runescape.wiki/?search=rune+plate
```

## Other commands
`!b version` shows the current version of the bot  
`!b bug` links to the [issue/bug](https://github.com/zedchance/blues_bot.py/issues) page

---

Dependencies | |
--- | ---
[discord.py](https://discordpy.readthedocs.io/en/latest/) | Discord bot API
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) | Web scraping tool