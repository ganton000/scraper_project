import asyncio
from typing import List

from fastapi import APIRouter

from models.symbol import Symbol
from workers.GoogleWorker import GoogleFinanceWorker


## stub data
symbols = ["AAPL", "TSLA", "MSFT"]


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
     response = [ await create_symbol(symbol_name) for symbol_name in symbols ]
     return response
