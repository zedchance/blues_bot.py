from fractions import Fraction

from osrsbox import monsters_api, items_api

monsters = monsters_api.load()
items = items_api.load()


def load_monster_from_api(monster):
    loaded_monster = [x for x in monsters if x.name.lower() == monster.lower()]
    if len(loaded_monster) == 0:
        loaded_monster = [x for x in monsters if monster.lower() in x.name.lower()]
    if len(loaded_monster) == 0:
        return False
    return loaded_monster[0]


def parse_monster_drops(drops):
    sorted_drops = []
    for x_drops in drops:
        for x_items in items:
            if x_items.name.lower() == x_drops.name.lower():
                rarity_string = (str(Fraction(x_drops.rarity).limit_denominator())).split('/')
                if len(rarity_string) > 1:
                    rarity_string = f"{rarity_string[0]}/{int(rarity_string[1]):,d}"
                else:
                    rarity_string = "1/1"
                sorted_drops.append({"name": x_drops.name, "rarity_string": rarity_string,
                                     "rarity_int": x_drops.rarity})
                break
    sorted_drops = [i for n, i in enumerate(sorted_drops) if i not in sorted_drops[n + 1:]]
    return sorted(sorted_drops, key=lambda i: i['rarity_int'], reverse=False)
