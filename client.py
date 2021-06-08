class Client:
	
		def client(self):
			config_data = self.config

			haasomeclient = HaasomeClient(self.ip,self.secret)
			return haasomeclient