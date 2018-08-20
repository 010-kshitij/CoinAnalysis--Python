import requests
from bs4 import BeautifulSoup
import json

class CoinValues:
    """ Getting Dynamic Coin Values """

    def get(self):
        coins = ('bitcoin', 'bitcoincash', 'dash', 'dogecoin', 'ethereum', 'litecoin', 'nxt', 'nem', 'ripple')
        url = "https://www.worldcoinindex.com/"
        headers = {'User-Agent':'Mozilla/5.0'}
        page = requests.get(url)

        coin_values = dict()

        soup = BeautifulSoup(page.text, 'html.parser')

        tables = soup.find_all('table')

        for table in tables:
            for tr in table.find_all('tr'):
                if tr.get('data-naam') in coins:
                    h2 = tr.h2.decode_contents(formatter="html").strip()
                    spans = tr.find_all('span')
                    n_spans = list()
                    for span in spans:
                        n_spans.append( span.decode_contents(formatter="html").strip())
                    coin_values[h2] = n_spans

        return coin_values
