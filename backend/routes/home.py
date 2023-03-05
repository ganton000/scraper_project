from fastapi import APIRouter


def create_home_router(log_level: str):

	router = APIRouter(
		tags=["home"],
	)

	@router.get("/")
	def home() -> dict:
		return {"message": "Hello World"}

	return router