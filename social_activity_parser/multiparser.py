"""Gets markets from Haas API, parse tweets, save to db and calculates santiments"""
from typing import Any
import apis_list
import pandas as pd
from pandas import DataFrame
from requests_html import HTMLSession
from twircy import TwitterParser
import json
from loguru import logger



def send_get_request(url: str) -> Any:
    session = HTMLSession()
    r = session.get(url)
    result = json.loads(r.text)
    return result


def convert_coins_to_twitter_search_request_url(coins: tuple[str]) -> str:
	search_req = ""
	req_start: str = 'https://twitter.com/search?q='
	req_end: str = '&src=typed_query'

	for i in coins:
		search_req += f'{i}%20OR%20'

	return req_start + search_req + req_end


def get_tweets(search_phrase: str, days: int = 5, limit: int = 50) -> DataFrame:
	items = []
	df: DataFrame
	parser: TwitterParser = TwitterParser(
		limit=int(limit),
		search_phrase=search_phrase,
		for_days=int(days)
	)

	df = parser.search()

	if len(df.index) > 0:
		df['coin'] = search_phrase
		items.append(df)
	logger.debug(df)

	df = pd.concat(items)
	return df




if __name__ == "__main__":
	coins = send_get_request(apis_list.coinlist_url)['Data']
	search = convert_coins_to_twitter_search_request_url(coins[0:10])
	df = get_tweets('EKB')

	df.reset_index(drop=True, inplace=True)
	print(df)

	print(len(df))
	print(df.columns)
	logger.debug("That's it, beautiful and simple logging!")
