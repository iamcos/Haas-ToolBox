

import os

keys = list(os.environ.keys())

os.environ['FOO'] = 'bar'
os.environ['TG_ID'] = '1116068'
os.environ['TG_HASH'] = '632cfe2e90ccf2e1bb50c34380c9864d'
os.environ['TG_BOT_KEY'] = '952803998:AAEBqnO0C7zrHv6oQB3lormOGFAjnLBiwk4'
os.environ['NEWS_API'] = '6903ab8f0c034ba3bd4e7a4c8ecf7dd0'
os.environ['TW_EMAIL'] = 'garrypotterr@gmail.com'
os.environ['TW_PASS'] = 'j7S5LlAvuN0u99b9rnO3'

keys2 = list(os.environ.keys())
keys3 = []


for i in keys2:
    if i not in keys:
        keys3.append(i)
        print(f'export {i}={os.environ[i]}')
        os.popen(f'export {i}={os.environ[i]}')

# os.system('ls -l')