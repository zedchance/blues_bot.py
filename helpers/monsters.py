from fractions import Fraction

from osrsbox import monsters_api, items_api

monsters = monsters_api.load()
items = items_api.load()


def load_monster_from_api(monster):
    for x in monsters:
        if x.name.lower() == monster:
            return x
    return False


def parse_monster_drops(drops):
    sorted_drops = []
    for x_drops in drops:
        for x_items in items:
            if x_items.name.lower() == x_drops.name.lower():
                sorted_drops.append({"name": x_drops.name, "rarity_string": Fraction(x_drops.rarity).limit_denominator(),
                                     "rarity_int": x_drops.rarity})
                break
    sorted_drops = [i for n, i in enumerate(sorted_drops) if i not in sorted_drops[n + 1:]]
    return sorted(sorted_drops, key=lambda i: i['rarity_int'], reverse=False)
