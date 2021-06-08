from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from InquirerPy import inquirer
from InquirerPy import get_style
from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumInsurance import EnumInsurance
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumSafety import EnumSafety
from InquirerPy.separator import Separator
import pandas as pd


class TradeBotEditor:
    """ 
    Trade Bot parameter manipulation class.
    Responsible for Trade Bot selection, parameter selection,
    keyboard interface to change parameter values and backtest_bot
    
    """

    def select_tradebot(self):
        
        if len(self.tradebotapi.get_all_trade_bots().result) > 0:
            tradebots = self.tradebotapi.get_all_trade_bots().result
        else:
            tradebots = None
        if tradebots != None:
            action = inquirer.select(
                message="Select Trade Bot",
                choices=[
                    {
                        "name": f"{x.name} | {EnumPriceSource(x.priceMarket.priceSource).name}",
                        "value": x,
                    }
                    for x in tradebots
                ]
                + ["Refresh Botlist"],
            ).execute()

            if action != "Back" or "Refresh Botlist":

                return action
            else:
                pass
        else:
            print("NO TRADE BOT DETECTED! Please creat one by hand")
            action = inquirer.select(
                message="Select Trade Bot",
                choices=[
                    Separator("NO TRADE BOT DETECTED! Please creat one by hand "),
                    "Refresh Botlist",
                ],
            ).execute()
            if action == "Refresh Botlist":
                pass
    def select_interface(self):
        interface = self.interface_selector()
        param_interfaces = self.read_interface(interface)
        param_num = None
        if param_interfaces:
            selectedInterface = self.parameter_selector(param_interfaces)
            for i, x in enumerate(param_interfaces):
                if x.title == selectedInterface.title:
                    param_num = i

            self.tradebot = self.iterate_parameter(
                interface, selectedInterface, param_num
            )
    
    def return_interfaces_menu_options(self):
         if self.tradebot:
                if len(self.tradebot.indicators) > 0:
                    indicators_menu_top = [Separator(""), Separator("Indicators:")]
                    indicators_menu = [
                        {"name": f"  {EnumIndicator(y.indicatorType).name}", "value": y}
                        if y.enabled == True
                        else Separator(
                            f"  {EnumIndicator(y.indicatorType).name} DISABLED"
                        )
                        for x, y in self.tradebot.indicators.items()
                    ]
                    indicator_choices = indicators_menu_top + indicators_menu

                else:
                    indicator_choices = [
                        Separator(""),
                        Separator("No Indicators to select"),
                        Separator(""),
                    ]
                if len(self.tradebot.insurances) > 0:
                    insurance_choices = [
                        [Separator(""), Separator("Insurances:")]
                        + {
                            "name": f"  {EnumInsurance(y.insuranceType).name}",
                            "value": y,
                        }
                        if y.enabled == True
                        else Separator(
                            f"  {EnumInsurance(y.insuranceType).name} DISABLED"
                        )
                        for x, y in self.tradebot.insurances.items()
                        if hasattr(y, "step")
                    ]
                else:
                    insurance_choices = [
                        Separator(""),
                        Separator("No Insurances to select"),
                        Separator(""),
                    ]
                
                if len(self.tradebot.safeties) > 0:
                    print(self.tradebot.safeties[list(self.tradebot.safeties.keys())[0]].__dict__)
                    safety_choices = [Separator(""), Separator("Safeties:")] + [
                        {"name": f"  {EnumSafety(y.safetyType).name}", "value": y}
                        if y.enabled == True
                        else Separator(f"  {EnumSafety(y.safetyType).name} DISABLED")
                        for x, y in self.tradebot.safeties.items()
                    ]
                else:
                    safety_choices = [
                        Separator(""),
                        Separator("No Safeties to select"),
                        Separator(""),
                    ]
                    
                choices = indicator_choices + insurance_choices + safety_choices + [Separator(""), "Back"]
                    
                return choices
    

                
    def interface_selector(self):
    
            choices = self.return_interfaces_menu_options()
            
            action = inquirer.select(
                message="Select Interface:",
                choices = choices,
                style=get_style({"seprator": "#658bbf bg:#ffffff"}),
            )

            kb_activate = True
            interface = action.execute()
            
            
            return interface

    def read_interface(self, source):
        if type(source) == Safety:
            interface = source.safetyInterface
        if type(source) == Indicator:
            interface = source.indicatorInterface
        if type(source) == Insurance:
            interface = source.insuranceInterface
        return interface

    def edit_interface(self, source):
        if type(source) == Safety:
            api = self.c.tradeBotApi.edit_bot_safety_settings
        if type(source) == Indicator:
            api = self.c.tradeBotApi.edit_bot_indicator_settings
        if type(source) == Insurance:
            api = self.c.tradeBotApi.edit_bot_insurance_settings
        return api

    def parameter_selector(self, interface):

        interfaceParameters = inquirer.select(
            message="Select Parameter",
            choices=[{"name": f"{i.title} : {i.value}", "value": i} for i in interface],
        ).execute()
        print("selected_parameter number", interfaceParameters.__dict__)
        return interfaceParameters

    def get_param_value(self, selectedInterfaceParameter):
        if selectedInterfaceParameter.step == 1.0:
            value = int(float(selectedInterfaceParameter.value))
        if selectedInterfaceParameter.step == 0.1:
            value = round(float(selectedInterfaceParameter.value), 1)
        if selectedInterfaceParameter.step == 0.01:
            value = round(float(selectedInterfaceParameter.value), 2)
        if selectedInterfaceParameter.step == 0.001:
            value = round(float(selectedInterfaceParameter.value), 3)
        if selectedInterfaceParameter.step == 0.0001:
            value = round(float(selectedInterfaceParameter.value), 4)
        if selectedInterfaceParameter.step == 0.00001:
            value = round(float(selectedInterfaceParameter.value), 5)
        if selectedInterfaceParameter.step == 0.000001:
            value = round(float(selectedInterfaceParameter.value), 6)
        if selectedInterfaceParameter.step == 0.0000001:
            value = round(float(selectedInterfaceParameter.value), 7)
        if selectedInterfaceParameter.step == 0.00000001:
            value = round(float(selectedInterfaceParameter.value), 8)
        if selectedInterfaceParameter.step == 0.000000001:
            value = round(float(selectedInterfaceParameter.value), 9)
        return value

    def get_param_step(self, selectedInterfaceParameter):
        if selectedInterfaceParameter.step == 1.0:
            step = int(selectedInterfaceParameter.step)
        if selectedInterfaceParameter.step == 0.1:
            step = round(float(selectedInterfaceParameter.step), 1)
        if selectedInterfaceParameter.step == 0.01:
            step = round(float(selectedInterfaceParameter.step), 2)
        if selectedInterfaceParameter.step == 0.001:
            step = round(float(selectedInterfaceParameter.step), 3)
        if selectedInterfaceParameter.step == 0.0001:
            step = round(float(selectedInterfaceParameter.step), 4)
        if selectedInterfaceParameter.step == 0.00001:
            step = round(float(selectedInterfaceParameter.step), 5)
        if selectedInterfaceParameter.step == 0.000001:
            step = round(float(selectedInterfaceParameter.step), 6)
        if selectedInterfaceParameter.step == 0.0000001:
            step = round(float(selectedInterfaceParameter.step), 7)
        if selectedInterfaceParameter.step == 0.00000001:
            step = round(float(selectedInterfaceParameter.step), 8)
        if selectedInterfaceParameter.step == 0.000000001:
            step = round(float(selectedInterfaceParameter.step), 9)
        return step

    def calculate_next_value(self, value, step, direction):

        if direction == 0:
            new_value = value + step
        if direction == 1:
            new_value = value - step
        return round(new_value, 4)

    def edit_param_value(
        self,
        api,
        interface,
        tradebot,
        param_num,
        new_val,
    ):
        result = api(tradebot.guid, interface.guid, param_num, new_val)
        # print(result.errorCode, result.errorMessage)
        return result.result

    def backtest_bot(self, tradebot, interval):
        tradebot = self.c.tradeBotApi.backtest_trade_bot(tradebot.guid, interval).result
        return tradebot

    def iterate_parameter(self, interface, selectedInterfaceParmeter, param_num):
        used_values = []
        value_roi = []
        self.value = self.get_param_value(selectedInterfaceParmeter)
        step = self.get_param_step(selectedInterfaceParmeter)
        action = inquirer.select(
            message="",
            choices=[
                Separator(
                    f"{selectedInterfaceParmeter.title}:{selectedInterfaceParmeter.value} | step: {selectedInterfaceParmeter.step} | ROI: {self.tradebot.roi}%"
                ),
                Separator(f"Press right to backtest up"),
                Separator(f"Press left to backtest down"),
                Separator(f"Press '.' to backtest 10 steps down"),
                Separator(f"Press '.' to backtest 10 steps up"),
                Separator(f"Press '=' - backtesting length X 2"),
                Separator(f"Press '-' - backtesting length \/ 2"),
            "Select another parameter",
            ],
        )

        @action.register_kb("right")
        def _(_):
            
            self.value = self.calculate_next_value(self.value, step, 0)
            while self.value in used_values:
                self.value = self.calculate_next_value(self.value, step, 0)
            api = self.edit_interface(interface)
            tradebot = self.edit_param_value(
                api, interface, self.tradebot, param_num, self.value
            )
            tradebot = self.backtest_bot(self.tradebot, self.ticks)
            print(
                f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  "
            )
            if float(tradebot.roi) != 0.0:
                value_roi.append([float(tradebot.roi),self.value,self.ticks])
            used_values.append(self.value)

        @action.register_kb("left")
        def _(_):
            self.value = self.calculate_next_value(self.value, step, 1)
            while self.value in used_values:
                self.value = self.calculate_next_value(self.value, step, 1)
            api = self.edit_interface(interface)
            tradebot = self.edit_param_value(
                api, interface, self.tradebot, param_num, self.value
            )
            tradebot = self.backtest_bot(self.tradebot, self.ticks)
            print(
                f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  "
            )
            value_roi.append([float(tradebot.roi),self.value])
            used_values.append(self.value)

        @action.register_kb("escape")
        def _(_):
            pass
        @action.register_kb("=")
        def _(_):
            self.ticks = int(self.ticks * 2)
            print(self.ticks,'                           ')
        @action.register_kb("-")
        def _(_):
            self.ticks = int(self.ticks/2)
            print(self.ticks,'\n')

        @action.register_kb(",")
        def _(_):
            for i in range(10):
                self.value = self.calculate_next_value(self.value, step, 1)
                while self.value in used_values:
	                self.value = self.calculate_next_value(self.value, step, 1)
                api = self.edit_interface(interface)
                tradebot = self.edit_param_value(
                    api, interface, self.tradebot, param_num, self.value
                )
                tradebot = self.backtest_bot(self.tradebot, self.ticks)
                print(
                    f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  "
                )
                value_roi.append([float(tradebot.roi),self.value])
                used_values.append(self.value)

        @action.register_kb(".")
        def _(_):
            for i in range(10):
                self.value = self.calculate_next_value(self.value, step, 0)
                while self.value in used_values:
	                self.value = self.calculate_next_value(self.value, step, 0)
                api = self.edit_interface(interface)
                tradebot = self.edit_param_value(
                    api, interface, self.tradebot, param_num, self.value
                )
                tradebot = self.backtest_bot(self.tradebot, self.ticks)
                print(
                    f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  "
                )
                value_roi.append([float(tradebot.roi),self.value])
                used_values.append(self.value)

        kb_activate = True

        action = action.execute()
        if action == "Select another parameter":
            if len(value_roi)>0:
                value = sorted(value_roi, key=lambda x: x[0], reverse=True)
                print(value)
                api = self.edit_interface(interface)
                self.tradebot = self.edit_param_value(
                        api, interface, self.tradebot, param_num, value[0][1]
                    )
                # self.value = value
                self.select_interface()
        elif action == "Set best value by ROI":
            if len(value_roi)>0:
                value = sorted(value_roi, key=lambda x: x[0], reverse=True)
                api = self.edit_interface(interface)
                self.tradebot = self.edit_param_value(
                        api, interface, self.tradebot, param_num, value[0][1]
                    )
                # self.value = value
                print(value)
                self.select_interface()
