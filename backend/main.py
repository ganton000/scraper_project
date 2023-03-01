from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

from routes.stocks import create_stock_router


origins = ["http://localhost", "http://localhost:3000"] ## react dev


def create_app(origins: list[str]) -> FastAPI:

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    stock_router = create_stock_router()
    app.include_router(stock_router)

    return app

app = create_app(origins)

@app.get("/")
def home() -> dict:
    return {"message": "Hello World"}

if __name__ == "__main__":
    pass
    #uvicorn.run(app, host="localhost", port=8000)


