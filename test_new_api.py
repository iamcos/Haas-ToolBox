from haasomeapi_2.swagger_client import ApiClient, AccountAPIApi
from haasomeapi_2.swagger_client import Configuration
ac = ApiClient()
c = Configuration()


# for i in ac.__dict__:
# 		try:
# 				print(i,i.__dict__)
# 		except Exception as e:
#
# 				print(i)
# 		finally:
# 				try:
# 						print(i.keys())
# 				except Exception as e:
# 						print(e)
# # print(ac.configuration.__dict__)
c.api_key = 11111
c.username = 1
c.password = 1


# print(ac.configuration.__dict__)

acapi = AccountAPIApi()
acapi.api_client = ac
acapi.Configuration = c

		print(AccountAPIApi.get_all_wallets_with_http_info.__dict__)