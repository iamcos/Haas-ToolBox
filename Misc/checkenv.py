import os

from decouple import config
# from dotenv import load_dotenv
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# print('load_dotenv',load_dotenv())
import os
# load_dotenv()

for i in os.environ.keys():
    print(i,os.environ.get(i))


print('then')
# tw = config('telgram_id')
# print(config('.').__dict__)
# print(os.getenv('tw_email'))
# config.search_path = '.'

print(config.__dict__)