from fastapi import HTTPException


class NotFoundException(HTTPException):

	def __init__(self, param_not_found: str) -> None:
		super().__init__(status_code=404, detail=f"{param_not_found} does not exist!")

class RateLimitExceeded(HTTPException):

	def __init__(self, timeout: float) -> None:
		error_message = {
			"error": "Rate limit exceeded",
			"timeout": timeout
		}
		super().__init__(status_code=429, detail=error_message)
