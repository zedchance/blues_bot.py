# Calculates experience
from math import floor

LEVEL_99 = 13034431


def xp_to_next_level(level):
    """ Returns xp to next level up """
    if level == 120:
        return 0
    return floor((level - 1) + 300 * (2 ** ((level - 1) / 7))) / 4


def level_to_xp(level):
    """ Converts level number to xp, handles virtual levels"""
    xp = 0
    if level >= 120:
        return 200000000
    for i in range(2, level + 1):
        xp += xp_to_next_level(i)
    return xp


def xp_to_level(xp):
    """ Converts xp to level number, handles virtual levels """
    level = 1
    if xp >= 200000000:
        return 120
    elif xp == -1:
        return level
    while xp >= level_to_xp(level):
        level += 1
    return level - 1


def next_level_string(xp, skill):
    """ Returns string representation of next level of skill, takes into account virtual levels """
    level = xp_to_level(xp)
    next_level = level + 1
    next_xp = level_to_xp(next_level) - xp
    if xp == 200000000:
        return "Maxed!"
    if xp > LEVEL_99:
        skill = f'{skill} (virtual level)'
    else:
        skill = f'{skill}'
    return f'{next_xp:,.0f} xp to {next_level} {skill}'

# Test code
# test_level = 40
# print("XP to level", test_level + 1, xp_to_next_level(test_level))
# print("Total xp at level", test_level, level_to_xp(test_level))

# test_xp = 14000000
# print(next_level_string(test_xp, "Attack"))
# print("Level to XP", level_to_xp(101))
# print("XP to level", xp_to_level(16000000))
