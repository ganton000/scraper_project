from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

from routes import stocks

app = FastAPI()


app.include_router(stocks.router)


@app.get("/")
def home() -> dict:
    return {"message": "Hello World"}



if __name__ == "__main__":
    pass
    #uvicorn.run(app, host="localhost", port=8000)


