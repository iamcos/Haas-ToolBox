import py_cui


class CliManager:
	def __init__(self,master):
		self.master = master

	
	
	def menu1(self):
		ws = self.master.create_new_widget_set(8,6)
		
		sm = ws.add_scroll_menu('One',0,0,row_span=2,column_span=2)
		sm.add_item_list(['Menu','Urusai','Harensasa'])
		self.ws = sm
		ws.add_key_command(py_cui.keys.KEY_ENTER,self.interact_with_menu())
		
	def interact_with_menu(self):
		selection = self.ws.get()
		if selection == 'Menu':
			self.menu2()
			self.master.apply_widget_set(self.ws)
		
		elif selection == 'Urusai':
		  self.menu3()
		  self.master.apply_widget_set(self.ws)



	def menu2(self):
		ws2 = self.master.create_new_widget_set(8,6)
		ws2.add_text_box('TEXT BOX',0,2,row_span=2,column_span=2,
		                         initial_text='Nothing here')
		self.ws = ws2
		return ws2

	def menu3(self):
		ws3 = self.master.create_new_widget_set(8,6)
		
		ws3.add_checkbox_menu('TEXT BOX',0,2,row_span=2,column_span=2)
		ws3.add_item_list(['Menu','Urusai','Harensasa'])
		self.ws = ws3
		return ws3


def main():
	mm = py_cui.PyCUI(20,10)
	mm.set_title('CUI TODO List')
	cm = CliManager(mm)
	cm.menu1()


if __name__ == "__main__":

	main()