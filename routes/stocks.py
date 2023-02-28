import asyncio

from fastapi import APIRouter

from models.symbol import Symbol, MultipleSymbols
from workers.GoogleWorker import GoogleFinanceWorker


## stub data
symbols = ["AAPL", "TSLA", "MSFT"]

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

@router.get("/symbol/{symbol_name}", response_model=Symbol)
async def get_symbol(symbol_name: str) -> Symbol:
	symbol = await create_symbol(symbol_name)
	return symbol

@router.get("/symbols", response_model=MultipleSymbols)
async def get_all_symbols(start: int=0, limit: int=2) -> MultipleSymbols:
    symbols = await get_all_symbols_with_pagination(start, limit)
    formatted_symbols = { "symbols": symbols }
    symbols_response = MultipleSymbols(**formatted_symbols)
    print(len(STUB_DATA))
    return symbols_response

@router.post("/symbol", response_model=MultipleSymbols)
async def add_symbol(symbol_name: str) -> MultipleSymbols:
	await create_stub_data()
	new_data = await create_symbol(symbol_name)
	STUB_DATA.append(new_data)
	return STUB_DATA
