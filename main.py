
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

from models.symbol import Symbol

app = FastAPI()

symbols = {
     "apple": { "stock": "AAPL", "name": "Apple", "price": 100 },
     "microsoft": { "stock": "MSFT", "name": "Microsoft", "price": 90 }
}

@app.get("/", response_class=JSONResponse)
def home() -> dict:
    return {"message": "Hello World"}

@app.get("/symbol/{symbol_name}", response_model=dict)
def get_symbol(symbol_name: str) -> dict:
	return symbols.get(symbol_name, {"message": "Symbol not found!"})


if __name__ == "__main__":
    pass


