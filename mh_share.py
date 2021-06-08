from haas import Haas
from configsstorage import ConfigsManagment
from InquirerPy import inquirer
class ShareMH(Haas, ConfigsManagment):
	def share_mh(self):
		menu_options = [
			# "Create bots from CSV",
			"Create bots from OBJ",\
			"Save bots to OBJ file",
		]

		while True:
			response = inquirer.select('Choose:', menu_options).execute()
			
			if response == "Create bots from OBJ":
									self.create_bots_from_obj()
			if response == "Create bots from CSV":
									self.create_bots_from_csv()
			if response == "Save bots to OBJ file":
					bots = self.bot_selector(15, multi=True)
					self.save_bots_to_file(bots)    
if __name__ == "__main__":
    cm = ShareMH().share_mh()