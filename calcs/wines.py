# Wine calculator for cooking

from calcs.experience import LEVEL_99
from helpers.hiscore import Hiscore

WINE_XP = 200
WINE_XP_PER_INV = WINE_XP * 14


class Wines(Hiscore):
    """ Wine cooking calculator """

    def wines_to_level_99(self):
        """ Returns the amount of wines needed to reach level 99 cooking """
        return (LEVEL_99 - self.cooking_xp) // WINE_XP

    def invs_to_level_99(self):
        """ Returns number of inventories to reach 99 cooking """
        return (LEVEL_99 - self.cooking_xp) // WINE_XP_PER_INV

    def wines_to_200m(self):
        """ Returns number of wines to reach 200m xp """
        return (200000000 - self.cooking_xp) // WINE_XP

    def invs_to_200m(self):
        """ Returns number of wines to reach 200m xp """
        return (200000000 - self.cooking_xp) // WINE_XP_PER_INV
