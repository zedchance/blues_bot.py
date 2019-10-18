# Calculates experience
from math import floor

def xp_to_next_level(level):
    return floor((level - 1) + 300 * (2 ** ((level - 1) / 7))) / 4

def level_to_xp(level):
    xp = 0
    for i in range(2, level + 1):
        xp += xp_to_next_level(i)
    return xp

# Test code
# test_level = 50
# print("XP to level", test_level + 1, xp_to_next_level(test_level))
# print("Total xp at level", test_level, level_to_xp(test_level))