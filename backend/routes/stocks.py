from fastapi import APIRouter, Depends

from schemas.symbol import Symbol, MultipleSymbols
from services.symbol_service import SymbolService
from services.exceptions import NotFoundException
from utils.utils import get_file_logger, get_console_logger
from helpers.dependencies import RateLimit


def create_stock_router(log_level: str) -> APIRouter:

	# initializations
	rate_limiter = RateLimit().create_rate_limiter
	router = APIRouter(
		prefix="/symbol",
		tags=["stocks"],
		dependencies=[Depends(rate_limiter)]
	)
	symbol_service = SymbolService()
	logger = get_file_logger(__name__, log_level)


	@router.post("/", response_model=MultipleSymbols, status_code=201)
	async def add_symbol(symbol_name: str) -> MultipleSymbols:
		"""Endpoint to create a new Symbol. Triggers the worker to scrape the data.

		Args:
			symbol_name (str): provided name of symbol.

		Returns:
			MultipleSymbols: List of Symbols
		"""
		logger.info(f"Creating {symbol_name} symbol...")
		await symbol_service.create_stub_data()
		new_data = await symbol_service.create_symbol(symbol_name)
		STUB_DATA.append(new_data)
		return STUB_DATA


	@router.get("/all", response_model=MultipleSymbols)
	async def get_all_symbols(start: int=0, limit: int=4) -> MultipleSymbols:
		"""Endpoint to retrieve all Symbols

		Args:
			start (int, optional): index to begin pagination. Defaults to 0.
			limit (int, optional): index to end paginated results. Defaults to 4.

		Returns:
			MultipleSymbols: List of Symbols
		"""
		symbols = await symbol_service.get_all_symbols_with_pagination(start, limit)
		formatted_symbols = { "symbols": symbols }
		symbols_response = MultipleSymbols(**formatted_symbols)
		return symbols_response

	@router.get("/{symbol_name}", response_model=Symbol)
	async def get_symbol(symbol_name: str) -> Symbol:
		"""Endpoint to retrieve a Symbol by its name attribute.

		Args:
			symbol_name (str): unique Symbol name

		Returns:
			Symbol
		"""
		logger.info(f"Fetching {symbol_name}...")
		symbol = await symbol_service.create_symbol(symbol_name)
		return symbol

	@router.put("/{symbol_name}")
	async def update_symbol(new_symbol_data: dict) -> MultipleSymbols:
		"""Endpoint to update a Symbol with the attributes provided

		Args:
			new_symbol_data (dict): JSON of symbol data information to be updated

		Returns:
			MultipleSymbols: List of Symbols
		"""
		logger.info(f"Updating {symbol_name}...")
		global STUB_DATA

		STUB_DATA = [] ## reset

		await symbol_service.create_stub_data()

		symbol_name = new_symbol_data.get("symbol")

		filtered_stub_data = [ model for model in STUB_DATA if model.symbol != symbol_name]
		filtered_stub_data.append(Symbol(**new_symbol_data))
		formatted_symbols = { "symbols": filtered_stub_data }
		symbols_response = MultipleSymbols(**formatted_symbols)
		return symbols_response

	@router.delete("/{symbol_name}")
	async def delete_symbol(symbol_name: str) -> dict:
		"""Endpoint to remove a stock Symbol

		Args:
			symbol_name (str): name attribute of Symbol

		Returns:
			dict: success or does not exist message
		"""
		logger.info(f"Deleting {symbol_name}...")
		global STUB_DATA

		STUB_DATA = [] ## reset

		await symbol_service.create_stub_data()

		filtered_stub_data = [ model for model in STUB_DATA if model.symbol != symbol_name]

		if len(filtered_stub_data) == len(STUB_DATA):
			logger.error(f"Error deleting {symbol_name}... not found")
			raise NotFoundException(symbol_name)

		STUB_DATA = filtered_stub_data

		return { "message" : f"{symbol_name} was successfully deleted!"}

	return router
