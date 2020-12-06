import datetime
import os
import json
import pandas as pd
import plotly.graph_objects as go

import streamlit as st

# from elasticsearch import Elasticsearch as es

from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumPriceSource import EnumPriceSource

from botdb import BotDB
from madhatter import MadHatterBot
from marketdata import MarketData as md
from haas import Haas

'''
Haas market data downloader and visualizer in a simple OHLC format via enabled local-api  with help of Haasonline
trading software, haasomeapi and haasomeapitools libraries for data retrival and Streamlit for visualisation.

'''


class StreamlitHaasTool(Haas):
		def __init__(self):
				Haas.__init__(self)
				self.market = None
				self.depth = None
				self.ticks = None
				self.bot = None
				self.bots = None
		
		def return_market(self):
				pass
		
		@st.cache()
		def fetch_data(self):
				get = st.sidebar.button('Get Data')
				if get:
						data = self.get_data()
						get = False
						return data
		
		def get_data(self):
				
				data = md().get_market_data(self.market,interval=self.interval,depth=int(self.depth))
				
				return data
		
		def _max_width_(self):
				max_width_str = f"max-width: 3000px;"
				st.markdown(
						f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>
        """,
						unsafe_allow_html=True,
						)
		
		def set_interval(self):
				interval = st.sidebar.selectbox(
						'Candle size',([1,2,3,4,5,6,10,12,15,20,30,45,60,90,120]),index=4)
				self.interval = interval
		
		def plot_market_data(self,marketdata):
				
				fig = go.Figure(data=[go.Candlestick
						(
						x=marketdata.index,
						opacity=0.7,
						open=marketdata['Open'],
						high=marketdata['High'],
						low=marketdata['Low'],
						close=marketdata['Close'],
						name=f"{self.market.primaryCurrency}/{self.market.secondaryCurrency}"
						)])
				fig.update_layout(
						title=f"{self.market.primaryCurrency}/{self.market.secondaryCurrency}",
						xaxis_title="Date",
						yaxis_title=f"Price ({self.market.secondaryCurrency})",
						font=dict(
								family="Courier New, monospace",
								size=12,
								color="black"
								)
						)
				
				self.plot = fig
		
		def return_bot_objects(self):
				files = []
				for file in os.listdir('./bt_results/'):
						# if file.endswith(".obj") or file.endswith('.json'):
						if file.endswith(".obj"):
								files.append(file)
				file = st.sidebar.selectbox('Select object file',files)
				print(file)
				# self.bot_objects = {}
				objects = pd.read_pickle(f'./bt_results/{file}')
				n = [[f'{x.name}| ROI: {x.roi}'][0] for x in objects]
				b = [x for x in objects]  # creates list of names
				dic = dict(zip(b,n))  # creates zipped obj/names list
				botobj = st.sidebar.selectbox('MH Bots: ',b,
				                              format_func=lambda x:dic[x])  # where b bot object returned from dic[x] name list
				st.write(botobj.name)
				self.bots = objects
				self.bot = botobj
		
		def get_market_data_for_bot(self):
				market_obj = self.bot.priceMarket
				self.market = market_obj
				if len(self.bot.completedOrders) > 0:
						trades_df = self.trades_to_df(self.bot)
						first_trade = trades_df.date.iloc[0]
						
						delta = datetime.datetime.now() - first_trade
						delta_minutes = delta.total_seconds() / 60
						self.ticks = delta_minutes
						marketdata = md().get_market_data(self.market,5,int(self.ticks / 5))
						try:
								marketdata.set_index(marketdata.Date,inplace=True)
						except Exception as e:
								print(e)
						marketdata = marketdata.resample('30min').mean()
						print(marketdata)
						plot = self.plot_market_data(marketdata)
				else:
						pass
		
		def plot_bot_trades(self):
				fig = self.plot
				for bot in self.bots:
						
						if not bot.completedOrders:
								fig.add_trace(go.Scatter(visible=False,x=[],y=[],mode='markers',
								                         name='Purchase Orders'))
								fig.add_trace(go.Scatter(visible=False,x=[],y=[],mode='markers',
								                         name='Sell Orders'))
						if len(bot.completedOrders) > 0:
								trades_df = self.trades_to_df(self.bot)
								trades_df.drop(['orderId','orderStatus','amountFilled'],axis=1,inplace=True)
								
								# print(trades_df)
								x_b = trades_df[trades_df.orderType == 0].date
								y_b = trades_df[trades_df.orderType == 0].price
								
								x_s = trades_df[trades_df.orderType == 1].date
								y_s = trades_df[trades_df.orderType == 1].price
								
								fig.add_trace(go.Scatter(
										x=x_b,
										y=y_b,
										mode='markers',
										name='Purchase Orders',
										marker_symbol="circle",
										marker_size=8,
										visible=False))
								
								fig.add_trace(go.Scatter(
										x=x_s,
										y=y_s,
										mode='markers',
										name='Sell Orders',
										marker_symbol="circle",
										marker_size=8,
										visible=False))
				fig.data[2].visible = True
				fig.data[1].visible = True
				
				
				
				plot = st.plotly_chart(fig,userapi_check_token_response=True)


def main():
		s = StreamlitHaasTool()
		
		bot = b.get_data()


if __name__ == '__main__':
		
		str = StreamlitHaasTool()
		str.return_bot_objects()
		str._max_width_()
		str.get_market_data_for_bot()
		str.plot_bot_trades()
