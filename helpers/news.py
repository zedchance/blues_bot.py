# Pulls latest news from OSRS site

import asyncio
import requests
from bs4 import BeautifulSoup, NavigableString

from helpers.urls import news_rss_feed


class News:
    """ Pulls the latest news from the OSRS RSS feed """

    def __init__(self):
        self.title = 'Old School RuneScape Recent News'

    async def fetch(self):
        """ Fetches the news """
        # Event loop
        loop = asyncio.get_event_loop()
        # Make request
        req = loop.run_in_executor(None, requests.get, news_rss_feed)
        response = await req
        if response.status_code == 404:
            print("404 from RSS feed")  # TODO
            return
        feed = BeautifulSoup(response.content, 'html.parser')

        # Build tuple array of latest articles
        # (Title, Description, Category, Link, Publication date)
        items = feed.find_all('item')
        self.articles = []
        for i in items:
            title = i.title.text
            description = i.description.text.strip()
            category = i.category.text
            link = i.guid.text
            pubdate = i.pubdate.text
            self.articles.append((title, description, category, link, pubdate))
