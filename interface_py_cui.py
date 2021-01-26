import py_cui

from madhatter import MadHatterBot
from haasomeapi.dataobjects.custombots import BaseCustomBot

from functools import wraps



class MadHatterToolset(MadHatterBot):

	
	def __init__(self,master):
		MadHatterBot.__init__(self),
		self.master = master
		self.bot = None
		
		self.state = 'Menu'
		self.app_state()

	def return_bots(self):
		bl =self.return_botlist()
		bli = []
		for i, b in enumerate(bl):
				bli.append(f"{i}. {b.name} ROI: {b.roi}%")
		self.bots = bl
		return bl, bli
	
	def select_bot(self):
		
		bot = self.widg.bot_list.get()
		
		if bot is None:
			
			self.master.show_error_popup('No Item', 'You may have no Mad-Hatter Bots created in Haas. Create at least one. ')
			return
		# help(self.selected_bots)
		if bot not in self.widg.selected_bots.get_item_list():
			self.widg.selected_bots.add_item(bot)
			self.bot = self.bots[self.widg.bot_list.get_selected_item_index()]
			
		else:
			self.widg.selected_bots.remove_item(bot)
	
	
	def app_state(self):
		if self.state == "Menu":
			self.master.set_selected_widget(self.mh_toolbox_menu())
		elif self.state == "MH":
			self.bot_sellector_menu()
	
	def label(self):

			"""Generates ascii-art version of pyautogit logo

			Returns
			-------
			logo : str
					ascii-art logo
			"""
			
			logo = '        _    _ _______ ____   _____ _____ _______\n'
			logo = logo + '    /\\  | |  | |__   __/ __ \\ / ____|_   _|__   __|\n'
			logo = logo + '   /  \\ | |  | |  | | | |  | | |  __  | |    | |   \n'
			logo = logo + '  / /\\ \\| |  | |  | | | |  | | | |_ | | |    | |   \n'
			logo = logo + ' / ____ \\ |__| |  | | | |__| | |__| |_| |_   | |   \n'
			logo = logo + '/_/    \\_\\____/   |_|  \\____/ \\_____|_____|  |_|   \n'
			return logo
	
	def bot_sellector_menu(self):
		self.widg = self.master.create_new_widget_set(19,35)
		self.widg.add_block_label(self.label(),0, 0, row_span=9, column_span=6, center=False)
		c1 = self.widg.bot_list = self.master.add_scroll_menu('Bots', 0,2,row_span=4,column_span=2)
		c2 = self.widg.selected_bots = self.master.add_scroll_menu("selected bots",0,4,row_span=5,column_span=2)
		c3 = self.widg.bot_list.add_item_list(self.return_bots()[1])
		# c5 = self.widg.add_text_box('Title',0,4)
		c4 = self.widg.bot_list.add_key_command(py_cui.keys.KEY_ENTER, self.select_bot)

	def mh_toolbox_menu(self):
		self.new_widget_set = self.master.create_new_widget_set(9,6)
		c =  self.new_widget_set.add_label('MH MENU', 0, 3, row_span=1, column_span=2)

		c1 = self.new_widget_set = self.master.add_scroll_menu('Main Menu',0,0,row_span=4,column_span=2)
		c2 = self.new_widget_set.add_item_list(['Select Bot',
                                'Set BT starting date',
                                'Settings',
                                'Backtest selected Bot',
                                'Interactive BT',
                                'Stoploss',
                                'Finetune',
                                'Autocreate',
                                'About',
                                'Exit'])
		self.new_widget_set.set_color(py_cui.MAGENTA_ON_BLACK)

		print('is it the same?',self.new_widget_set.get() == "Select Bot")
		c3 = self.new_widget_set.add_key_command(py_cui.keys.KEY_ENTER, self.react_to_response)

		
	def react_to_response(self):
		self.response = self.new_widget_set.get()
		selection = self.response
	
		if selection is None:
			self.master.show_error_popup('No Item',
			                             'You may have Nothing selected. ')
			return 'NA'
		
		elif selection == "Select Bot":
			self.state = 'MH'
			self.widg
		elif selection == "Set BT starting date":
			pass
		elif selection == "Settings":
			pass
		elif selection == "Backtest selected Bot":
			pass
		elif selection == "Interactive BT":
			pass
		elif selection == "Stoploss":
			pass
		elif selection == "Finetune":
			pass
		elif selection == "Autocreate":
			pass
		elif selection == "About":
			pass
		elif selection == "Exit":
			pass
		elif selection == 'About':
			pass
		elif selection == 'Exit':
			pass

def main():
	root = py_cui.PyCUI(10, 8)
	root.set_title('CUI TODO List')
	# root
	mt = MadHatterToolset(root)
	
	
	root.start()
	
if __name__ == '__main__':
	main()



