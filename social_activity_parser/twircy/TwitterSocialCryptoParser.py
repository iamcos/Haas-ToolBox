from pandas.core.frame import DataFrame
import stweet as st
from arrow import Arrow
import pandas as pd
from loguru import logger as log
from stweet.model.tweet import Tweet
from stweet.search_runner.search_tweets_task import SearchTweetsTask
from stweet.tweet_output.collector_tweet_output import CollectorTweetOutput
from social_activity_parser.SocialCryptoParser import SocialCryptoParser
from social_activity_parser.twircy.ParserRequest import ParserRequest


class TwitterSocialCryptoParser(SocialCryptoParser):
	def __init__(self) -> None:
		super().__init__()
		self.tweets_collector: CollectorTweetOutput = st.CollectorTweetOutput()

	def parse_data(self, req: ParserRequest) -> DataFrame:
		"""Gets tweets by stweet as DataFrame"""

		search_tweets_task: SearchTweetsTask = st.SearchTweetsTask(
			all_words=req.search_phrase,
			tweets_limit=req.limit,
			since=Arrow.now().shift(days=-req.for_days)
		)

		st.TweetSearchRunner(
			search_tweets_task=search_tweets_task,
			tweet_outputs=[self.tweets_collector]
		).run()

		output: list[Tweet] = self.tweets_collector.get_scrapped_tweets()

		df: DataFrame = self._tweets_to_df(output)

		log.debug(f'Total Tweets collected: {len(output)}')

		return df

	def _tweets_to_df(self, tweets: list[Tweet]) -> DataFrame:
		df = pd.DataFrame(tweets)
		# TODO: Convert str lambda to correct datetime type
		df['created_at'] = df['created_at'].apply(lambda a: str(a))
		return df
