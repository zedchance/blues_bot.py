# Used to pull API data from the GE page

import json

import matplotlib.pyplot as plotter
import requests
from osrsbox import items_api

from helpers.urls import ge_api_item_url, ge_graph_url, ge_query_url


def nice_price(price):
    """ Returns the price in nice numbers with k/m/b on the end as a string """
    if price < 1000:
        return f'{price:,.0f} gp'
    elif price < 1000000:
        return f'{price / 1000:,.1f} K gp'
    elif price < 1000000000:
        return f'{price / 1000000:,.1f} M gp'
    else:
        return f'{price / 1000000000:,.2f} B gp'


class GrandExchange:
    """ Pulls API data from the GE website """

    def __init__(self, query):
        # Check if query was entered
        self.query = query
        if query == '':
            raise MissingQuery("You must enter a search term")

        # This boolean is flipped if there is a lot of results from query
        self.multiple_results = False

        # Search using API query
        self.matches = self.get_matches()
        if len(self.matches) == 1:
            item_id = str(self.matches[0]['id'])
        elif len(self.matches) > 0 and self.matches[0]['name'].lower() == self.query.lower():
            item_id = str(self.matches[0]['id'])
        elif len(self.matches) == 0:
            # Search JSON file
            file = open('assets/item_ids.json')
            id_list = json.load(file)
            item_id = ''
            for i in id_list:
                if query.lower() in i['name'].lower():
                    item_id = str(i['id'])
                    break
            file.close()
        else:
            self.multiple_results = True
            return

        # Request data
        # Price info
        self.item = str(item_id)
        session = requests.session()
        req = session.get(ge_api_item_url + item_id)
        if req.status_code == 404:
            raise NoResults(f'No results for {query} found')
        data = req.json()
        # Graph data
        graph_req = session.get(f'{ge_graph_url}{item_id}.json')
        self.graph_data = graph_req.json()

        # Assign variables
        self.icon = data['item']['icon_large']
        self.id = data['item']['id']
        self.name = data['item']['name']
        self.description = data['item']['description']
        self.is_members = (data['item']['members'] == 'true')

        # Current price
        self.current_price = data['item']['current']['price']
        self.current_price_trend = data['item']['current']['trend']

        # Prices over time
        self.todays_price_trend = data['item']['today']['trend']
        self.todays_price_change = data['item']['today']['price']
        self.day30_trend = data['item']['day30']['trend']
        self.day30_change = data['item']['day30']['change']
        self.day90_trend = data['item']['day90']['trend']
        self.day90_change = data['item']['day90']['change']
        self.day180_trend = data['item']['day180']['trend']
        self.day180_change = data['item']['day180']['change']

        # Details from osrsbox
        all_db_items = items_api.load()
        self.buy_limit = 'N/A'
        self.high_alch = 'N/A'
        for item in all_db_items:
            if str(item.id) == item_id:
                if item.buy_limit:
                    self.buy_limit = f'{item.buy_limit:,}'
                if item.highalch:
                    self.high_alch = f'{item.highalch:,}'

    def generate_graph(self):
        """ Generates a graph of daily price data """
        # Gather data
        prices = []
        average = []
        for data in self.graph_data['daily']:
            prices.append(self.graph_data['daily'][data])
        for data in self.graph_data['average']:
            average.append(self.graph_data['average'][data])
        plotter.rcParams['ytick.color'] = 'lightslategrey'
        plotter.rcParams['figure.figsize'] = 8, 3
        plotter.box(on=None)
        # Axis labels
        high = max(prices)
        mid = sum(prices)/len(prices)
        low = min(prices)
        plotter.yticks([high, mid, low], [nice_price(high), nice_price(mid), nice_price(low)])
        plotter.xticks([])
        # Average line
        plotter.axhline(y=mid, dashes=[1, 3])
        # Title, plot, and save
        plotter.title('Past 180 days', loc='right', color='lightslategrey')
        plotter.plot(average, color="red")
        plotter.plot(prices, color="lightslategrey")
        plotter.savefig('assets/graph.png', transparent=True)
        plotter.close()

    def get_matches(self):
        """ Searches for the ID number of the query """
        session = requests.session()
        url = ge_query_url(self.query)
        req = session.get(url)
        data = req.json()
        matches = []
        for item in data['items']:
            if self.query.lower() in item['name'].lower():
                matches.append(item)
        return matches

    def get_possible_matches_str(self):
        """ Returns a string of the top possible matches """
        ret = f''
        count = 1
        for i in self.matches:
            ret += f"`{count}` {i['name']} - *{i['current']['price']} gp*\n"
            count += 1
        ret += f'\nReply with number for more information.'
        return ret


class MissingQuery(Exception):
    pass


class NoResults(TypeError):
    pass
