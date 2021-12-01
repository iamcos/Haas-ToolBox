
import json
import click
import pandas as pd
from requests_html import HTMLSession
from multiprocessing import Pool

import datetime


class TradingViewParser:

	def __init__(self):
		self.asset = "ETCUSDT" # can be exchange or ticker i.e. binance | btcusdt
		self.pages = 1 # how many pages to parse with selected asset
		self.current_page = 1  # nvm
		self.lang = 'ru'
		self.general_crypto_url1 = f"https://{self.lang}.tradingview.com/markets/cryptocurrencies/ideas/?sort=recent"
		self.general_crypto_url2 = f"https://{self.lang}.tradingview.com/markets/cryptocurrencies/ideas/page-{self.current_page}/?sort=recent"
		self.session = self.init_session()
	
	def validate_ticker(self):
		erroreous_title = "Page not found — TradingView"
		r = self.get_ideas_for_ticker()
		r_title = r.html.find('#title', first=True).text
		if r_title == erroreous_title:
			raise Exception ("Page not found, check your input data")
		else: 
			return f"{self.asset} TW page is being parsed"
	
	def return_all_languages(self,page):

		if self.current_page < 2:
			languages = page.html.find('.tv-dropdown-behavior__body tv-header__dropdown-body js-lang-dropdown-list-desktop i-hidden')
			
			print('langs 1',[i.attrs['vertical-align: inherit'].text for i in languages])
		else:
			print('langs 2', languages)
			print('langs 3',[i for i in languages])
			print('langs 1',[i.attrs['vertical-align: inherit'].text for i in languages])
	def init_session(self):
		session = HTMLSession() 

		if self.current_page:
			page = session.get(f"https://{self.lang}.tradingview.com/ideas/{self.asset}/?sort=recent"	)
			return page
		else:
			page = session.get(f"https://{self.lang}.tradingview.com/ideas/{self.asset}/page-{self.current_page}/?sort=recent"	)
			return page
				
	def return_cards(self, page):
		# print('page',page.html.find('.tv-feed__item '))
		cards = [card for card in page.html.find('.tv-feed__item') if card.attrs['data-widget-type'] == 'idea']
		return cards
			

	def get_username(self, page):
		username = page.html.find('.tv-user-link__wrap', first=True).attrs['data-username']
	
		return username

	def get_exchange_with_ticker(self, page):
		
		data= page.html.find('.tv-chart-view__symbol--desc', first=True)
		if data != None:
			exchange, ticker = data.text.split(':')
			return exchange, ticker
		else:
			return None, None

	def get_link(self, card):
		link = list(card.find('.tv-widget-idea__title-row', first=True).absolute_links)[0]
	
		return link
	
	def get_date(self, page):
		date = page.html.find('.tv-chart-view__title-time', first=True).attrs['data-timestamp']
		dt = datetime.datetime.utcfromtimestamp(int(float(date)))
		return dt

	def get_idea_page(self, link):
	
		idea_page = HTMLSession().get(link)
		# idea_page.html.render()
		return idea_page
		
	def get_likes(self,page):
		likes = page.html.find('.tv-card-social-item__count', first=True).text
		return int(likes)
	
	def get_comments(self, page):
		try:
			cmmts = []
			comment_page = page.html.find('#chart-view-comments', first=True)
			comments = comment_page.find('.tv-chart-comment')
			cmt = []
			
			for comment in comments:
				if comment != None:
					username = comment.find('.js-userlink-popup', first=True).attrs['data-username']
					text = comment.find('.js-chart-comment__text', first=True).text
					time = comment.find('.tv-chart-comment__time', first=True).attrs['data-timestamp']
					
					dt = datetime.datetime.utcfromtimestamp(int(float(time)))
					if comment.attrs['data-depth'] == 0:
							cmt = []
							cmt.append([username,text,dt])
					elif comment.attrs['data-depth'] == 1:
							cmt[-1].append([username, text, dt])
					elif comment.attrs['data-depth'] == 2:
							cmt[-1][-1].append([username, text, dt])
				cmmts.append(cmt)
			else:
				return []
			return cmmts
		except Exception as e:
			print(e)
			return None
			
	
	def get_decription(self, 	page):
		description_text = page.html.find('.tv-chart-view__description-wrap ', first=True).text
		if description_text == None:
			return None
		return description_text
		
	def get_direction(self, page):

			direction_data = page.html.find('.tv-idea-label', first=True)
			if direction_data != None:
				if direction_data.attrs['class'][1] == 'tv-idea-label--long':
					return 'long'
				elif direction_data.attrs['class'][1] == 'tv-idea-label--short':
					return 'short'
			else:
				return None	
			
	def  idea_to_df(self,page):
				
				data = {'ticker':self.get_exchange_with_ticker(page)[1], 'exchange':self.get_exchange_with_ticker(page)[0], 'text':self.get_decription(page), 'direction':self.get_direction(page),  'date':self.get_date(page),'user':str(self.get_username(page)),'likes':self.get_likes(page),'comments':str(self.get_comments(page))}
				return data

	def ideas_df(self,cards):
		dfs = []
		for card in cards:
			
			link = self.get_link(card)
			page = self.get_idea_page(link)
			data = self.idea_to_df(page)
			
			dfs.append(pd.DataFrame([data]))
		dfss = pd.concat(dfs)
		dfss.index = pd.to_datetime(dfss.date)
		dfss.drop('date',axis=1)
		return dfss
		
if __name__ == "__main__":

	lang = ['ru', 'en', 'de']
	for l in lang:
		tw = TradingViewParser()

		cardss = []
		tw.lang = l
		if tw.pages>1:
			for i in range(1, tw.pages):
			
			
				tw.current_page = i
				page = tw.init_session()
				# print(page.url)
				pgs = tw.return_all_languages(page)
				cards = tw.return_cards(page)
				cardss.extend(cards)
				result = tw.ideas_df(cardss)
				result.to_csv(f'TW_{tw.asset}_{tw.lang}__ideas.config')
				print(result)
		else:
				tw.current_page = 1
				page = tw.init_session()
				pgs = tw.return_all_languages(page)
				# print(page.url)
				cards = tw.return_cards(page)
				cardss.extend(cards)
				result = tw.ideas_df(cardss)
				result.to_csv('TW_{tw.asset}_{tw.lang}__ideas.config')
				print(result)
