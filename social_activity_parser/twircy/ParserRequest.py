from typing import NamedTuple


class TwitterRequest(NamedTuple):
	search_phrase: str
	for_days: int = 14
	limit: int = 10000
	min_likes: int = 0
