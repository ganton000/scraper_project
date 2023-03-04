from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from sqlalchemy import (
	Float,
	String,
	TIMESTAMP,
	UniqueConstraint
)

from models.base import Base

class Stocks(Base):
	__tablename__ = "stocks"

	__table_args__ = (UniqueConstraint("name", name="name"),)

	symbol: Mapped[str] = mapped_column(String(5), primary_key=True)
	name: Mapped[str] = mapped_column(String(20))
	date_scraped: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.utcnow)
	exchange: Mapped[str] = mapped_column(String(10), default="NASDAQ")
	price: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	market_cap: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	pe_ratio: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	close_price: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	prev_close: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	position: Mapped[str] = mapped_column(String(4))
	close_diff: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	close_diff_percent: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	day_low: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	day_high: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	year_low: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	year_high: Mapped[float] = mapped_column(Float(decimal_return_scale=2))
	dividend_yield: Mapped[float] = mapped_column(Float(decimal_return_scale=2), nullable=True)
	avg_volume: Mapped[float] = mapped_column(Float(decimal_return_scale=2))

	def __repr__(self) -> str:
		return f"stock {self.name} with ticker {self.symbol} on {self.exchange} exchange"
