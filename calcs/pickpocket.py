from tabulate import tabulate

from calcs.experience import level_to_xp, xp_to_level, LEVEL_99

from helpers.hiscore import Hiscore

PP = {
    'Man': (1, 8),
    'Farmer': (10, 14.5),
    'Female HAM member': (15, 18.5),
    'Male HAM member': (20, 22.2),
    'Warrior': (25, 26),
    'Villager': (30, 8),
    'Rogue': (32, 36.5),
    'Cave goblin': (36, 40),
    'Master Farmer': (38, 43),
    'Guard': (40, 46.8),
    'Fremennik Citizen': (45, 65),
    'Bearded Pollnivian Bandit': (45, 65),
    'Desert Bandit': (53, 79.4),
    'Knight of Ardougne': (55, 84.3),
    'Pollnivian Bandit': (55, 84.3),
    'Yanille Watchman': (65, 137.5),
    'Paladin': (70, 151.8),
    'Gnome': (75, 198.3),
    'Hero': (80, 273.3),
    'Vyre': (82, 306.9),
    'Elf': (85, 353.3),
    'TzHaar-Hur': (90, 103.4),
}


class Pickpocket(Hiscore):
    """ Thieving pickpocket calculator """

    def pp_to_next_lvl(self, name):
        """ Returns amount of pickpockets to lvl up """
        needed = self.xp_needed_to_level_up("Thieving")
        lvl, xp = PP[name]
        if self.thieving_level < lvl:
            return False
        return needed // xp

    def generate_table(self):
        results = [('Lvl', 'Name', 'Amount to lvl up')]
        for i in PP:
            name = i
            lvl, xp = PP[i]
            pp_needed = f'{self.pp_to_next_lvl(name):,.0f}'
            if lvl in range(self.thieving_level - 20, self.thieving_level + 1):
                results.append((lvl, name, pp_needed))
        return tabulate(results, tablefmt='plain')
