# Commonly used URLs

# Hiscore and wiki
hiscore_url = 'https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal.ws?user1='
wiki_url = 'https://oldschool.runescape.wiki/?search='

# News RSS feed
news_rss_feed = 'https://secure.runescape.com/m=news/latest_news.rss?oldschool=true'

# Grand exchange
ge_url = 'http://services.runescape.com/m=itemdb_oldschool/results?query='
ge_api_url = 'http://services.runescape.com/m=itemdb_oldschool'
ge_api_item_url = ge_api_url + '/api/catalogue/detail.json?item=' # + itemID
ge_graph_url = ge_api_url + '/api/graph/' # + itemID.json

# Rsbuddy exchange
rsbuddy_url = 'https://rsbuddy.com/exchange?search='

# Crystal math labs xp tracker
cml_url = 'http://crystalmathlabs.com/tracker/track.php?player='
cml_update_url = 'http://crystalmathlabs.com/tracker/update.php?player='
cml_boss_url = 'https://crystalmathlabs.com/tracker/bosstrack.php?player='
cml_sig = 'http://crystalmathlabs.com/tracker/sig.php?name='
cml_logo = 'https://crystalmathlabs.com/tracker/images/logo.png'

def cml_track(username, duration):
    return f'https://crystalmathlabs.com/tracker/api.php?type=track&player={username}&time={duration}'

# Icons
clue_icon = 'https://www.runescape.com/img/rsp777/game_icon_cluescrollsall.png'
bounty_icon = 'https://www.runescape.com/img/rsp777/game_icon_bountyhunterrogue.png'
lms_icon = 'https://www.runescape.com/img/rsp777/game_icon_lmsrank.png'
members_icon = 'http://www.runescape.com/img/rsp777/grand_exchange/members.png'
news_icon = 'https://cdn.runescape.com/assets/img/external/oldschool/2019/newsposts/2019-12-16/summary_3.png'

def get_icon_url(skill):
    return f'https://www.runescape.com/img/rsp777/hiscores/skill_icon_{skill}1.gif'