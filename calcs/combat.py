# Combat calculator

from math import floor

from helpers.hiscore import Hiscore

class Combat(Hiscore):
    """ Combat level calculator """
    
    def calculate_combat(self):
        """ Calculate user's combat level """
        base = 0.25 * (self.defence_level + self.hitpoints_level + floor(self.prayer_level / 2))
        melee = 0.325 * (self.attack_level + self.strength_level)
        ranged = 0.325 * (floor(3 * self.ranged_level / 2))
        magic = 0.325 * (floor(3 * self.magic_level / 2))
        m = melee
        if ranged > m:
            m = ranged
        if magic > m:
            m = magic
        return base + m
        