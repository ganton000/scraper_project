from time import perf_counter_ns

from models.symbol import Symbol
from workers.GoogleWorker import GoogleFinanceWorker
from utils.utils import get_console_logger

## stub data
symbols = ["AAPL", "TSLA", "MSFT", "GOOG"]

STUB_DATA = []

logger = get_console_logger(__name__)

class SymbolService:

	def __init__(self) -> None:
		pass

	@staticmethod
	async def create_symbol(symbol_name: str) -> Symbol:
		worker = GoogleFinanceWorker(symbol_name)
		symbol_data = await worker.process_data()
		return Symbol(**symbol_data)

	async def create_stub_data(self) -> list[Symbol]:
		for symbol_name in symbols:
			STUB_DATA.append(await self.create_symbol(symbol_name))
		return STUB_DATA


	async def get_all_symbols_with_pagination(self, start: int, limit: int) -> list[Symbol]:
		start_time = perf_counter_ns()
		global STUB_DATA
		await self.create_stub_data()
		symbols_arr = []
		for idx in range(len(STUB_DATA)):
			if idx < start:
				continue
			elif len(symbols_arr) >= limit:
				break
			else:
				symbols_arr.append(STUB_DATA[idx])

		end_time = perf_counter_ns() - start_time
		logger.info(f"Total time to grab data: {end_time:.2e} nanoseconds")
		STUB_DATA = [] # reset global
		return symbols_arr
