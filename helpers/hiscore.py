# Used to pull hiscores from OSRS hiscore page

import asyncio
import logging
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from calcs.experience import level_to_xp, xp_to_level, next_level_string

main_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="


class Hiscore:
    """ Pulls hiscores from OSRS hiscore page """

    def __init__(self, username):  # TODO find out where the NoneType object is being called on a bad response
        self.username = username
        if username == '':
            raise MissingUsername(f'You need to enter a username after the command')

    async def fetch(self):
        """ Fetch the results """
        # Event loop
        loop = asyncio.get_event_loop()
        req = loop.run_in_executor(None, requests.get, main_url + self.username)
        response = await req
        if response.status_code == 404:
            raise UserNotFound(f'No hiscore data for {self.username}.')
        elif response.url == 'https://www.runescape.com/unavailable':
            logging.error(f'No response from hiscore page for {self.username} at this time')
            raise HiscoreUnavailable(f'The hiscore page for `{self.username}` is unavailable at this time.')
        doc = BeautifulSoup(response.content, 'html.parser')
        first = [i.split() for i in doc]
        self.scores = [i.split(',') for i in first[0]]

        # Assign levels
        self.overall_rank = int(self.scores[0][0])
        self.overall_level = int(self.scores[0][1])
        self.overall_xp = int(self.scores[0][2])
        self.attack_rank = int(self.scores[1][0])
        self.attack_level = int(self.scores[1][1])
        self.attack_xp = int(self.scores[1][2])
        self.defence_rank = int(self.scores[2][0])
        self.defence_level = int(self.scores[2][1])
        self.defence_xp = int(self.scores[2][2])
        self.strength_rank = int(self.scores[3][0])
        self.strength_level = int(self.scores[3][1])
        self.strength_xp = int(self.scores[3][2])
        self.hitpoints_rank = int(self.scores[4][0])
        self.hitpoints_level = int(self.scores[4][1])
        self.hitpoints_xp = int(self.scores[4][2])
        self.ranged_rank = int(self.scores[5][0])
        self.ranged_level = int(self.scores[5][1])
        self.ranged_xp = int(self.scores[5][2])
        self.prayer_rank = int(self.scores[6][0])
        self.prayer_level = int(self.scores[6][1])
        self.prayer_xp = int(self.scores[6][2])
        self.magic_rank = int(self.scores[7][0])
        self.magic_level = int(self.scores[7][1])
        self.magic_xp = int(self.scores[7][2])
        self.cooking_rank = int(self.scores[8][0])
        self.cooking_level = int(self.scores[8][1])
        self.cooking_xp = int(self.scores[8][2])
        self.woodcutting_rank = int(self.scores[9][0])
        self.woodcutting_level = int(self.scores[9][1])
        self.woodcutting_xp = int(self.scores[9][2])
        self.fletching_rank = int(self.scores[10][0])
        self.fletching_level = int(self.scores[10][1])
        self.fletching_xp = int(self.scores[10][2])
        self.fishing_rank = int(self.scores[11][0])
        self.fishing_level = int(self.scores[11][1])
        self.fishing_xp = int(self.scores[11][2])
        self.firemaking_rank = int(self.scores[12][0])
        self.firemaking_level = int(self.scores[12][1])
        self.firemaking_xp = int(self.scores[12][2])
        self.crafting_rank = int(self.scores[13][0])
        self.crafting_level = int(self.scores[13][1])
        self.crafting_xp = int(self.scores[13][2])
        self.smithing_rank = int(self.scores[14][0])
        self.smithing_level = int(self.scores[14][1])
        self.smithing_xp = int(self.scores[14][2])
        self.mining_rank = int(self.scores[15][0])
        self.mining_level = int(self.scores[15][1])
        self.mining_xp = int(self.scores[15][2])
        self.herblore_rank = int(self.scores[16][0])
        self.herblore_level = int(self.scores[16][1])
        self.herblore_xp = int(self.scores[16][2])
        self.agility_rank = int(self.scores[17][0])
        self.agility_level = int(self.scores[17][1])
        self.agility_xp = int(self.scores[17][2])
        self.thieving_rank = int(self.scores[18][0])
        self.thieving_level = int(self.scores[18][1])
        self.thieving_xp = int(self.scores[18][2])
        self.slayer_rank = int(self.scores[19][0])
        self.slayer_level = int(self.scores[19][1])
        self.slayer_xp = int(self.scores[19][2])
        self.farming_rank = int(self.scores[20][0])
        self.farming_level = int(self.scores[20][1])
        self.farming_xp = int(self.scores[20][2])
        self.runecraft_rank = int(self.scores[21][0])
        self.runecraft_level = int(self.scores[21][1])
        self.runecraft_xp = int(self.scores[21][2])
        self.hunter_rank = int(self.scores[22][0])
        self.hunter_level = int(self.scores[22][1])
        self.hunter_xp = int(self.scores[22][2])
        self.construction_rank = int(self.scores[23][0])
        self.construction_level = int(self.scores[23][1])
        self.construction_xp = int(self.scores[23][2])

        # Build array of levels
        self.levels = []
        self.levels.append(("Attack", self.attack_level, self.attack_xp, self.attack_rank))
        self.levels.append(("Defence", self.defence_level, self.defence_xp, self.defence_rank))
        self.levels.append(("Strength", self.strength_level, self.strength_xp, self.strength_rank))
        self.levels.append(("Hitpoints", self.hitpoints_level, self.hitpoints_xp, self.hitpoints_rank))
        self.levels.append(("Ranged", self.ranged_level, self.ranged_xp, self.ranged_rank))
        self.levels.append(("Prayer", self.prayer_level, self.prayer_xp, self.prayer_rank))
        self.levels.append(("Magic", self.magic_level, self.magic_xp, self.magic_rank))
        self.levels.append(("Cooking", self.cooking_level, self.cooking_xp, self.cooking_rank))
        self.levels.append(("Woodcutting", self.woodcutting_level, self.woodcutting_xp, self.woodcutting_rank))
        self.levels.append(("Fletching", self.fletching_level, self.fletching_xp, self.fletching_rank))
        self.levels.append(("Fishing", self.fishing_level, self.fishing_xp, self.fishing_rank))
        self.levels.append(("Firemaking", self.firemaking_level, self.firemaking_xp, self.firemaking_rank))
        self.levels.append(("Crafting", self.crafting_level, self.crafting_xp, self.crafting_rank))
        self.levels.append(("Smithing", self.smithing_level, self.smithing_xp, self.smithing_rank))
        self.levels.append(("Mining", self.mining_level, self.mining_xp, self.mining_rank))
        self.levels.append(("Herblore", self.herblore_level, self.herblore_xp, self.herblore_rank))
        self.levels.append(("Agility", self.agility_level, self.agility_xp, self.agility_rank))
        self.levels.append(("Thieving", self.thieving_level, self.thieving_xp, self.thieving_rank))
        self.levels.append(("Slayer", self.slayer_level, self.slayer_xp, self.slayer_rank))
        self.levels.append(("Farming", self.farming_level, self.farming_xp, self.farming_rank))
        self.levels.append(("Runecrafting", self.runecraft_level, self.runecraft_xp, self.runecraft_rank))
        self.levels.append(("Hunter", self.hunter_level, self.hunter_xp, self.hunter_rank))
        self.levels.append(("Construction", self.construction_level, self.construction_xp, self.construction_rank))

        # self.scores[24] has been changed to something unkown

        # Assign bounty hunter scores
        self.bounty_hunter_hunter_rank = int(self.scores[25][0])
        self.bounty_hunter_hunter_score = int(self.scores[25][1])
        self.bounty_hunter_rogue_rank = int(self.scores[26][0])
        self.bounty_hunter_rogue_score = int(self.scores[26][1])


        # Assign clue scroll scores
        self.all_clues_rank = int(self.scores[27][0])
        self.all_clues_score = int(self.scores[27][1])
        self.beginner_clues_rank = int(self.scores[28][0])
        self.beginner_clues_score = int(self.scores[28][1])
        self.easy_clues_rank = int(self.scores[29][0])
        self.easy_clues_score = int(self.scores[29][1])
        self.medium_clues_rank = int(self.scores[30][0])
        self.medium_clues_score = int(self.scores[30][1])
        self.hard_clues_rank = int(self.scores[31][0])
        self.hard_clues_score = int(self.scores[31][1])
        self.elite_clues_rank = int(self.scores[32][0])
        self.elite_clues_score = int(self.scores[32][1])
        self.master_clues_rank = int(self.scores[33][0])
        self.master_clues_score = int(self.scores[33][1])

        # Assign LMS scores
        self.lms_rank = int(self.scores[34][0])
        self.lms_score = int(self.scores[34][1])

        # Assign boss kill counts
        self.kc_abyssal_sire = int(self.scores[36][1])
        self.kc_abyssal_sire_rank = int(self.scores[36][0])
        self.kc_alchemical_hydra = int(self.scores[37][1])
        self.kc_alchemical_hydra_rank = int(self.scores[37][0])
        self.kc_barrows_chest = int(self.scores[38][1])
        self.kc_barrows_chest_rank = int(self.scores[38][0])
        self.kc_bryophyta = int(self.scores[39][1])
        self.kc_bryophyta_rank = int(self.scores[39][0])
        self.kc_callisto = int(self.scores[40][1])
        self.kc_callisto_rank = int(self.scores[40][0])
        self.kc_cerberus = int(self.scores[41][1])
        self.kc_cerberus_rank = int(self.scores[41][0])
        self.kc_chambers_of_xeric = int(self.scores[42][1])
        self.kc_chambers_of_xeric_rank = int(self.scores[42][0])
        self.kc_chambers_of_xeric_challenge = int(self.scores[43][1])
        self.kc_chambers_of_xeric_challenge_rank = int(self.scores[43][0])
        self.kc_chaos_elemental = int(self.scores[44][1])
        self.kc_chaos_elemental_rank = int(self.scores[44][0])
        self.kc_chaos_fanatic = int(self.scores[45][1])
        self.kc_chaos_fanatic_rank = int(self.scores[45][0])
        self.kc_commander_zilyana = int(self.scores[46][1])
        self.kc_commander_zilyana_rank = int(self.scores[46][0])
        self.kc_corporeal_beast = int(self.scores[47][1])
        self.kc_corporeal_beast_rank = int(self.scores[47][0])
        self.kc_crazy_archaeologist = int(self.scores[48][1])
        self.kc_crazy_archaeologist_rank = int(self.scores[48][0])
        self.kc_dagannoth_prime = int(self.scores[49][1])
        self.kc_dagannoth_prime_rank = int(self.scores[49][0])
        self.kc_dagannoth_rex = int(self.scores[50][1])
        self.kc_dagannoth_rex_rank = int(self.scores[50][0])
        self.kc_dagannoth_supreme = int(self.scores[51][1])
        self.kc_dagannoth_supreme_rank = int(self.scores[51][0])
        self.kc_deranged_archaeologist = int(self.scores[52][1])
        self.kc_deranged_archaeologist_rank = int(self.scores[52][0])
        self.kc_general_graardor = int(self.scores[53][1])
        self.kc_general_graardor_rank = int(self.scores[53][0])
        self.kc_giant_mole = int(self.scores[54][1])
        self.kc_giant_mole_rank = int(self.scores[54][0])
        self.kc_grotesque_guardians = int(self.scores[55][1])
        self.kc_grotesque_guardians_rank = int(self.scores[55][0])
        self.kc_hespori = int(self.scores[56][1])
        self.kc_hespori_rank = int(self.scores[56][0])
        self.kc_kalphite_queen = int(self.scores[57][1])
        self.kc_kalphite_queen_rank = int(self.scores[57][0])
        self.kc_king_black_dragon = int(self.scores[58][1])
        self.kc_king_black_dragon_rank = int(self.scores[58][0])
        self.kc_kraken = int(self.scores[59][1])
        self.kc_kraken_rank = int(self.scores[59][0])
        self.kc_kreearra = int(self.scores[60][1])
        self.kc_kreearra_rank = int(self.scores[60][0])
        self.kc_kril_tsutsaroth = int(self.scores[61][1])
        self.kc_kril_tsutsaroth_rank = int(self.scores[61][0])
        self.kc_mimic = int(self.scores[62][1])
        self.kc_mimic_rank = int(self.scores[62][0])
        self.nightmare = int(self.scores[63][0])
        self.nightmare_rank = int(self.scores[63][1])
        self.phosanis_nightmare = int(self.scores[64][0])
        self.phosanis_nightmare_rank = int(self.scores[64][1])
        self.kc_obor = int(self.scores[65][1])
        self.kc_obor_rank = int(self.scores[65][0])
        self.kc_sarachnis = int(self.scores[66][1])
        self.kc_sarachnis_rank = int(self.scores[66][0])
        self.kc_scorpia = int(self.scores[67][1])
        self.kc_scorpia_rank = int(self.scores[67][0])
        self.kc_skotizo = int(self.scores[68][1])
        self.kc_skotizo_rank = int(self.scores[68][0])
        self.kc_tempoross = int(self.scores[69][1])
        self.kc_tempoross_rank = int(self.scores[69][0])
        self.kc_the_gauntlet = int(self.scores[70][1])
        self.kc_the_gauntlet_rank = int(self.scores[70][0])
        self.kc_the_corrupted_gauntlet = int(self.scores[71][1])
        self.kc_the_corrupted_gauntlet_rank = int(self.scores[71][0])
        self.kc_theatre_of_blood = int(self.scores[72][1])
        self.kc_theatre_of_blood_rank = int(self.scores[72][0])
        self.kc_theatre_of_blood_hard_mode_rank = int(self.scores[73][0])
        self.kc_theatre_of_blood_hard_mode = int(self.scores[73][1])
        self.kc_thermonuclear_smoke_devil = int(self.scores[74][1])
        self.kc_thermonuclear_smoke_devil_rank = int(self.scores[74][0])
        self.kc_tzkal_zuk = int(self.scores[75][1])
        self.kc_tzkal_zuk_rank = int(self.scores[75][0])
        self.kc_tztok_jad = int(self.scores[76][1])
        self.kc_tztok_jad_rank = int(self.scores[76][0])
        self.kc_venenatis = int(self.scores[77][1])
        self.kc_venenatis_rank = int(self.scores[77][0])
        self.kc_vetion = int(self.scores[78][1])
        self.kc_vetion_rank = int(self.scores[78][0])
        self.kc_vorkath = int(self.scores[79][1])
        self.kc_vorkath_rank = int(self.scores[79][0])
        self.kc_wintertodt = int(self.scores[80][1])
        self.kc_wintertodt_rank = int(self.scores[80][0])
        self.kc_zalcano = int(self.scores[81][1])
        self.kc_zalcano_rank = int(self.scores[81][0])
        self.kc_zulrah = int(self.scores[82][1])
        self.kc_zulrah_rank = int(self.scores[82][0])

        # Build array of kc
        self.kcs = []
        self.kcs.append(("Abyssal Sire", self.kc_abyssal_sire, self.kc_abyssal_sire_rank))
        self.kcs.append(("Alchemical Hydra", self.kc_alchemical_hydra, self.kc_alchemical_hydra_rank))
        self.kcs.append(("Barrows Chest", self.kc_barrows_chest, self.kc_barrows_chest_rank))
        self.kcs.append(("Bryophyta", self.kc_bryophyta, self.kc_bryophyta_rank))
        self.kcs.append(("Callisto", self.kc_callisto, self.kc_callisto_rank))
        self.kcs.append(("Cerberus", self.kc_cerberus, self.kc_cerberus_rank))
        self.kcs.append(("Chambers of Xeric", self.kc_chambers_of_xeric, self.kc_chambers_of_xeric_rank))
        self.kcs.append(("Chambers of Xeric: Challenge Mode", self.kc_chambers_of_xeric_challenge, self.kc_chambers_of_xeric_challenge_rank))
        self.kcs.append(("Chaos Elemental", self.kc_chaos_elemental, self.kc_chaos_elemental_rank))
        self.kcs.append(("Chaos Fanatic", self.kc_chaos_fanatic, self.kc_chaos_fanatic_rank))
        self.kcs.append(("Commander Zilyana", self.kc_commander_zilyana, self.kc_commander_zilyana_rank))
        self.kcs.append(("Corporeal Beast", self.kc_corporeal_beast, self.kc_corporeal_beast_rank))
        self.kcs.append(("Crazy Archaeologist", self.kc_crazy_archaeologist, self.kc_crazy_archaeologist_rank))
        self.kcs.append(("Dagannoth Prime", self.kc_dagannoth_prime, self.kc_dagannoth_prime_rank))
        self.kcs.append(("Dagannoth Rex", self.kc_dagannoth_rex, self.kc_dagannoth_rex_rank))
        self.kcs.append(("Dagannoth Supreme", self.kc_dagannoth_supreme, self.kc_dagannoth_supreme_rank))
        self.kcs.append(("Deranged Archaeologist", self.kc_deranged_archaeologist, self.kc_deranged_archaeologist_rank))
        self.kcs.append(("General Graardor", self.kc_general_graardor, self.kc_general_graardor_rank))
        self.kcs.append(("Giant Mole", self.kc_giant_mole, self.kc_giant_mole_rank))
        self.kcs.append(("Grotesque Guardians", self.kc_grotesque_guardians, self.kc_grotesque_guardians_rank))
        self.kcs.append(("Hespori", self.kc_hespori, self.kc_hespori_rank))
        self.kcs.append(("Kalphite Queen", self.kc_kalphite_queen, self.kc_kalphite_queen_rank))
        self.kcs.append(("King Black Dragon", self.kc_king_black_dragon, self.kc_king_black_dragon_rank))
        self.kcs.append(("Kraken", self.kc_kraken, self.kc_kraken_rank))
        self.kcs.append(("Kree'Arra", self.kc_kreearra, self.kc_kreearra_rank))
        self.kcs.append(("K'ril Tsutsaroth", self.kc_kril_tsutsaroth, self.kc_kril_tsutsaroth_rank))
        self.kcs.append(("Mimic", self.kc_mimic, self.kc_mimic_rank))
        self.kcs.append(("Obor", self.kc_obor, self.kc_obor_rank))
        self.kcs.append(("Sarachnis", self.kc_sarachnis, self.kc_sarachnis_rank))
        self.kcs.append(("Scorpia", self.kc_scorpia, self.kc_scorpia_rank))
        self.kcs.append(("Skotizo", self.kc_skotizo, self.kc_skotizo_rank))
        self.kcs.append(("Tempoross", self.kc_tempoross, self.kc_tempoross_rank))
        self.kcs.append(("The Gauntlet", self.kc_the_gauntlet, self.kc_the_gauntlet_rank))
        self.kcs.append(("The Corrupted Gauntlet", self.kc_the_corrupted_gauntlet, self.kc_the_corrupted_gauntlet_rank))
        self.kcs.append(("Theatre of Blood", self.kc_theatre_of_blood, self.kc_theatre_of_blood_rank))
        self.kcs.append(("Theatre of Blood Hard Mode", self.kc_theatre_of_blood_hard_mode, self.kc_theatre_of_blood_hard_mode_rank))
        self.kcs.append(("Thermonuclear Smoke Devil", self.kc_thermonuclear_smoke_devil, self.kc_thermonuclear_smoke_devil_rank))
        self.kcs.append(("TzKal-Zuk", self.kc_tzkal_zuk, self.kc_tzkal_zuk_rank))
        self.kcs.append(("TzTok-Jad", self.kc_tztok_jad, self.kc_tztok_jad_rank))
        self.kcs.append(("Venenatis", self.kc_venenatis, self.kc_venenatis_rank))
        self.kcs.append(("Vet'ion", self.kc_vetion, self.kc_vetion_rank))
        self.kcs.append(("Vorkath", self.kc_vorkath, self.kc_vorkath_rank))
        self.kcs.append(("Wintertodt", self.kc_wintertodt, self.kc_wintertodt_rank))
        self.kcs.append(("Zalcano", self.kc_zalcano, self.kc_zalcano_rank))
        self.kcs.append(("Zulrah", self.kc_zulrah, self.kc_zulrah_rank))

    def level_lookup(self, skill):
        for (name, level, xp, rank) in self.levels:
            if name == skill:
                return level
        return None

    def generate_clue_table(self):
        """ Returns a formatted table of clue scroll scores """
        if self.all_clues_rank == -1:
            return None
        results = []
        if self.beginner_clues_rank != -1:
           results.append((self.beginner_clues_score, 'Beginner'))
        if self.easy_clues_rank != -1:
            results.append((self.easy_clues_score, 'Easy'))
        if self.medium_clues_rank != -1:
            results.append((self.medium_clues_score, 'Medium'))
        if self.hard_clues_rank != -1:
            results.append((self.hard_clues_score, 'Hard'))
        if self.elite_clues_rank != -1:
            results.append((self.elite_clues_score, 'Elite'))
        if self.master_clues_rank != -1:
            results.append((self.master_clues_score, 'Master'))
        return tabulate(results, tablefmt='plain')

    def generate_kc_table(self):
        """ Returns a formatted table of kill counts """
        results = []
        for (name, kc, rank) in self.kcs:
            if int(kc) > -1:
                results.append((kc, name))
        if len(results) == 0:
            return None
        return tabulate(results, tablefmt='plain')

    def generate_99_table(self):
        """ Returns the number of 99s and a formatted table of level 99s """
        results = []
        count = 0
        for (name, level, xp, rank) in self.levels:
            if int(level) == 99:
                results.append((name, f'{int(xp) / 1000000:.1f}M xp'))
                count += 1
        if count == 0:
            return count, None
        return count, tabulate(results, tablefmt='plain')

    def generate_hiscore_table(self):
        """ Returns a formatted table of all hiscore info """
        results = []
        for (name, level, xp, rank) in self.levels:
            results.append((level, name))
        return tabulate(results, tablefmt='plain')

    def generate_combat_table(self):
        """ Returns a formatted table of all combat info """
        results = []
        results.append((self.attack_level, 'Attack'))
        results.append((self.defence_level, 'Defence'))
        results.append((self.strength_level, 'Strength'))
        results.append((self.prayer_level, 'Prayer'))
        results.append((self.magic_level, 'Magic'))
        results.append((self.ranged_level, 'Ranged'))
        return tabulate(results, tablefmt='plain')

    def closest_level_up(self):
        """ Returns a string of the skill closest to level up """
        ret = ""
        compare = 200000000
        ret_name = ""
        ret_xp = 0
        for (name, lvl, xp, rank) in self.levels:
            xp_needed = level_to_xp(xp_to_level(xp) + 1) - xp
            if xp_needed < compare:
                compare = xp_needed
                ret_name = name
                ret_xp = xp
        return next_level_string(ret_xp, ret_name)


class UserNotFound(TypeError):
    pass


class MissingUsername(Exception):
    pass


class HiscoreUnavailable(Exception):
    pass

# Test code
# bluetrane = Hiscore("bluetrane")
# print("Overall rank:", bluetrane.overall_rank)
# print("Overall level:", bluetrane.overall_level)
# print("Overall xp:", bluetrane.overall_xp)
# print("Slayer level:", bluetrane.slayer_level)
# print("Runecraft level:", bluetrane.runecraft_level)
# print("Medium clue scrolls", bluetrane.medium_clues_score)
# print("LMS rank:", bluetrane.lms_rank)
