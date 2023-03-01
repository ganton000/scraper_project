from time import time

from fastapi import Response
from services.exceptions import RateLimitExceeded

## globals
START_TIME = time()
RESET_INTERVAL = 3600 ## seconds
REQUEST_COUNT = 0
REQUEST_LIMIT = 5


def rate_limit(response: Response) -> None:
	global START_TIME
	global RESET_INTERVAL
	global REQUEST_COUNT
	global REQUEST_LIMIT

	# reset
	if time() > (START_TIME + RESET_INTERVAL):
		START_TIME = time()
		REQUEST_COUNT = 0

	# limit reached
	if REQUEST_COUNT >= REQUEST_LIMIT:
		timeout = round(START_TIME + RESET_INTERVAL - time(), 2) + 0.01
		raise RateLimitExceeded(timeout)

	REQUEST_COUNT += 1
	# create header for rate-limit
	response.headers["X-app-rate-limit"] = f"{REQUEST_COUNT}:{REQUEST_LIMIT}"

	return Response