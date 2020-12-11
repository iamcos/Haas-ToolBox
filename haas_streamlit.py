import datetime
import os

import altair as alt
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from haasomeapi.enums.EnumPriceSource import EnumPriceSource

from haas import Haas
from marketdata import MarketData as md


# from elasticsearch import Elasticsearch as es

"""
Haas market data downloader and visualizer in a simple OHLC format via enabled
local-api  with help of Haasonline
trading software, haasomeapi and haasomeapitools libraries for data retrival and
Streamlit for visualisation.

"""


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

		
		def return_market(self):
				pass
	
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
		
		self.plot = fig
	
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
		marketdata = md().get_market_data(self.market,5,int(self.ticks / self.interval))
		try:
			marketdata.set_index(marketdata.Date,inplace=True)
		except Exception as e:
			print(e)
		# self.marketdata = marketdata = marketdata.resample("30min").mean()
		# print(marketdata)
		plot = self.plot_market_data(marketdata)
	
	def calculate_ticks_from_bot_trades(self):
		if len(self.bot.completedOrders) > 0:
			st.write(
				f"Selected bot {self.bot.name} has {len(self.bot.completedOrders)} trades"
				)
			trades_df = self.trades_to_df(self.bot)
			first_trade = trades_df.date.iloc[0]
			st.write(f"First trade date: {first_trade}")
			
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
		fig = self.plot
		for bot in self.bots:
			
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
		
		plot = st.plotly_chart(fig,userapi_check_token_response=True)
	
	
	def create_table(self):
		st.title("Let's create a table!")
		for i in range(1,10):
			cols = st.beta_columns(4)
			cols[0].write(f"{i}")
			cols[1].write(f"{i * i}")
			cols[2].write(f"{i * i * i}")
			cols[3].write("x" * i)
	
	def altair_chart(self):
		
		source = self.marketdata
		
		open_close_color = alt.condition("datum.open <= datum.close",
		                                 alt.value("#06982d"),
		                                 alt.value("#ae1325"))
		
		base = alt.Chart(source).encode(
			alt.X('Date:T',
			      axis=alt.Axis(
				      format='%m/%d/%h/%m',
				      labelAngle=-45,
				      title='Date'
				      )
			      ),
			# color=open_close_color
			)
		
		rule = base.mark_rule().encode(
			alt.Y(
				'Low:Q',
				title='Price',
				scale=alt.Scale(zero=False),
				),
			alt.Y2('High:Q')
			)
		
		bar = base.mark_bar().encode(
			alt.Y('Open:Q'),
			alt.Y2('Close:Q')
			)
		
		rule + bar
		st.write(rule + bar)
	
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
		
		pc = st.sidebar.selectbox('Coin',primcur.primarycurrency.unique())
		
		seccur = primcur[primcur.primarycurrency == pc]
		sc = st.sidebar.selectbox('Coin',seccur.secondarycurrency.unique())
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
		starting_date = st.sidebar.date_input('Select Start Date')
		starting_time = st.sidebar.time_input('Select Starting Time')
		get = st.sidebar.button('Get Data')
		if get:
			self._max_width_()
			self.calculate_ticks(datetime.datetime.combine(starting_date,starting_time))
			self.get_marketdata()
			st.plotly_chart(self.plot,use_container_width=True)

def plot_bot_trades_from_csv():
	str = StreamlitHaasTool()
	
	str.return_bot_objects()
	str._max_width_()
	str.get_market_data_for_bot()
	str.plot_bot_trades()
	str.altair_chart()
	str.fetch_data()




if __name__ == "__main__":
	
	str = StreamlitHaasTool()
	str.market_data_viewer()
