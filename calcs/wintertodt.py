from calcs.experience import LEVEL_99, xp_to_next_level, level_to_xp
from helpers.hiscore import Hiscore

class Wintertodt(Hiscore):
    """ Used to calculate information about Wintertodt """

    # Average xp per kill
    def average(self):
        return self.firemaking_xp // self.kc_wintertodt

    # Estimated kills until level up
    def kills_to_level_up(self):
        remaining = (level_to_xp(self.firemaking_level + 1)) - self.firemaking_xp
        return remaining // self.average()

    # Estimated kills remaining until level 99
    def kills_to_level_99(self):
        return (LEVEL_99 - self.firemaking_xp) // self.average()

    # Estimate total kills
    def estimated_total_kills(self):
        return self.kc_wintertodt + self.kills_to_level_99()