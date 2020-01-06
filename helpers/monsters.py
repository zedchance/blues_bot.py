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
                if x_items.cost >= 0:
                    sorted_drops.append({"name": x_drops.name, "value": x_items.cost})
                    break
                else:
                    sorted_drops.append({"name": x_drops.name, "value": 0})
                    break
    return sorted(sorted_drops, key=lambda i: i['value'], reverse=True)
