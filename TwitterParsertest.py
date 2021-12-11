from social_activity_parser.twircy.TwitterParser import TwitterParser
from social_activity_parser.twircy.TwitterRequest import TwitterRequest
import pandas as pd

def main():
	search_terms = 'buy sell target binance'

	df = TwitterParser(TwitterRequest(search_terms)).search()
	df = df.reset_index(inplace=True)
	# df.drop(axis='columns',inplace=True)
	# print(df.columns)
	# df2 = pd.merge(left=df.created_at, right=df.full_text, on=df.index)
	# print(df2.head(n = 10).values)


if __name__ == '__main__':
	main()
