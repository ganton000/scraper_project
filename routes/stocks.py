import asyncio
from typing import List

from fastapi import APIRouter

from models.symbol import Symbol
from workers.GoogleWorker import GoogleFinanceWorker


## stub data
symbols = ["AAPL", "TSLA", "MSFT"]

STUB_DATA = []

async def create_stub_data():
	for symbol_name in symbols:
		STUB_DATA.append(await create_symbol(symbol_name))
	return STUB_DATA

async def create_symbol(symbol_name: str) -> Symbol:
	worker = GoogleFinanceWorker(symbol_name)
	symbol_data = await worker.process_data()
	return Symbol(**symbol_data)

router = APIRouter()

@router.get("/symbol/{symbol_name}", response_model=Symbol)
async def get_symbol(symbol_name: str) -> Symbol:
	symbol = await create_symbol(symbol_name)
	print(symbol)
	return symbol

@router.get("/symbols/", response_model=List[Symbol])
async def get_symbols():
     await create_stub_data()
     return STUB_DATA

@router.post("/symbol", response_model=List[Symbol])
async def add_symbol(symbol_name: str):
	await create_stub_data()
	new_data = await create_symbol(symbol_name)
	STUB_DATA.append(new_data)
	return STUB_DATA
