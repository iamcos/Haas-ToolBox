from typing import NamedTuple


class ParserRequest(NamedTuple):
	search_phrase: str
	for_days: int = 14
	limit: int = 10000
