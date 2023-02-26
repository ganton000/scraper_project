import asyncio
from threading import Thread

import requests
from bs4 import BeautifulSoup

class Scraper(Thread):


	def __init__(self, symbol: str, exchange: str="NASDAQ", **kwargs) -> None:
		super(Scraper, self).__init__()
		self._symbol = symbol.upper()
		self._exchange = exchange.upper()
		self._url = f"https://www.google.com/finance/quote/{self._symbol}:{self._exchange}?hl=en"

	@staticmethod
	async def get_stock_data(self):
		pass

	def run(self):
		asyncio.run(self.get_stock_data())



if __name__ == "__main__":
    pass