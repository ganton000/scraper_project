from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class Symbol(BaseModel):
	symbol: str
	name: str
	date_scraped: date
	exchange: str = "NASDAQ"
	price: float
	market_cap: float = Field(
		description="market cap in trillions (USD)"
	)
	pe_ratio: float
	close_price: float
	prev_close: float
	position: str = "gain" if close_price > prev_close else "loss"
	close_diff: float = prev_close - close_price
	close_diff_percent: float = - round((close_diff/prev_close)*100, 2) if close_diff < 0 \
								else round((close_diff/prev_close)*100, 2)
	day_low: float
	day_high: float
	year_low: float
	year_high: float
	dividend_yield: Optional[float]
	avg_volume: float = Field(
		description="avg trading volume in millions"
	)
