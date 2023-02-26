from typing import Optional

from pydantic import BaseModel, Field


class Symbol(BaseModel):
	symbol: str
	name: str
	exchange: str
	price: float
	prev_close: float
	dividend_yield: Optional[float]
	avg_volume: float = Field(
		description="avg trading volume in millions"
	)


