from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

from routes import stocks

app = FastAPI()

origins = ["http://localhost", "http://localhost:3000"] ## react dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(stocks.router)


@app.get("/")
def home() -> dict:
    return {"message": "Hello World"}



if __name__ == "__main__":
    pass
    #uvicorn.run(app, host="localhost", port=8000)


