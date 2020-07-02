# Crystal Math Labs xp tracker

import asyncio
import logging
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

cml_url = 'https://crystalmathlabs.com/tracker/track.php?player='
cml_update_url = 'https://crystalmathlabs.com/tracker/update.php?player='
cml_boss_url = 'https://crystalmathlabs.com/tracker/bosstrack.php?player='
cml_stats_url = 'https://crystalmathlabs.com/tracker/view_stats.php?player='
cml_sig = 'http://crystalmathlabs.com/tracker/sig.php?name='
cml_logo = 'https://crystalmathlabs.com/tracker/images/logo.png'


def cml_track(username, duration):
    return f'https://crystalmathlabs.com/tracker/api.php?type=track&player={username}&time={duration}'


class Tracker:
    """ Crystal Math Labs xp tracking class """

    def __init__(self, username):
        self.username = username
        self.logo = cml_logo
        if username == '':
            raise NoUsername('You must type a username after the command.\n'
                             'Type `!b help xp` for more information.')

    async def fetch(self, time='7d'):
        """ Fetch CML results """
        # Event loop
        loop = asyncio.get_event_loop()
        # Update results if able
        update = loop.run_in_executor(None, requests.get, cml_update_url + self.username)
        # Await update page
        update_response = await update
        # Get username's page
        self.url = cml_url + self.username + f'&time={time}'
        req = loop.run_in_executor(None, requests.get, self.url)
        # Boss kill request
        boss_req = loop.run_in_executor(None, requests.get, cml_boss_url + self.username + f'&time={time}')
        # Stats request
        stats_req = loop.run_in_executor(None, requests.get, cml_stats_url + self.username + f'&time={time}')
        # Await requests
        response = await req
        boss_res = await boss_req
        stats_res = await stats_req
        if response.status_code == 404:
            raise UserNotFound(f'No data for {self.username}.')
        # Parse responses
        doc = BeautifulSoup(response.content, 'html.parser')
        boss_doc = BeautifulSoup(boss_res.content, 'html.parser')
        stats_doc = BeautifulSoup(stats_res.content, 'html.parser')

        # Put results in an array of tuples
        # (Skill name, XP gained, Rank change, Levels gained, EHP)
        response = doc.find_all('tr')
        self.results = []
        for i in response[1:-1]:
            # Parse
            name = i.a.text
            if name.strip() == 'EHP':
                break
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

        # Sort results by xp gained (second item in tuple)
        # https://stackoverflow.com/a/3121985
        self.top_gains = sorted(self.results, key=lambda tup: tup[1], reverse=True)
        for (name, xp, rank, levels, ehp) in self.top_gains:
            if name == 'Overall':
                if xp == 0:
                    raise NoDataPoints(f'Either this is the first time {self.username} has been tracked this week, '
                                       f'or no XP has been gained. Gain some more XP and try again.\n\n'
                                       '(This command is more useful if you use it often.)')

        # Extract last changed time
        details_response = doc.find_all('div', {"id": "track_details"})
        details_search = details_response[0].find_all('span')
        self.results_duration = details_search[0].text
        self.oldest_data = details_search[2].text
        self.last_checked = details_search[6].text
        self.last_changed = details_search[8].text

        # Boss kill counts
        boss_response = boss_doc.find_all('tr')
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

        # Get stats
        stats_response = stats_doc.find_all('tr')
        self.stats = []
        for i in stats_response[1:-1]:
            # Parse
            search = i.find_all('td')
            name = search[0].text
            if name.strip() == 'EHP':
                break
            xp = search[1].text.replace(',', '')
            rank = search[2].text.replace(',', '')
            lvl = search[3].text.replace(',', '')
            # Store results
            self.stats.append((name, xp, rank, lvl))

    def get_lvl(self, name):
        """ Returns the lvl for a stat """
        for (skill, xp, rank, lvl) in self.stats:
            if name.strip() == skill.strip():
                return lvl

    def get_non_virtual_lvl(self, name):
        """ Returns the non-virtal lvl for a stat """
        overall = 0
        for (skill, xp, rank, lvl) in self.stats[1:]:
            if int(lvl) > 99:
                overall += 99
            else:
                overall += int(lvl)
            if name.strip() == skill.strip():
                if int(lvl) > 99:
                    return 99
                else:
                    return lvl
        if name.strip() == 'Overall':
            return overall

    def generate_table(self, skills=5):
        """ Returns a formatted table of top 5 gains """
        results = []
        results.append(('Skill', 'Lvl', 'XP'))
        for (name, xp, rank, levels, ehp) in self.top_gains[1:skills + 1]:
            if xp > 0:
                high_level = int(self.get_lvl(name))
                low_level = high_level - int(levels)
                if high_level == low_level:
                    results.append((name, high_level, f'+{xp:,}'))
                else:
                    results.append((name, f'{low_level} to {high_level}', f'+{xp:,}'))
        if len(results) == 0:
            return None
        return tabulate(results, tablefmt='plain')

    def generate_recent_kills_table(self):
        """ Returns a formatted table of recent boss kills """
        results = []
        for (name, kills, rank) in self.top_kills:
            if kills > 0:
                results.append((kills, name))
        if len(results) == 0:
            return None
        return tabulate(results, tablefmt='plain')

    def get_sig(self):
        return f'{cml_sig}{self.username}'


class UserNotFound(TypeError):
    pass


class NoDataPoints(Exception):
    pass


class NoUsername(Exception):
    pass
