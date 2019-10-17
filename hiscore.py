# Used to pull hiscores from OSRS hiscore page

import requests
from bs4 import BeautifulSoup

main_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

class Hiscore:
    """ Pulls hiscores from OSRS hiscore page """

    def __init__(self, username):
        # Pull hiscores
        session = requests.session()
        req = session.get(main_url + username)
        doc = BeautifulSoup(req.content, 'html.parser')
        first = [i.split() for i in doc]
        self.scores = [i.split(',') for i in first[0]]

        # Assign levels
        self.overall_rank = self.scores[0][0]
        self.overall_level = self.scores[0][1]
        self.overall_xp = self.scores[0][2]
        self.attack_rank = self.scores[1][0]
        self.attack_level = self.scores[1][1]
        self.attack_xp = self.scores[1][2]
        self.defence_rank = self.scores[2][0]
        self.defence_level = self.scores[2][1]
        self.defence_xp = self.scores[2][2]
        self.strength_rank = self.scores[3][0]
        self.strength_level = self.scores[3][1]
        self.strength_xp = self.scores[3][2]
        self.hitpoints_rank = self.scores[4][0]
        self.hitpoints_level = self.scores[4][1]
        self.hitpoints_xp = self.scores[4][2]
        self.ranged_rank = self.scores[5][0]
        self.ranged_level = self.scores[5][1]
        self.ranged_xp = self.scores[5][2]
        self.prayer_rank = self.scores[6][0]
        self.prayer_level = self.scores[6][1]
        self.prayer_xp = self.scores[6][2]
        self.magic_rank = self.scores[7][0]
        self.magic_level = self.scores[7][1]
        self.magic_xp = self.scores[7][2]
        self.cooking_rank = self.scores[8][0]
        self.cooking_level = self.scores[8][1]
        self.cooking_xp = self.scores[8][2]
        self.woodcutting_rank = self.scores[9][0]
        self.woodcutting_level = self.scores[9][1]
        self.woodcutting_xp = self.scores[9][2]
        self.fletching_rank = self.scores[10][0]
        self.fletching_level = self.scores[10][1]
        self.fletching_xp = self.scores[10][2]
        self.fishing_rank = self.scores[11][0]
        self.fishing_level = self.scores[11][1]
        self.fishing_xp = self.scores[11][2]
        self.firemaking_rank = self.scores[12][0]
        self.firemaking_level = self.scores[12][1]
        self.firemaking_xp = self.scores[12][2]
        self.crafting_rank = self.scores[13][0]
        self.crafting_level = self.scores[13][1]
        self.crafting_xp = self.scores[13][2]
        self.smithing_rank = self.scores[14][0]
        self.smithing_level = self.scores[14][1]
        self.smithing_xp = self.scores[14][2]
        self.mining_rank = self.scores[15][0]
        self.mining_level = self.scores[15][1]
        self.mining_xp = self.scores[15][2]
        self.herblore_rank = self.scores[16][0]
        self.herblore_level = self.scores[16][1]
        self.herblore_xp = self.scores[16][2]
        self.agility_rank = self.scores[17][0]
        self.agility_level = self.scores[17][1]
        self.agility_xp = self.scores[17][2]
        self.thieving_rank = self.scores[18][0]
        self.thieving_level = self.scores[18][1]
        self.thieving_xp = self.scores[18][2]
        self.slayer_rank = self.scores[19][0]
        self.slayer_level = self.scores[19][1]
        self.slayer_xp = self.scores[19][2]
        self.farming_rank = self.scores[20][0]
        self.farming_level = self.scores[20][1]
        self.farming_xp = self.scores[20][2]
        self.runecraft_rank = self.scores[21][0]
        self.runecraft_level = self.scores[21][1]
        self.runecraft_xp = self.scores[21][2]
        self.hunter_rank = self.scores[22][0]
        self.hunter_level = self.scores[22][1]
        self.hunter_xp = self.scores[22][2]
        self.construction_rank = self.scores[23][0]
        self.construction_level = self.scores[23][1]
        self.construction_xp = self.scores[23][2]

        # Assign mini-game scores
        self.bounty_hunter_hunter_rank = self.scores[24][0]
        self.bounty_hunter_hunter_score = self.scores[24][1]
        self.bounty_hunter_rogue_rank = self.scores[25][0]
        self.bounty_hunter_rogue_score = self.scores[25][1]
        self.lms_rank = self.scores[26][0]
        self.lms_score = self.scores[26][1]

        # Assign clue scroll scores
        self.all_clues_rank = self.scores[27][0]
        self.all_clues_score = self.scores[27][1]
        self.beginner_clues_rank = self.scores[28][0]
        self.beginner_clues_score = self.scores[28][1]
        self.easy_clues_rank = self.scores[29][0]
        self.easy_clues_score = self.scores[29][1]
        self.medium_clues_rank = self.scores[30][0]
        self.medium_clues_score = self.scores[30][1]
        self.hard_clues_rank = self.scores[31][0]
        self.hard_clues_score = self.scores[31][1]
        self.elite_clues_rank = self.scores[32][0]
        self.elite_clues_score = self.scores[32][1]
        self.master_clues_rank = self.scores[33][0]
        self.master_clues_score = self.scores[33][1]


# Test code
# bluetrane = Hiscore("bluetrane")
# print("Overall rank:", bluetrane.overall_rank)
# print("Overall level:", bluetrane.overall_level)
# print("Overall xp:", bluetrane.overall_xp)
# print("Slayer level:", bluetrane.slayer_level)
# print("Runecraft level:", bluetrane.runecraft_level)
# print("Medium clue scrolls", bluetrane.medium_clues_score)
# print("LMS rank:", bluetrane.lms_rank)