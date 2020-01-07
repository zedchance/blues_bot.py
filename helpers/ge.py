# Used to pull API data from the GE page

import requests
import json
import matplotlib.pyplot as plotter
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter

from helpers.urls import ge_api_item_url, ge_graph_url


class GrandExchange:
    """ Pulls API data from the GE website """

    def __init__(self, query):
        # Check if query was entered
        if query == '':
            raise MissingQuery("You must enter a search term")

        # Search for ID number from query
        file = open('assets/item_ids.json')
        id_list = json.load(file)
        item_id = ""
        for i in id_list:
            if query.lower() in i['name'].lower():
                item_id = str(i['id'])
                break
        file.close()

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

    def generate_graph(self):
        """ Generates a graph of daily price data """
        prices = []
        average = []
        for data in self.graph_data['daily']:
            prices.append(self.graph_data['daily'][data])
        for data in self.graph_data['average']:
            average.append(self.graph_data['average'][data])
        plotter.rcParams['ytick.color'] = 'lightslategrey'
        plotter.rcParams['figure.figsize'] = 8, 3
        plotter.box(on=None)
        plotter.xticks([])
        plotter.title('Past 180 days', loc='right', color='lightslategrey')
        plotter.plot(average, color="red")
        plotter.plot(prices, color="lightslategrey")
        plotter.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f} gp'))
        plotter.savefig('assets/graph.png', transparent=True)
        plotter.close()


class MissingQuery(Exception):
    pass


class NoResults(TypeError):
    pass
