from models.symbol import Symbol
from workers.GoogleWorker import GoogleFinanceWorker

## stub data
symbols = ["AAPL", "TSLA", "MSFT", "GOOG"]

STUB_DATA = []


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
		STUB_DATA = [] # reset global
		return symbols_arr
