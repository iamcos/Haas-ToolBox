from haasomeapi.enums.EnumPriceSource import EnumPriceSource
import stweet as st
import arrow
import pandas as pd
from tw_ta import TW_TA
from marketdata import MarketData
from autoscraper unoirt AutoScraper
honoroble_mentions = 'SeddikFarid', 'WilliamHarmison', 'BitcoinMacro21', 'bti_trading', 'CryptoSignalD1', 'OxyBiz'

class TwitterParser:
	md = MarketData()
	as = AutoScraper()
	def account_parser(self, username, df):
		
		usernames = ['SeddikFarid', 'WilliamHarmison', 'BitcoinMacro21', 'bti_trading', 'CryptoSignalD1', 'OxyBiz']
		
		if username not in usernames:
			print('Twitter username is not yet parsable, please create a template for it manually or ask Cosmos for assistance')
			
		if username == 'bitpeaks':
	
	def get_tweets(self):
		username = "bitpeaks"
		since = arrow.now().shift(hours=-10)
		search_tweets_task = st.SearchTweetsTask(
				from_username=username,since=since
		)
		tweets_collector = st.CollectorTweetOutput()
		st.TweetSearchRunner(
				search_tweets_task=search_tweets_task,
				tweet_outputs=[tweets_collector]
		).run()

		tweets = tweets_collector.get_scrapped_tweets()

		df = pd.DataFrame(data = tweets)
		df.drop_duplicates('full_text', inplace=True)
		return df
		
		def parse_tweets_auto(self, tweets_df):
		

		result = as.build(html=driver, wanted_list=['Bitpanda,Binance'])
		
		def parse_tweets(self, tweets_df):
			parsed_tweets = []
				
			for i in df.index:
					time = df.created_at[i]
					# splitting text into actionable pices 
					signal, string = df.full_text[i].split('$')
					coin, string = string.split(' on #')
					exchange, string = string.split(" @ ")
					value, *string = string.split(' ')
					
					parsed_tweets.append([time.format('HH:mm'), signal, coin, exchange.upper(), float(value)])
			
			parsed_tweets = pd.DataFrame(data=parsed_tweets, columns=['time_of_prediction', 'signal', 'coin', 'exchange', 'price_prediction'])
			
			pms = []
			for i in parsed_tweets.index:
				try:
					exchange = int(EnumPriceSource.__getitem__(parsed_tweets.exchange[i]).value)
					priceMarket = md.return_priceMarket_object(EnumPriceSource(exchange).value, ticker = f"{parsed_tweets.coin[i]}USDT")
					pms.append(priceMarket[0])
				except Exception as e:
					# print(e)
					exchange = parsed_tweets.exchange[i]
			dfs =[]
			for priceMarket in pms:
				try:
					current_price = md.c.marketDataApi.get_price_ticker(
						EnumPriceSource(priceMarket.priceSource).value,
						priceMarket.primaryCurrency,
						priceMarket.secondaryCurrency,
						priceMarket.contractName,
					).result.currentBuyValue
				except Exception as e:
					current_price = None
				# print(priceMarket.primaryCurrency,current_price)
				df = parsed_tweets[parsed_tweets.coin == priceMarket.primaryCurrency].to_dict()
				df['obj'] = priceMarket
				df = pd.DataFrame(df)
				if current_price is not None:
					df['current_price'] = float(current_price)
					df['diff'] = df.price_prediction - df.current_price
				else:
					df['diff'] = None
					df['current_price'] = None
				df = df[['exchange','coin','signal','time_of_prediction','price_prediction','current_price','diff','obj']]

				dfs.append(df)
			dfss = pd.concat(dfs,ignore_index=True)
			return dfss.drop_duplicates(['coin']).reset_index(drop=True)

if __name__ == "__main__":
	tweets  = predictions = TwitterParser().get_tweets()
	
	
	# predictions.to_csv('twitter_signals.csv')
	
	twta = TW_TA()
	# d = twta.return_predictions_for_tweets(predictions)
	# df = pd.DataFrame(data=d,columns=['ticker','1m','5m','15m','1h','4h','1d','1W','1M'])
	# print(df)
	# df.to_csv('TW_predictions_for_twitter_coins.csv')
	
	
