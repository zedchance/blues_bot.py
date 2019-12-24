from calcs.experience import LEVEL_99, xp_to_next_level
from helpers.hiscore import Hiscore

class Wintertodt(Hiscore):
    """ Used to calculate information about Wintertodt """

    # Average xp per kill
    def average(self):
        return int(self.firemaking_xp) // int(self.kc_wintertodt)

    # Estimated kills until level up
    def kills_to_level_up(self):
        remaining = xp_to_next_level(int(self.firemaking_level))
        return remaining // self.average()

    # Estimated kills remaining until level 99
    def kills_to_level_99(self):
        return (LEVEL_99 - int(self.firemaking_xp)) // self.average()

    # Estimate total kills
    def estimated_total_kills(self):
        return int(self.kc_wintertodt) + self.kills_to_level_99()