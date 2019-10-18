# Zeah runecrafting calculator (bloods and souls)

from helpers.hiscore import Hiscore
from calcs.experience import level_to_xp, LEVEL_99

# TODO Make sure to account for new bonus with kourend elites done
VENERATE = 2.5 / 4.0
BLOOD_XP = 23.8 + VENERATE
SOUL_XP = 29.7 + VENERATE
RUNES_PER_TRIP = 204

class Zeah():
    """ Calculator for blood and soul runes """
    
    def __init__(self, username):
        self.username = username
        user = Hiscore(username)
        self.runecraft_level = int(user.runecraft_level)
        self.runecraft_xp = int(user.runecraft_xp)
    
    def xp_needed_to_level_up(self):
        """ Returns xp needed to level up """
        return level_to_xp(self.runecraft_level + 1) - self.runecraft_xp
    
    def bloods_to_level_up(self):
        """ Returns number of blood runes needed to level up """
        return self.xp_needed_to_level_up() / BLOOD_XP
    
    def blood_trips_to_level_up(self):
        """ Returns number of blood trips to level up """
        return self.bloods_to_level_up() / RUNES_PER_TRIP
    
    def bloods_to_level_99(self):
        """ Returns number of blood runes needed to reach level 99 """
        return (LEVEL_99 - self.runecraft_xp) / BLOOD_XP
    
    def blood_trips_to_level_99(self):
        """ Returns number of blood trips to level 99 """
        return self.bloods_to_level_99() / RUNES_PER_TRIP
    
    def souls_to_level_up(self):
        """ Returns number of soul runes needed to level up """
        return self.xp_needed_to_level_up() / SOUL_XP
    
    def soul_trips_to_level_up(self):
        """ Returns number of soul trips needed to level up """
        return self.souls_to_level_up() / RUNES_PER_TRIP
    
    def souls_to_level_99(self):
        """ Returns number of soul runes needed to reach level 99 """
        return (LEVEL_99 - self.runecraft_xp) / SOUL_XP
    
    def soul_trips_to_level_99(self):
        """ Returns number of soul trips needed to level 99 """
        return self.souls_to_level_99() / RUNES_PER_TRIP