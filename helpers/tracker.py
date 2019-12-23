# Crystal Math Labs xp tracker

import requests
from bs4 import BeautifulSoup

from helpers.urls import cml_track, cml_update_url, cml_sig, cml_url, cml_boss_url


class Tracker:
    """ Crystal Math Labs xp tracking class """

    def __init__(self, username):
        self.username = username
        session = requests.session()
        # Update results if able
        update = session.get(cml_update_url + username)
        # Get username's page
        req = session.get(cml_url + username)
        if req.status_code == 404:
            raise UserNotFound(f'No data for {username}.')
        doc = BeautifulSoup(req.content, 'html.parser')

        # Put results in an array of tuples
        # (Skill name, XP gained, Rank change, Levels gained, EHP)
        response = doc.find_all('tr')
        self.results = []
        for i in response[1:-1]:
            # Parse
            name = i.a.text
            search = i.find_all('td')
            no_commas = search[1].text.replace(',', '')
            no_plus = no_commas.replace('+', '')
            xp_gained = int(no_plus)
            rank_change = search[2].text
            levels_gained = search[3].text
            ehp = search[4].text
            # record = search[5].text
            # Store results
            self.results.append((name, xp_gained, rank_change, levels_gained, ehp))

        # Sort results by xp gained (seconds item in tuple)
        # https://stackoverflow.com/a/3121985
        self.top_gains = sorted(self.results, key=lambda tup: tup[1], reverse=True)
        for (name, xp, rank, levels, ehp) in self.top_gains:
            if name == 'Overall':
                if xp == 0:
                    raise NoDataPoints(f'Either this is the first time {username} has been tracked this week, '
                                       f'or no XP has been gained.\n'
                                       'Gain some more XP and try again.\n'
                                       '(This command is more useful if you use it often.)')

        # Extract last changed time
        details_response = doc.find_all('div', {"id": "track_details"})
        details_search = details_response[0].find_all('span')
        self.results_duration = details_search[0].text
        self.oldest_data = details_search[2].text
        self.last_checked = details_search[6].text
        self.last_changed = details_search[8].text

        # Get latest boss kills
        req = session.get(cml_boss_url + username)
        doc = BeautifulSoup(req.content, 'html.parser')
        boss_response = doc.find_all('tr')
        self.boss_kills = []
        for i in boss_response[1:-1]:
            name = i.a.text
            boss_search = i.find_all('td')
            no_commas = boss_search[1].text.replace(',', '')
            no_plus = no_commas.replace('+', '')
            kills = int(no_plus)
            rank = boss_search[2].text
            self.boss_kills.append((name, kills, rank))

        # Sort boss kills array
        self.top_kills = sorted(self.boss_kills, key=lambda tup: tup[1], reverse=True)

    def get_sig(self):
        return f'{cml_sig}{self.username}'

class UserNotFound(TypeError):
    pass

class NoDataPoints(Exception):
    pass