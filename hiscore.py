# Used to pull hiscores from OSRS hiscore page

import requests
from bs4 import BeautifulSoup

main_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

class Hiscore:
    """ Pulls hiscores from OSRS hiscore page """

    def __init__(self, username):
        session = requests.session()
        req = session.get(main_url + username)
        doc = BeautifulSoup(req.content, 'html.parser')
        first = [i.split() for i in doc]
        self.scores = [i.split(',') for i in first[0]]

# Test code
b = Hiscore("bluetrane")
print(b.scores)