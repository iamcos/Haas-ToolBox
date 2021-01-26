import stweet as st
import datetime
from arrow import Arrow
import pandas as pd
import re
from datetime import timedelta, date
class Twitter_Parser:
	
	def __init__(self, search_phrase, for_days = 14, limit=10000 , min_likes=0):
		
		self.for_days = Arrow.now().shift(days=-for_days)
		self.limit = limit
		self.min_likes = min_likes
		self.search_phrase = search_phrase
		self.tweets_collector = st.CollectorTweetOutput()
		
		
		# text Cleaners
		
		self.pat0 = r'\\(n|x..)'  # remove all unicode and emoji
		self.pat1 = r'@[A-Za-z0-9]+'  # remove any text with @ (links)
		self.comb1 = r'|'.join((self.pat0,self.pat1))
		self.pat2 = r'https?://[A-Za-z0-9./]+'  # remove all urls
		# r'^https?:\/\/.*[\r\n]*'
		self.comb2 = r'|'.join((self.comb1,self.pat2))
		self.pat3 = r'[^a-zA-Z0-9$.#]'  # remove every other character except a-z & 0-9 & $
		self.comb3 = r'|'.join((self.comb2,self.pat3))
	
	
	def parse_targets(self):
	 df = self.df
		
	
	def search(self):
		
		search_tweets_task = st.SearchTweetsTask(
			all_words=self.search_phrase,
			tweets_limit=self.limit,
			since=self.for_days
			)
		st.TweetSearchRunner(
		    search_tweets_task=search_tweets_task,
				
		    tweet_outputs=[self.tweets_collector]
		).run()
		self.tweets = self.tweets_collector.get_scrapped_tweets()
		df = self.tweets_to_df()
		return df
	
	def tweets_to_df(self):
		
		df = pd.DataFrame(self.tweets)
		print(df)
		# df.created_at = pd.to_datetime(df.created_at)
		print('Total Tweets collected: ',len(df.full_text))
		df.full_text = df.full_text.apply(lambda x: re.sub(self.comb3, ' ', x).lower())
		# df = df.full_text.apply(lambda x:x not in ['reached'])
		df.full_text.to_csv(f'{self.search_phrase}.csv')
		print(f'Tweets > {self.min_likes} likes: {len(df.full_text)} are saved to "{self.search_phrase}.csv"')
		self.df = df
		return df

	
def main():
	search_terms = 'buy sell target binance'
	df = Twitter_Parser(search_phrase=search_terms,for_days=2).search()
	df.reset_index(inplace=True)
	# df.dropna(axis='columns',inplace=True)
	# print(df.columns)
	df2 = pd.merge(left=df.created_at,right=df.full_text,on=df.index)
	# print(df2.head(n = 10).values)


if __name__ == '__main__':
	main()