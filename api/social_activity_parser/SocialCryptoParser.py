from pandas.core.frame import DataFrame
from api.social_activity_parser.twircy.ParserRequest import ParserRequest


class SocialCryptoParser:

	def parse_data(self, req: ParserRequest) -> DataFrame:
		raise NotImplementedError
