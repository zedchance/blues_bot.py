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

        # Get info from first article
        article_req = loop.run_in_executor(None, requests.get, self.articles[0][3])
        article_response = await article_req
        if article_response.status_code == 404:
            print("404 from article page")  # TODO
            return
        response = BeautifulSoup(article_response.content, 'html.parser')
        content = response.find('html')
        # Article image
        img_search = content.find_all('img')
        self.image = img_search[0].attrs.get('src')
        # Article text
        self.latest_article_text = ''
        sibling = content.next_sibling  # Skip over first line (which is the title)
        for i in sibling.next_siblings:
            if isinstance(i, NavigableString):
                if i != '\n':
                    self.latest_article_text += i.strip()
                    self.latest_article_text += '\n\n'
            else:
                if i.name == 'strong':
                    self.latest_article_text += f'**{i.text}**\n'
        if len(self.latest_article_text) > 1024:
            cut_length = 800 - len(self.articles[0][3]) + 20
            self.latest_article_text = self.latest_article_text[:cut_length]
            self.latest_article_text += f'... *[Read more]({self.articles[0][3]})*'
        # else:
        #     self.latest_article_text += f'*[Read more]({self.articles[0][3]})*'

        # Test code
        # text = ''
        # for i in content.next_siblings:
        #     if isinstance(i, NavigableString):
        #         text += i
        # print(text.strip())
