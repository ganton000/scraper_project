from fastapi import HTTPException


class NotFoundException(HTTPException):

	def __init__(self, param_not_found: str) -> None:
		super().__init__(status_code=404, detail=f"{param_not_found} does not exist!")
