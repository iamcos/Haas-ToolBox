import datetime
import os

import altair as alt
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
import streamlit as st
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from numpy.ma import arange

from haas import Haas
from marketdata import MarketData as md

import talib
from talib import MA_Type


# from elasticsearch import Elasticsearch as es

# """
# Haas market data downloader and visualizer in a simple OHLC format via enabled
# local-api  with help of Haasonline
# trading software, haasomeapi and haasomeapitools libraries for data retrival and
# Streamlit for visualisation.
#
# """


class StreamlitHaasTool(Haas):
	def __init__(self):
		Haas.__init__(self)

		self.market = None
		self.depth = None
		self.ticks = None
		self.bot = None
		self.bots = None
		self.interval = 5
		self.marketdata = None
		self.plot = None
		


	
	def fetch_data(self):
		get = st.sidebar.button("Get Data")
		
		if get:
			data = self.get_data()
			get = False
			return data
	
	def get_data(self):
		self.interval = self.bot.interval
		data = md().get_market_data(
			self.bot.pricemMarket,
			interval=self.interval,
			depth=int(self.ticks) / self.interval,
			)
		
		return data
	
	def _max_width_(self):
		max_width_str = f"max-width: 3000px;"
		max_height_str = f"max-height: 3000px;"
		st.markdown(
			f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str},{max_height_str}
        }}
        </style>
        """,
			unsafe_allow_html=True,
			)
	
	def set_interval(self):
		interval = st.sidebar.selectbox(
			"Candle size",
			([1,2,3,4,5,6,10,12,15,20,30,45,60,90,120]),
			index=4,
			)
		self.interval = interval
	
	def plot_market_data(self,marketdata):
		
		fig = go.Figure(
			data=[
				go.Candlestick(
					x=marketdata.index,
					opacity=0.7,
					open=marketdata["Open"],
					high=marketdata["High"],
					low=marketdata["Low"],
					close=marketdata["Close"],
					name=f"{self.market.primaryCurrency}/{self.market.secondaryCurrency}",
					
					)
				]
			)
		fig.update_layout(
			title=f"{self.market.primaryCurrency}/{self.market.secondaryCurrency}",
			xaxis_title="Date",
			yaxis_title=f"Price ({self.market.secondaryCurrency})",
			font=dict(family="Courier New, monospace",size=12,color="black"),
			autosize=True
			)
		# fig.update_traces(line_width=10,selector=dict(type='candlestick'))
		
		self.fig = fig
	
	def return_bot_objects(self):
		files = []
		for file in os.listdir("./bt_results/"):
			# if file.endswith(".obj") or file.endswith('.json'):
			if file.endswith(".obj"):
				files.append(file)
		file = st.sidebar.selectbox("Select object file",files)
		print(file)
		# self.bot_objects = {}
		objects = pd.read_pickle(f"./bt_results/{file}")
		n = [[f"{x.name}| ROI: {x.roi}"][0] for x in objects]
		b = [x for x in objects]  # creates list of names
		dic = dict(zip(b,n))  # creates zipped obj/names list
		botobj = st.sidebar.selectbox(
			"MH Bots: ",b,format_func=lambda x:dic[x]
			)  # where b bot object returned from dic[x] name list
		st.write(botobj.name)
		self.bots = objects
		self.bot = botobj
	
	def get_market_data_for_bot(self):
		market_obj = self.bot.priceMarket
		self.market = market_obj
		self.calculate_ticks_from_bot_trades()
		self.get_marketdata()
	
	@st.cache()
	def get_marketdata(self):
		if self.bot:
			self.interval = self.bot.interval
		marketdata = md().get_market_data(self.market,self.interval,int(self.ticks / self.interval))
		try:
			marketdata.set_index(marketdata.Date,inplace=True)
		except Exception as e:
			print(e)
		self.marketdata = marketdata
		plot = self.plot_market_data(marketdata)
	
	def calculate_ticks_from_bot_trades(self):
		if len(self.bot.completedOrders) > 0:
			st.write(
				f"{self.bot.name} has {len(self.bot.completedOrders)} trades"
				)
			trades_df = self.trades_to_df(self.bot)
			first_trade = trades_df.date.iloc[0]
			# st.write(f"First trade date: {first_trade}")
			
			delta = datetime.datetime.now() - first_trade
			delta_minutes = delta.total_seconds() / 60
			self.ticks = delta_minutes
		else:
			self.ticks = 100
			st.write(
				f"Selected bot {self.bot.name} has {len(self.bot.completedOrders)} trades"
				)
	
	def calculate_ticks(self,start_date):
		delta = datetime.datetime.now() - start_date
		delta_minutes = delta.total_seconds() / 60 / self.interval
		self.ticks = delta_minutes
	
	def plot_bot_trades(self):
		fig = self.fig
		bot = self.bot
		if not bot.completedOrders:
			fig.add_trace(
				go.Scatter(
					visible=False,
					x=[],
					y=[],
					mode="markers",
					name="Purchase Orders",
					)
				)
			fig.add_trace(
				go.Scatter(
					visible=False,x=[],y=[],mode="markers",name="Sell Orders"
					)
				)
		if len(bot.completedOrders) > 0:
			trades_df = self.trades_to_df(self.bot)
			trades_df.drop(
				["orderId","orderStatus","amountFilled"],axis=1,inplace=True
				)
			
			# print(trades_df)
			x_b = trades_df[trades_df.orderType == 0].date
			y_b = trades_df[trades_df.orderType == 0].price
			
			x_s = trades_df[trades_df.orderType == 1].date
			y_s = trades_df[trades_df.orderType == 1].price
			
			fig.add_trace(
				go.Scatter(
					x=x_b,
					y=y_b,
					mode="markers",
					name="Purchase Orders",
					marker_symbol="circle",
					marker_size=8,
					
					# stackgroup=bot.guid
					)
				)
			
			fig.add_trace(
				go.Scatter(
					x=x_s,
					y=y_s,
					mode="markers",
					name="Sell Orders",
					marker_symbol="circle",
					marker_size=8,
					
					# stackgroup=bot.guid
					)
				)

		# st.write(fig.data)
		# fig.data[2].visible = True
		# fig.data[1].visible = True
		self.fig = fig
		plot = st.plotly_chart(fig,use_container_width=True)

	
	@st.cache()
	def get_all_markets(self):
		mdd = md()
		return mdd.get_all_markets()
	
	def market_data_viewer(self):
		df = self.get_all_markets()
		
		n = [EnumPriceSource(x) for x in df.pricesource.unique()]
	
		
		pricesource = st.sidebar.selectbox("markets",n,format_func=lambda x:x.name)
		# print(pricesource)
		primcur = df[df.pricesource == pricesource.value]
		
		pc = st.sidebar.selectbox('Primary Coin',primcur.primarycurrency.unique())
		
		seccur = primcur[primcur.primarycurrency == pc]
		sc = st.sidebar.selectbox('Secondary Coin',seccur.secondarycurrency.unique())
		self.market = \
		df.marketobj[df.pricesource == pricesource.value][df.primarycurrency == pc][
			df.secondarycurrency == sc].values[0]
		intervals = [1,
		             2,
		             3,
		             4,
		             5,
		             6,
		             10,
		             12,
		             15,
		             20,
		             30,
		             45,
		             60,
		             90,
		             120,
		             150,
		             180,
		             240,
		             300,
		             600,
		             1200,
		             2400,
		             ]
		self.interval = st.sidebar.selectbox('Interval',intervals,key=self.interval)
		starting_date = st.sidebar.date_input('Select Start Date',value= datetime.datetime.now()-datetime.timedelta(days=1))
		starting_time = st.sidebar.time_input('Select Starting Time',value=datetime.datetime.now()-datetime.timedelta(hours=6))
		get = st.sidebar.button('Get Data')
		if get:
			self._max_width_()
			self.calculate_ticks(datetime.datetime.combine(starting_date,starting_time))
			self.get_marketdata()
			self.plot = st.plotly_chart(self.fig,use_container_width=True)
	
	def plot_bot_trades_from_csv(self):
		self.return_bot_objects()
		self._max_width_()
		self.get_market_data_for_bot()
		self.plot_bot_trades()
		
		
	def add_indicators(self):
		md = self.marketdata
		# md.ta.log_return(cumulative=True,append=True)
		# md.ta.percent_return(cumulative=True,append=True)
		# md.ta.strategy('All')
		# mama_short = md.mama(length=10,append=True)
		rsismall = md.ta.rsi(length=7,buy=10,sell=90,append=True)
		
		st.write(md.columns)
		st.write(md.tail())
		md.plot(figsize=(16,10))
		
		
	
	def plot_indicators(self):
		
		# st.write(fig.__dict__)
		self.fig.add_trace(go.Scatter(
			x=arange(0,1.0),
			y=self.marketdata['CUMLOGRET_1'],
			mode="markers",
			name= 'New indyuk',
			
		))
		# self.plot = st.plotly_chart(self.fig,use_container_width=True)
		
		
		
if __name__ == "__main__":
	str = StreamlitHaasTool()
	resp = st.sidebar.selectbox('Select', ['Ta-Lib','Plot Market Data','Plot Bot Trades'])
	if resp == 'Plot Bot Trades':
		str.plot_bot_trades_from_csv()
	if resp == 'Plot Market Data':
		str.market_data_viewer()
		str.add_indicators()
		str.plot_indicators()
	if resp == 'Ta-Lib':
		pass