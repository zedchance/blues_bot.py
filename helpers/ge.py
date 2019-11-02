# Used to pull API data from the GE page

import requests

from helpers.urls import ge_api_item_url

class GrandExchange:
    """ Pulls API data from the GE website """
    def __init__(self, item):
        self.item = item
        if item == '':
            raise MissingQuery("You must enter a search term")
        # Request data
        session = requests.session()
        req = session.get(ge_api_item_url + item)
        if req.status_code == 404:
            raise NoResults(f'No results for {item} found')
        data = req.json()

        # Assign variables
        self.icon = data['item']['icon']
        self.id = data['item']['id']
        self.name = data['item']['name']
        self.description = data['item']['description']
        self.is_members = (data['item']['members'] == 'true')

        # Current price
        self.current_price = data['item']['current']['price']
        self.current_price_trend = data['item']['current']['trend']

        # Prices over time
        self.todays_price_trend = data['item']['today']['trend']
        self.todays_price = data['item']['today']['price']
        self.day30_price_trend = data['item']['day30']['trend']
        self.day30_price = data['item']['day30']['change']
        self.day90_price_trend = data['item']['day90']['trend']
        self.day90_price = data['item']['day90']['change']
        self.day180_price_trend = data['item']['day180']['trend']
        self.day180_price = data['item']['day180']['change']

class MissingQuery(Exception):
    pass

class NoResults(TypeError):
    pass