from typing import Optional

from pydantic import BaseModel, Field


class Symbol(BaseModel):
	symbol: str
	name: str
	date_scraped: str
	exchange: str = "NASDAQ"
	price: float
	market_cap: float = Field(
		description="market cap in trillions (USD)"
	)
	pe_ratio: float
	close_price: float
	prev_close: float
	position: str
	close_diff: float
	close_diff_percent: float
	day_low: float
	day_high: float
	year_low: float
	year_high: float
	dividend_yield: Optional[float]
	avg_volume: float = Field(
		description="avg trading volume in millions"
	)

class MultipleSymbols(BaseModel):
	symbols: list[Symbol]