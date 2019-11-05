# Commonly used URLs

hiscore_url = 'https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal.ws?user1='
wiki_url = 'https://oldschool.runescape.wiki/?search='

ge_url = 'http://services.runescape.com/m=itemdb_oldschool/results?query='
ge_api_url = 'http://services.runescape.com/m=itemdb_oldschool'
ge_api_item_url = ge_api_url + '/api/catalogue/detail.json?item=' # + itemID
ge_graph_url = ge_api_url + '/api/graph/' # + itemID.json

rsbuddy_url = 'https://rsbuddy.com/exchange?search='

cml_url = 'http://crystalmathlabs.com/tracker/track.php?player='
cml_update_url = 'http://crystalmathlabs.com/tracker/update.php?player='
cml_sig = 'http://crystalmathlabs.com/tracker/sig.php?name='

def get_icon_url(skill):
    return f'https://www.runescape.com/img/rsp777/hiscores/skill_icon_{skill}1.gif'

clue_icon = 'https://www.runescape.com/img/rsp777/game_icon_cluescrollsall.png'
bounty_icon = 'https://www.runescape.com/img/rsp777/game_icon_bountyhunterrogue.png'
lms_icon = 'https://www.runescape.com/img/rsp777/game_icon_lmsrank.png'

members_icon = 'http://www.runescape.com/img/rsp777/grand_exchange/members.png'