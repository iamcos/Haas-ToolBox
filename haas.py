import configparser as cp
import os
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
import inquirer
import datetime
import pandas as pd
import time
from inquirer.themes import GreenPassion
class Haas:
    """
    Haasonline trading software interaction class: get botlist, marketdata,
    create bots and configure their parameters,
    initiate backtests and so forth can be done through this class
    """

    def __init__(self):
        self.config = cp.ConfigParser()
        self.bot = None
        self.bots = None
        self.ip = None
        self.secret = None
        self.check_config()
        self.c = self.client()
        
      

    def return_config(self):
        # print('CONFIG 1',self.config)
        return self.config

    def check_config(self):

        if not os.path.exists("config.ini"):
            self.get_server_data()

        else:
            # Read File
            self.config.read("./config.ini")

            ip = self.config["SERVER DATA"].get("server_address")
            secret = self.config["SERVER DATA"].get("secret")
            self.ip = ip
            self.secret = secret
            client = self.client()
            print(f'Connection status: {client.accountDataApi.get_all_wallets().errorCode.value}')
           
            if client.accountDataApi.get_all_wallets().errorCode.value == 100:
                print('Successfully connected!')
                print(f'there are {len(client.accountDataApi.get_all_wallets().result)} active wallets, '
                      f'{len(client.customBotApi.get_all_custom_bots().result)} custom bots system')
            elif client.accountDataApi.get_all_wallets().errorCode.value == 9002:
                for i in range(10):
                    print(f'Server may be offline...')
                    print(f'Retrying {i} out of 10')
                    time.sleep(5)
                    if client.accountDataApi.get_all_wallets().errorCode.value == 100:
                        break
            else:

                self.get_server_data()
                self.check_config()
            return client

    def client(self):
        self.init_config()
        config_data = self.config

        haasomeclient = HaasomeClient(self.ip, self.secret)
        return haasomeclient

    def write_file(self):
        self.config.write(open("config.ini", "w"))

    def init_config(self):
        # self.config = cp.ConfigParser().read('config.ini')
        # return .read('config.ini')‹#3  £
        pass

    def get_server_data(self):

        server_api_data = [
            inquirer.Text(
                "ip", "Type Haas Local api IP like so: 127.0.0.1", default="127.0.0.1"
            ),
            inquirer.Text(
                "port", "Type Haas Local api PORT like so: 8095", default="8095"
            ),
            inquirer.Text(
                "secret",
                "Type Haas Local Key (Secret) like so: 123",
            ),
        ]
        connection_data = inquirer.prompt(server_api_data,theme=GreenPassion())

        self.config["SERVER DATA"] = {
            "server_address": "http://"
                              + connection_data["ip"]
                              + ":"
                              + connection_data["port"],
            "secret": connection_data["secret"],
        }
        self.ip = self.config["SERVER DATA"].get("server_address")
        self.secret = self.config["SERVER DATA"].get("secret")
        self.write_file()

    def write_date(self):

        choices = [
            f"Write Year",
            f"Write month (current is {str(datetime.datetime.today().month)}): ",
            f"Write day (today is {str(datetime.datetime.today().day)}: ",
            f"Write  hour (now is {str(datetime.datetime.today().hour)}):",
            f"Write min (now {str(datetime.datetime.today().minute)}): ",
        ]

        date_q = [
            inquirer.Text("y", message=choices[0]),
            inquirer.Text("m", message=choices[1]),
            inquirer.Text("d", message=choices[2]),
            inquirer.Text("h", message=choices[3]),
            inquirer.Text("min", message=choices[4]),
        ]

        menu = [
            inquirer.List("response", message="Go through each step", choices=choices)
        ]
        answers = inquirer.prompt(date_q,theme=GreenPassion())

        self.config["BT DATE"] = {
            "year": answers["y"],
            "month": answers["m"],
            "day": answers["d"],
            "hour": answers["h"],
            "min": answers["min"],
        }

        self.write_file()
  
    def read_ticks(self):
        date_dict = {}

        try:
            for i in ["min", "hour", "day", "month", "year"]:
                date_dict[i] = self.config["BT DATE"].get(i)
        except Exception as e:
            print('read ticks', e)
            self.write_date()

        print(
            "BT date set to: ",
            date_dict["year"],
            date_dict["month"],
            date_dict["day"],
            date_dict["hour"],
            date_dict["min"],
        )
        dt_from = datetime.datetime(
            int(date_dict["year"]),
            int(date_dict["month"]),
            int(date_dict["day"]),
            int(date_dict["hour"]),
            int(date_dict["min"]),
        )

        delta = datetime.datetime.now() - dt_from
        delta_minutes = delta.total_seconds() / 60

        return int(delta_minutes)

    def bot_selector(self, botType, multi=False):

        bots = [x for x in self.c.customBotApi.get_all_custom_bots().result if x.botType == botType]
        # print(bots)
        bots.sort(key=lambda x:x.name,reverse=False)
        b2 = [
            (
                f"{i.name} {i.priceMarket.primaryCurrency}-{i.priceMarket.secondaryCurrency}, {i.roi}",
                i,
            )
            for i in bots
        ]
       
        if multi != True:
            question = [
                inquirer.List(
                    "bot",
                    message="Enter to select bot",
                    choices=b2,
                )
            ]
            try:
                selection = inquirer.prompt(question,theme=GreenPassion())
                self.bot = selection['bot']
            except Exception as e:
                print('Bot Selection error',e)
                # print('')


        else:
            question = [
                inquirer.Checkbox(
                    "bots",
                    message="Spacebar on bots to select. Enter to confirm selection",
                    choices=b2,
                )
            ]
        
            try:
                selection = inquirer.prompt(question,theme=GreenPassion())
                self.bots = selection['bots']
                return selection['bots']
            except Exception as e:
                print('Bot Selection error', e)
                # print('')
           

    def get_csv_files(self, path="./"):
        files = []
        for file in os.listdir(path):
            # if file.endswith(".csv") or file.endswith('.json'):
            if file.endswith(".csv"):
                files.append(os.path.join(path, file))
        return files

    def file_selector(self, path="."):
        files = self.get_csv_files(path)
        # print(files[0:5])
        question = [
            inquirer.List("file", "Please Select file from list: ", [i for i in files])
        ]

        selection = inquirer.prompt(question,theme=GreenPassion())
        self.file = selection["file"]
        self.configs = pd.read_csv(self.file)

        return self.file


    def trades_to_df(self,bot):
        print('Orders from bot',self.bot)
        completedOrders = [
            {
                "orderId":x.orderId,
                "orderStatus":x.orderStatus,
                "orderType":x.orderType,
                "price":x.price,
                "amount":x.amount,
                "amountFilled":x.amountFilled,
                "date":pd.to_datetime(x.unixAddedTime,unit="s"),
                }
            for x in self.bot.completedOrders
            ]
        
        orders_df = pd.DataFrame(completedOrders)
        return orders_df



def test():
    h = Haas()
    # print(h.__dict__)


if __name__ == '__main__':
    test()
