# Used to pull hiscores from OSRS hiscore page

import requests
from bs4 import BeautifulSoup

main_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

class Hiscore:
    """ Pulls hiscores from OSRS hiscore page """

    def __init__(self, username):
        # Pull hiscores
        if username == '':
            raise MissingUsername(f'You need to enter a username after the command')
        session = requests.session()
        req = session.get(main_url + username)
        if req.status_code == 404:
            raise UserNotFound(f'No hiscore data for {username}.')
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

        # Build array of level 99s
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

        # Assign boss kill counts
        self.kc_abyssal_sire = self.scores[35][1]
        self.kc_abyssal_sire_rank = self.scores[35][0]
        self.kc_alchemical_hydra = self.scores[36][1]
        self.kc_alchemical_hydra_rank = self.scores[36][0]
        self.kc_barrows_chest = self.scores[37][1]
        self.kc_barrows_chest_rank = self.scores[37][0]
        self.kc_bryophyta = self.scores[37][1]
        self.kc_bryophyta_rank = self.scores[37][0]
        # self.kc_callisto = self.scores[38][1]
        # self.kc_callisto_rank = self.scores[38][0]
        # self.kc_cerberus = self.scores[39][1]
        # self.kc_cerberus_rank = self.scores[39][0]
        self.kc_chambers_of_xeric = self.scores[39][1]
        self.kc_chambers_of_xeric_rank = self.scores[39][0]
        self.kc_chambers_of_xeric_challenge = self.scores[40][1]
        self.kc_chambers_of_xeric_challenge_rank = self.scores[40][0]
        self.kc_chaos_elemental = self.scores[41][1]
        self.kc_chaos_elemental_rank = self.scores[41][0]
        self.kc_chaos_fanatic = self.scores[42][1]
        self.kc_chaos_fanatic_rank = self.scores[42][0]
        self.kc_commander_zilyana = self.scores[43][1]
        self.kc_commander_zilyana_rank = self.scores[43][0]
        self.kc_corporeal_beast = self.scores[44][1]
        self.kc_corporeal_beast_rank = self.scores[44][0]
        self.kc_crazy_archaeologist = self.scores[45][1]
        self.kc_crazy_archaeologist_rank = self.scores[45][0]
        self.kc_dagannoth_prime = self.scores[46][1]
        self.kc_dagannoth_prime_rank = self.scores[46][0]
        self.kc_dagannoth_rex = self.scores[47][1]
        self.kc_dagannoth_rex_rank = self.scores[47][0]
        self.kc_dagannoth_supreme = self.scores[48][1]
        self.kc_dagannoth_supreme_rank = self.scores[48][0]
        self.kc_deranged_archaeologist = self.scores[49][1]
        self.kc_deranged_archaeologist_rank = self.scores[49][0]
        self.kc_general_graardor = self.scores[50][1]
        self.kc_general_graardor_rank = self.scores[50][0]
        self.kc_giant_mole = self.scores[51][1]
        self.kc_giant_mole_rank = self.scores[51][0]
        self.kc_grotesque_guardians = self.scores[52][1]
        self.kc_grotesque_guardians_rank = self.scores[52][0]
        self.kc_hespori = self.scores[53][1]
        self.kc_hespori_rank = self.scores[53][0]
        self.kc_kalphite_queen = self.scores[54][1]
        self.kc_kalphite_queen_rank = self.scores[54][0]
        self.kc_king_black_dragon = self.scores[55][1]
        self.kc_king_black_dragon_rank = self.scores[55][0]
        self.kc_kraken = self.scores[56][1]
        self.kc_kraken_rank = self.scores[56][0]
        self.kc_kreearra = self.scores[57][1]
        self.kc_kreearra_rank = self.scores[57][0]
        self.kc_kril_tsutsaroth = self.scores[58][1]
        self.kc_kril_tsutsaroth_rank = self.scores[58][0]
        self.kc_mimic = self.scores[59][1]
        self.kc_mimic_rank = self.scores[59][0]
        self.kc_obor = self.scores[60][1]
        self.kc_obor_rank = self.scores[60][0]
        self.kc_sarachnis = self.scores[61][1]
        self.kc_sarachnis_rank = self.scores[61][0]
        self.kc_scorpia = self.scores[62][1]
        self.kc_scorpia_rank = self.scores[62][0]
        self.kc_skotizo = self.scores[63][1]
        self.kc_skotizo_rank = self.scores[63][0]
        self.kc_the_gauntlet = self.scores[64][1]
        self.kc_the_gauntlet_rank = self.scores[64][0]
        self.kc_the_corrupted_gauntlet = self.scores[65][1]
        self.kc_the_corrupted_gauntlet_rank = self.scores[65][0]
        self.kc_theatre_of_blood = self.scores[66][1]
        self.kc_theatre_of_blood_rank = self.scores[66][0]
        self.kc_thermonuclear_smoke_devil = self.scores[67][1]
        self.kc_thermonuclear_smoke_devil_rank = self.scores[67][0]
        self.kc_tzkal_zuk = self.scores[68][1]
        self.kc_tzkal_zuk_rank = self.scores[68][0]
        self.kc_tztok_jad = self.scores[69][1]
        self.kc_tztok_jad_rank = self.scores[69][0]
        self.kc_venenatis = self.scores[70][1]
        self.kc_venenatis_rank = self.scores[70][0]
        self.kc_vetion = self.scores[71][1]
        self.kc_vetion_rank = self.scores[71][0]
        self.kc_vorkath = self.scores[72][1]
        self.kc_vorkath_rank = self.scores[72][0]
        self.kc_wintertodt = self.scores[73][1]
        self.kc_wintertodt_rank = self.scores[73][0]
        self.kc_zalcano = self.scores[74][1]
        self.kc_zalcano_rank = self.scores[74][0]
        self.kc_zulrah = self.scores[75][1]
        self.kc_zulrah_rank = self.scores[75][0]

        # Build array of kc
        self.kcs = []
        self.kcs.append(("Abyssal Sire", self.kc_abyssal_sire, self.kc_abyssal_sire_rank))
        self.kcs.append(("Alchemical Hydra", self.kc_alchemical_hydra, self.kc_alchemical_hydra_rank))
        self.kcs.append(("Barrows Chest", self.kc_barrows_chest, self.kc_barrows_chest_rank))
        self.kcs.append(("Bryophyta", self.kc_bryophyta, self.kc_bryophyta_rank))
        # self.kcs.append(("Callisto", self.kc_callisto, self.kc_callisto_rank))
        # self.kcs.append(("Cerberus", self.kc_cerberus, self.kc_cerberus_rank))
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
        self.kcs.append(("The Gauntlet", self.kc_the_gauntlet, self.kc_the_gauntlet_rank))
        self.kcs.append(("The Corrupted Gauntlet", self.kc_the_corrupted_gauntlet, self.kc_the_corrupted_gauntlet_rank))
        self.kcs.append(("Theatre of Blood", self.kc_theatre_of_blood, self.kc_theatre_of_blood_rank))
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
            if (name == skill):
                return level
        return None

class UserNotFound(TypeError):
    pass

class MissingUsername(Exception):
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