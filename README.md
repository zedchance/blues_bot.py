# !blue

A Discord bot for pulling *Old School Runescape* hiscores, generating useful links, 
and common calculators.

* [Try the bot out](#try-the-bot-out)
* [Use](#use)
* [Commands](#commands)
  * [Help](#help)
  * [Levels](#levels)
  * [Scores](#scores)
  * [Calculators](#calculators)
  * [Links](#links)
  * [Other commands](#other-commands)
* [Dependencies](#dependencies)

## Try the bot out
You can test the bot [in my server](https://discord.gg/WUsZ5Hf). Feel free to leave suggestions in the `#suggestions` channel! You can report any issues you have with the bot [on the issue page](https://github.com/zedchance/blues_bot.py/issues).

## Use
Each command starts with `!blue` or `!b`. Summon a list of the bots commands by typing `!blue help`.  
`!blue help [command]` to see how to use the command  
`!blue help [Category]` to see a description of the category  
<img src="screenshots/help_light.png" width="450">

## Commands
### Help
`!b help`. The help command shows a list of all available commands. 

You can call `!b help` with a command name after to 
show information on how to use each command.  
For example: `!b help attack`  
<img src="screenshots/help_att_light.png" width="350">

### Levels
`!b lvl` shows all the available commands.  
<img src="screenshots/lvl_light.png" width="400">

For example `!b attack bluetrane` returns:  
<img src="screenshots/att_command_light.png" width="250">

Or `!b total zezima`  
<img src="screenshots/total_zezima_light.png" width="250">

Show a user's boss kill counts with `!b kc bluetrane`:  
<img src="screenshots/kc_light.png" width="480">

To view all level 99s use `!b 99s bluetrane`:  
<img src="screenshots/99s_light.png" width="200">

`!b xp bluetrane` is a helpful weekly summary of XP gains and other details.  
<img src="screenshots/xp_light.png" width="430">  
This pulls data from [Crystal Math Labs](https://crystalmathlabs.com).

### Scores
`!b help scores` shows a list of the commands available  
<img src="screenshots/scores_light.png" width="350">

For example `!b clues bluetrane` returns  
<img src="screenshots/clues_light.png" width="450">

### Calculators
`!b help calculators` can be used to see all available calculators with short descriptions.  
<img src="screenshots/calculators_light.png" width="400">

For example `!b wines zezima` returns  
<img src="screenshots/wines_light.png" width="320">

Or `!b rooftop bluetrane` returns  
<img src="screenshots/rooftop_light.png" width="450">

### Links
The bot can return useful URLs for an easy way to share/lookup a link.
`!b help links` shows a list of available commands.  
<img src="screenshots/links_light.png" width="550">

For example `!b ge trident` returns  
<img src="screenshots/ge_light_graph.png" width="550">

Or `!b wiki rune plate` returns
```
https://oldschool.runescape.wiki/?search=rune+plate
```

### Other commands
`!b version` shows the current version of the bot  
`!b bug` links to the [issue/bug](https://github.com/zedchance/blues_bot.py/issues) page

## Dependencies

Library | Description
--- | ---
[discord.py](https://discordpy.readthedocs.io/en/latest/) | Discord bot API
[requests](https://github.com/psf/requests) | HTTP request library
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) | Web scraping tool
[embed_help](https://github.com/zedchance/embed_help) | Better looking help messages
[matplotlib](https://matplotlib.org) | Python 2D plotting library
[Crystal Math Labs](https://crystalmathlabs.com) | OSRS XP tracking site