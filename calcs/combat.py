# Combat calculator

from math import floor

from helpers.hiscore import Hiscore

class Combat():
    """ Combat level calculator """
    
    def __init__(self, username):
        self.username = username
        user = Hiscore(username)
        self.hitpoints_level = int(user.hitpoints_level)
        self.attack_level = int(user.attack_level)
        self.strength_level = int(user.strength_level)
        self.defence_level = int(user.defence_level)
        self.prayer_level = int(user.prayer_level)
        self.ranged_level = int(user.ranged_level)
        self.magic_level = int(user.magic_level)
    
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
        