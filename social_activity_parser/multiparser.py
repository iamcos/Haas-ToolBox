"""Gets markets from Haas API, parse tweets, save to db and calculates santiments"""
from typing import Any
import apis_list
import pandas as pd
from pandas import DataFrame
from requests_html import HTMLSession
from twircy import twitter_parser as tp
import json
from loguru import logger


def get_tweets(search_phrase: str, days: int = 5, limit: int = 50) -> DataFrame:

	coins: list[str] = send_get_request()

    items = []
    df: DataFrame

    df = tp.search()

    if len(df.index) > 0:
        df['coin'] = search_phrase
        items.append(df)
    logger.debug(df)

    df = pd.concat(items)
    return df


def send_get_request(url: str) -> Any:
    session = HTMLSession()
    r = session.get(url)
    result = json.loads(r.text)
    return result


if __name__ == "__main__":
    coins = send_get_request(apis_list.coinlist_url)['Data']
    search = convert_coins_to_twitter_search_request_url(coins[0:10])
    df = get_tweets('EKB')

    df.reset_index(drop=True, inplace=True)
    print(df)

    print(len(df))
    print(df.columns)
    logger.debug("That's it, beautiful and simple logging!")
