
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

from models.symbol import Symbol

app = FastAPI()


@app.get("/", response_class=JSONResponse)
def home() -> dict:
    return {"message": "Hello World"}

@app.post("/symbol/", response_model=Symbol)
def get_symbol(symbol_name: str) -> Symbol:
	return Symbol(symbol_name)

if __name__ == "__main__":
    pass


