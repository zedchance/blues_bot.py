# Crystal Math Labs xp tracker

import requests
from bs4 import BeautifulSoup

from helpers.urls import cml_url, cml_update_url, cml_sig

class Tracker():
    """ Crystal Math Labs xp tracking class """

    def __init__(self, username):
        self.username = username
        session = requests.session()
        update = session.get(cml_update_url + self.username)

    def get_sig(self):
        return f'{cml_sig}{self.username}'