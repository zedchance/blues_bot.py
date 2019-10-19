# Agility rooftop course calculator

from helpers.hiscore import Hiscore
from calcs.experience import level_to_xp, LEVEL_99

DRAYNOR_LEVEL = 10
DRAYNOR_LAP = 120
AL_KHARID_LEVEL = 20
AL_KHARID_LAP = 180
VARROCK_LEVEL = 30
VARROCK_LAP = 238
CANIFIS_LEVEL = 40
CANIFIS_LAP = 240
FALADOR_LEVEL = 50
FALADOR_LAP = 440
SEERS_LEVEL = 60
SEERS_LAP = 570
POLLNIVEACH_LEVEL = 70
POLLNIVEACH_LAP = 890
RELLEKKA_LEVEL = 80
RELLEKKA_LAP = 780
ARDOUGNE_LEVEL = 90
ARDOUGNE_LAP = 793

class Agility():
    """ Agility rooftop course calculator """
    
    def __init__(self, username):
        self.username = username
        user = Hiscore(username)
        self.agility_level = int(user.agility_level)
        self.agility_xp = int(user.agility_xp)
        self.course = self.determine_course()
    
    def determine_course(self):
        """ Determines highest level course user can use and sets lap xp"""
        if self.agility_level < DRAYNOR_LEVEL:
            return None
        elif self.agility_level < AL_KHARID_LEVEL:
            self.lap_xp = DRAYNOR_LAP
            return "Draynor"
        elif self.agility_level < VARROCK_LEVEL:
            self.lap_xp = AL_KHARID_LAP
            return "Al Kharid"
        elif self.agility_level < CANIFIS_LEVEL:
            self.lap_xp = VARROCK_LAP
            return "Varrock"
        elif self.agility_level < FALADOR_LEVEL:
            self.lap_xp = CANIFIS_LAP
            return "Canifis"
        elif self.agility_level < SEERS_LEVEL:
            self.lap_xp = FALADOR_LAP
            return "Falador"
        elif self.agility_level < POLLNIVEACH_LEVEL:
            self.lap_xp = SEERS_LAP
            return "Seers"
        elif self.agility_level < RELLEKKA_LEVEL:
            self.lap_xp = POLLNIVEACH_LAP
            return "Pollniveach"
        elif self.agility_level < ARDOUGNE_LEVEL:
            self.lap_xp = RELLEKKA_LAP
            return "Rellekka"
        else:
            self.lap_xp = ARDOUGNE_LAP
            return "Ardougne"
    
    def xp_needed_to_level_up(self):
        """ Returns the amount of xp needed to level up """
        return level_to_xp(self.agility_level + 1) - self.agility_xp
    
    def laps_to_level_up(self):
        """ Returns number of laps on highest available course to level up """
        return self.xp_needed_to_level_up() // self.lap_xp + 1
    
    def laps_to_next_course(self):
        """ Returns number of laps until user can access next course """
        

# Ex
# 70 Agility (blah xp)
# number laps on current course to level up
# number laps to next course