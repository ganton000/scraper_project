import re
import asyncio
import aiohttp
from datetime import date
from threading import Thread

from bs4 import BeautifulSoup

class Scraper(Thread):


	def __init__(self, symbol: str, exchange: str="NASDAQ", **kwargs) -> None:
		super(Scraper, self).__init__()
		self._symbol = symbol.upper()
		self._exchange = exchange.upper()
		self._url = f"https://www.google.com/finance/quote/{self._symbol}:{self._exchange}?hl=en"


	async def get_stock_data(self):
		async with aiohttp.ClientSession() as session:
			async with session.get(self._url) as response:
				if response.status != 200:
					raise Exception("Unable to retrieve response from request!")

				page_contents = BeautifulSoup(await response.text(), "html.parser")

				#table_data = page_contents.find_all("div", {"class": "P6K39c"})
				table_data = page_contents.select(".P6K39c")
				table_keys = ["prev_close", "day_low", "day_high", "year_low", "year_high", "market_cap", "avg_volume", "pe_ratio", "dividend_yield"]

				values = ",".join(( data.text for data in table_data ))

				# extract only numeric values
				pattern = r'\d+(?:\.\d+)?'
				parsed_values = re.findall(pattern, values)

				# convert numeric strings to float and create dict
				table_values = [ float(val) for val in parsed_values ][0:9]
				params = dict(zip(table_keys, table_values))

				return params



	async def run(self):
		pass


async def main():

	symbol = "msft"
	worker = Scraper(symbol)

	results = await worker.get_stock_data()
	print(results)


if __name__ == "__main__":
	asyncio.run(main())