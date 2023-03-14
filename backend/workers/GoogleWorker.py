import re
import asyncio
import aiohttp
from datetime import date
from threading import Thread
from queue import Queue, Empty

from bs4 import BeautifulSoup


class GoogleFinanceWorker:

	def __init__(self, symbol: str, exchange: str="NASDAQ", **kwargs) -> None:
		self._symbol = symbol.upper()
		self._exchange = exchange.upper()
		self._url = f"https://www.google.com/finance/quote/{self._symbol}:{self._exchange}?hl=en"


	async def _get_stock_data(self):
		async with aiohttp.ClientSession() as session:
			async with session.get(self._url) as response:
				if response.status != 200:
					raise Exception("Unable to retrieve response from request!")

				page_contents = BeautifulSoup(await response.text(), "html.parser")

				return page_contents

	async def process_data(self):
			page_contents = await self._get_stock_data()

			table_data = page_contents.select(".P6K39c")
			table_keys = ["prev_close", "day_low", "day_high", "year_low", "year_high", "market_cap", "avg_volume", "pe_ratio", "dividend_yield"]

			values = ",".join(( data.text for data in table_data ))

			# extract only numeric values
			pattern = r'\d+(?:\.\d+)?'
			parsed_values = re.findall(pattern, values)

			# convert numeric strings to float and create dict
			table_values = (float(val) for val in parsed_values[:9])
			params = dict(zip(table_keys, table_values))
			params["date_scraped"] = date.today().strftime("%m/%d/%Y")
			params["price"] = float(page_contents.find("div", { "class" : "YMlKec fxKbKc"}).text.replace("$",""))

			parent_div = page_contents.find('div', {'jsname': 'ip75Cb', 'class': 'kf1m0'})
			nested_div = parent_div.find('div', {'class': 'YMlKec fxKbKc'})
			params["close_price"] = float(nested_div.text.replace("$",""))

			params["symbol"] = self._symbol
			params["name"] = page_contents.select(".zzDege")[0].text
			params["position"] = "Gain" if params["close_price"] > params["prev_close"] else "Loss"
			params["close_diff"]  = round(abs(params["close_price"] - params["prev_close"]), 2)
			params["close_diff_percent"] = round((params["close_diff"]/params["prev_close"])*100, 2)

			return params

class GoogleFinanceWriter:

	def __init__(self, file_name: str, input_queue: Queue[str], **kwargs) -> None:
		super(GoogleFinanceWriter, self).__init__()
		self._input_queue = input_queue
		self.file_name = file_name

	async def write_data(self):
		pass


class GoogleFinanceQueueScheduler(Thread):

	def __init__(self, input_queue: Queue[str]=None, output_queue: Queue[str]=None, **kwargs) -> None:
		super(GoogleFinanceQueueScheduler, self).__init__()
		self._output_queue = output_queue
		self._input_queue = input_queue

	async def run(self) -> None:
		while True:

			try:
				ticker_symbol = self._input_queue.get()
			except Empty:
				print("{self.__name__} queue is empty")
				break

			if ticker_symbol == "FINISHED":
				break

			finance_worker = GoogleFinanceWorker(ticker_symbol)
			stock_dict = asyncio.create_task(finance_worker.process_data())

			# more stuff

			self._output_queue.put(await stock_dict)


async def main():

	symbol = "tsla"
	stocks_queue = Queue()
	worker = GoogleFinanceWorker(symbol, stocks_queue)

	results = asyncio.create_task(worker.process_data())


	await results
	print(results)


if __name__ == "__main__":
	asyncio.run(main())