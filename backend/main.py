import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse

from routes.stocks import create_stock_router
from database import create_tables, get_db


# initialize logger
log_level = "INFO"


origins = ["http://localhost", "http://localhost:3000", "http://scraper_api-frontend:3000"] ## react dev


def create_app(origins: list[str]) -> FastAPI:

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    stock_router = create_stock_router(log_level)
    app.include_router(stock_router)

    return app

app = create_app(origins)

### creates postgres tables
create_tables()

@app.get("/")
def home() -> dict:
    return {"message": "Hello World"}


if __name__ == "__main__":
    with get_db() as db:
        result = db.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        print([row[0] for row in result])
    #uvicorn.run(app, host="localhost", port=8000)


