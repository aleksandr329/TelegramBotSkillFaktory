import requests
import json
from bs4 import BeautifulSoup as BS
from parameters import nam

##I didn't add @staticmethod in my opinion, he's not really needed here!

class Valuta:
    def __init__(self, base: str, quote: str):
        self.base = base.lower()
        self.quote = quote.lower()

    def get_price(self):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={nam[self.base]}&tsyms={nam[self.quote]}')
        text = json.loads(r.content)
        for a, b in text.items():
            c = a
            z = b
        return z

class EnterErorr(Exception):
    pass
