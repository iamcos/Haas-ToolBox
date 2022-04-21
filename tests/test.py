from configparser import ConfigParser


config_parser: ConfigParser = ConfigParser()
config_parser.read('lalal')
print('data' in config_parser)

