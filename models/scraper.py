import re
import asyncio
import aiohttp
from datetime import date
from threading import Thread
from typing import Optional, queue

from bs4 import BeautifulSoup

class GoogleFinanceWorker(Thread):


	def __init__(self, symbol: str, output_queue: queue, exchange: str="NASDAQ", **kwargs) -> None:
		super(GoogleFinanceWorker, self).__init__()
		self._symbol = symbol.upper()
		self._exchange = exchange.upper()
		self._output_queue = output_queue
		self._url = f"https://www.google.com/finance/quote/{self._symbol}:{self._exchange}?hl=en"


	async def _get_stock_data(self):
		async with aiohttp.ClientSession() as session:
			async with session.get(self._url) as response:
				if response.status != 200:
					raise Exception("Unable to retrieve response from request!")

				page_contents = BeautifulSoup(await response.text(), "html.parser")

				return page_contents

	async def run(self):
		pass

class GoogleFinanceProcessor(Thread):

	def __init__(self, input_queue: queue, output_queue: queue, **kwargs) -> None:
		super(GoogleFinanceProcessor, self).__init__()
		self._input_queue = input_queue
		self._output_queue = output_queue


	async def process_data(self):
				page_contents = self._get_stock_data()
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
				params["date_scraped"] = date.today().strftime("%m/%d/%Y")

				return params


	async def run(self):
		pass


async def main():

	symbol = "tsla"
	worker = GoogleFinanceWorker(symbol)

	results = asyncio.create_task(worker.get_stock_data())


	await results
	print(results)


if __name__ == "__main__":
	asyncio.run(main())