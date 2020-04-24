# Used to pull API data from the GE page

import asyncio
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
            raise MissingQuery("You must enter a search term after the command")

        # This boolean is flipped if there is a lot of results from query
        self.multiple_results = False

        # Fields
        self.matches = []
        self.item_id = ''
        self.graph_data = None
        self.icon = None
        self.id = None
        self.name = None
        self.description = None
        self.is_members = None
        self.current_price = None
        self.current_price_trend = None
        self.todays_price_trend = None
        self.todays_price_change = None
        self.day30_trend = None
        self.day30_change = None
        self.day90_trend = None
        self.day90_change = None
        self.day180_trend = None
        self.day180_change = None
        self.buy_limit = 'N/A'
        self.high_alch = 'N/A'

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

    async def fetch(self):
        """ Fetch the data from the GrandExchange """
        # Event loop
        loop = asyncio.get_event_loop()
        # Find item ID
        url = ge_query_url(self.query)
        match_req = loop.run_in_executor(None, requests.get, url)
        match_response = await match_req
        match_data = match_response.json()
        for item in match_data['items']:
            if self.query.lower() in item['name'].lower():
                self.matches.append(item)
        if len(self.matches) == 1:
            self.item_id = str(self.matches[0]['id'])
        elif len(self.matches) > 0 and self.matches[0]['name'].lower() == self.query.lower():
            self.item_id = str(self.matches[0]['id'])
        elif len(self.matches) == 0:
            # Search JSON file
            file = open('assets/item_ids.json')
            id_list = json.load(file)
            for i in id_list:
                if self.query.lower() in i['name'].lower():
                    self.item_id = str(i['id'])
                    break
            file.close()
        else:
            self.multiple_results = True
            return

        # Price info
        req = loop.run_in_executor(None, requests.get, ge_api_item_url + self.item_id)
        # Graph data
        graph_req = loop.run_in_executor(None, requests.get, f'{ge_graph_url}{self.item_id}.json')
        # Responses
        response = await req
        graph_response = await graph_req
        if response.status_code == 404:
            raise NoResults(f'No results for {self.query} found')
        data = response.json()
        self.graph_data = graph_response.json()

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

        # OSRSBox details
        all_db_items = items_api.load()
        for item in all_db_items:
            if str(item.id) == self.item_id:
                if item.buy_limit:
                    self.buy_limit = f'{item.buy_limit:,}'
                if item.highalch:
                    self.high_alch = f'{item.highalch:,}'

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
