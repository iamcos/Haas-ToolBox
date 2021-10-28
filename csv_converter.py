import pandas as pd

import texthero as hero
from texthero import preprocessing


custom_create_bots_from_csv = [preprocessing.fillna,
                   preprocessing.lowercase,
                   preprocessing.remove_whitespace,
                   preprocessing.remove_urls,
                   ]
df = pd.read_csv('TW_binance.csv')

df2 = df[df.direction == 'long'][df.exchange == 'BINANCE']


df2.cleaned_text = df2.text.pipe(hero.clean, custom_create_bots_from_csv)
df2.label = None
df2.clean = df2.cleaned_text
df2.label = None
columns = df2.columns
df3 = df2.drop(labels='clean',axis=0)
print(df3)
