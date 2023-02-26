from fastapi import APIRouter

from models.symbol import Symbol


symbols = {
     "apple": { "stock": "AAPL", "name": "Apple", "price": 100 },
     "microsoft": { "stock": "MSFT", "name": "Microsoft", "price": 90 }
}

router = APIRouter()

@router.get("/symbol/{symbol_name}", response_model=dict)
def get_symbol(symbol_name: str) -> dict:
	return symbols.get(symbol_name, {"message": "Symbol not found!"})

