
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

from models.symbol import Symbol

app = FastAPI()


@app.get("/", response_class=JSONResponse)
def home() -> dict:
    return {"message": "Hello World"}

@app.post("/symbol/", response_model=Symbol)
def get_symbol_data():

	return

if __name__ == "__main__":
    pass


