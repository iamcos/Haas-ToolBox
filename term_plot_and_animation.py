from terminalplot import plot_to_string, plot
from terminalplot import get_terminal_size
import asciichartpy
from pynimation import *
term_size = get_terminal_size()
from haas import Haas
print(term_size)
import pandas as pd
from marketdata import MarketData
md = MarketData()
ac = asciichartpy

# z = pd.read_csv('/Users/cosmos/Documents/GitHub/haasomeapitools/market_data/BINANCE-ADA-BKRW-1439.csv')
# z.Date = pd.to_datetime(z.Date)

h = Haas()
bo = h.return_bot_objects()
start_time = h.calculate_ticks_from_bot_trades(bo)
t = h.trades_to_df(bo)
print(len(t.index),' Trades start ',start_time )
print(t)
t.date = pd.to_datetime(t.date)
z = md.get_market_data(bo.priceMarket,bo.interval,start_time)
print(z)
# z['trades'] = 
print(ac.plot([z.Buy,t.price],cfg={'height':int(term_size[0]*0.88),}))