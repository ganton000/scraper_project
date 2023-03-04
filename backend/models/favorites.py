from sqlalchemy import (
	ForeignKey,
	ARRAY,
    Integer,
	ForeignKeyConstraint,
	Index
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)


from models.base import Base

class Favorites(Base):
	__tablename__ = "favorites"

	#__table_args__ = (ForeignKeyConstraint("favorite_stocks", "stocks.symbol"),)
	#__table_args__ = (Index("ix_favorites_favorite_stocks_symbol", favorite_stocks, postgresql_using="gin"),)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	favorite_stocks: Mapped[list[int]] = mapped_column(ARRAY(ForeignKey("stocks.symbol")), default=None)

	stock = relationship("Stocks", backref="favorites")
