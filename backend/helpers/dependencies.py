from time import time

from fastapi import Response
from services.exceptions import RateLimitExceeded


class RateLimit:

	def __init__(self, reset_interval: int=3600, request_count: int=0, request_limit: int=5) -> None:
		self.start_time= time()
		self.reset_interval = 3600 ## seconds
		self.request_count = 0
		self.request_limit = 5


	def create_rate_limiter(self, response: Response) -> Response:

		# reset
		if time() > (self.start_time + self.reset_interval):
			self.start_time = time()
			self.request_count = 0

		# limit reached
		if self.request_count > self.request_limit:
			timeout = round(self.start_time + self.reset_interval - time(), 2) + 0.01
			raise RateLimitExceeded(timeout)

		self.request_count += 1
		# create header for rate-limit
		response.headers["X-app-rate-limit"] = f"{self.request_count}:{self.request_limit}"

		return Response