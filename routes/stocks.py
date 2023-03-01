import asyncio

from fastapi import APIRouter

from models.symbol import Symbol, MultipleSymbols
from workers.GoogleWorker import GoogleFinanceWorker


## stub data
symbols = ["AAPL", "TSLA", "MSFT", "GOOG"]

STUB_DATA = []

async def create_symbol(symbol_name: str) -> Symbol:
	worker = GoogleFinanceWorker(symbol_name)
	symbol_data = await worker.process_data()
	return Symbol(**symbol_data)

async def create_stub_data() -> list[Symbol]:
	for symbol_name in symbols:
		STUB_DATA.append(await create_symbol(symbol_name))
	return STUB_DATA


async def get_all_symbols_with_pagination(start: int, limit: int) -> list[Symbol]:
	global STUB_DATA
	await create_stub_data()
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

router = APIRouter()

@router.post("/symbol", response_model=MultipleSymbols)
async def add_symbol(symbol_name: str) -> MultipleSymbols:
	"""Endpoint to create a new Symbol. Triggers the worker to scrape the data.

	Args:
		symbol_name (str): provided name of symbol.

	Returns:
		MultipleSymbols: List of Symbols
	"""
	await create_stub_data()
	new_data = await create_symbol(symbol_name)
	STUB_DATA.append(new_data)
	return STUB_DATA

@router.get("/symbol/{symbol_name}", response_model=Symbol)
async def get_symbol(symbol_name: str) -> Symbol:
	"""Endpoint to retrieve a Symbol by its name attribute.

	Args:
		symbol_name (str): unique Symbol name

	Returns:
		Symbol
	"""
	symbol = await create_symbol(symbol_name)
	return symbol

@router.put("/symbol/{symbol_name}")
async def update_symbol(new_symbol_data: dict) -> MultipleSymbols:
	"""Endpoint to update a Symbol with the attributes provided

	Args:
		new_symbol_data (dict): JSON of symbol data information to be updated

	Returns:
		MultipleSymbols: List of Symbols
	"""
	global STUB_DATA

	STUB_DATA = [] ## reset

	await create_stub_data()

	symbol_name = new_symbol_data.get("symbol")

	filtered_stub_data = [ model for model in STUB_DATA if model.symbol != symbol_name]
	filtered_stub_data.append(Symbol(**new_symbol_data))
	formatted_symbols = { "symbols": filtered_stub_data }
	symbols_response = MultipleSymbols(**formatted_symbols)
	return symbols_response

@router.get("/symbols", response_model=MultipleSymbols)
async def get_all_symbols(start: int=0, limit: int=4) -> MultipleSymbols:
	"""Endpoint to retrieve all Symbols

	Args:
		start (int, optional): index to begin pagination. Defaults to 0.
		limit (int, optional): index to end paginated results. Defaults to 4.

	Returns:
		MultipleSymbols: List of Symbols
	"""
	symbols = await get_all_symbols_with_pagination(start, limit)
	formatted_symbols = { "symbols": symbols }
	symbols_response = MultipleSymbols(**formatted_symbols)
	return symbols_response

@router.delete("/symbol/{symbol_name}")
async def delete_symbol(symbol_name: str) -> dict:
	"""Endpoint to remove a stock Symbol

	Args:
		symbol_name (str): name attribute of Symbol

	Returns:
		dict: success or does not exist message
	"""
	global STUB_DATA

	STUB_DATA = [] ## reset

	await create_stub_data()

	filtered_stub_data = [ model for model in STUB_DATA if model.symbol != symbol_name]

	if len(filtered_stub_data) == len(STUB_DATA):
		return { "message" : f"{symbol_name} does not exist!" }

	STUB_DATA = filtered_stub_data

	return { "message" : f"{symbol_name} was successfully deleted!"}
