from pydantic import BaseModel


class Symbol(BaseModel):
	symbol: str
	url: str

