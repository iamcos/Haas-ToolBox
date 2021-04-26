from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.apis.TradeBotApi import TradeBotApi
from InquirerPy import inquirer
from InquirerPy import get_style
import time
from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumInsurance import EnumInsurance
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumSafety import EnumSafety

from InquirerPy.separator import Separator
class TradeBotEditor:
  
  def select_tradebot(self):
    if len(self.tradebotapi.get_all_trade_bots().result)>0:
        tradebots = self.tradebotapi.get_all_trade_bots().result
    else:
        tradebots = None
    if tradebots != None:
        action= inquirer.select(
            message="Select Trade Bot",
            choices=[{"name": f"{x.name} | {EnumPriceSource(x.priceMarket.priceSource).name}", "value": x} for x in tradebots]+['Refresh Botlist'],
        ).execute()
        
        if action != 'Back'or 'Refresh Botlist':
            
            return action
        else:
            pass
    else:
        print('NO TRADE BOT DETECTED! Please creat one by hand')
        action= inquirer.select(
            message="Select Trade Bot",
            choices=[Separator("NO TRADE BOT DETECTED! Please creat one by hand "),'Refresh Botlist',
            ]
        ).execute()
        if action == 'Refresh Botlist':
            pass
        
  def interface_selector(self):
    while True:
        if self.tradebot:
            if len(self.tradebot.indicators) > 0:
                indicator_choices = [Separator(""),Separator("Indicators:")]+[{"name": f"  {EnumIndicator(y.indicatorType).name}", "value": y}
                        if y.enabled == True
                        else Separator(f"  {EnumIndicator(y.indicatorType).name} DISABLED")
                        for x, y in self.tradebot.indicators.items()]
                    
            else:
                indicator_choices = [Separator(""),Separator("No Indicators to select"),Separator("")]
            if len(self.tradebot.insurances) > 0:
                insurance_choices = [[Separator(""), Separator("Insurances:")]+{"name": f"  {EnumInsurance(y.insuranceType).name}", "value": y}
                if y.enabled == True else Separator(f"  {EnumInsurance(y.insuranceType).name} DISABLED") for x, y in self.tradebot.insurances.items() if hasattr(y,"step")
                ]
            else:
                insurance_choices = [Separator(""),Separator("No Insurances to select"),Separator("")]
            if len(self.tradebot.safeties) > 0:
                safety_choices = [Separator(""), Separator("Safeties:")]+[{"name": f"  {EnumSafety(y.safetyType).name}", "value": y}
                if y.enabled == True else Separator(f"  {EnumSafety(y.safetyType).name} DISABLED") for x, y in self.tradebot.safeties.items()
                ]
            else:
                safety_choices = [Separator(""),Separator("No Safeties to select"),Separator("")]
            action = inquirer.select(
                    message="Select Interface:",
                    choices=indicator_choices+insurance_choices+safety_choices+[Separator(""),"Back"],
                    style=get_style({"seprator": "#658bbf bg:#ffffff"}),
                )

            kb_activate = True
            interface = action.execute()
            if interface == "Back":
                interface = None
                self.select_interface()
            else:
                return interface
                
  def read_interface(self,source):
    if type(source) == Safety:
      interface = source.safetyInterface
    if type(source) == Indicator:
      interface = source.indicatorInterface
    if type(source) == Insurance:
      interface = source.insuranceInterface
    return interface
    
  def edit_interface(self,source):
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
          choices=[
              {"name": f"{i.title} : {i.value}", "value": i}
              for i in interface
          ]
          + ["Go back"],
      ).execute()
      print("selected_parameter number", interfaceParameters)
      return interfaceParameters

    
  def get_param_value(self, selectedInterfaceParameter):
    if selectedInterfaceParameter.step == 1.0:
      value = int(float(selectedInterfaceParameter.value))
    if selectedInterfaceParameter.step == 0.1:
      value = round(float(selectedInterfaceParameter.value), 1)
    if selectedInterfaceParameter.step == 0.01:
      value = round(float(selectedInterfaceParameter.value), 2)
    return value
  
  def get_param_step(self, selectedInterfaceParameter):
    if selectedInterfaceParameter.step == 1.0:
      step = int(selectedInterfaceParameter.step)
    if selectedInterfaceParameter.step == 0.1:
      step = round(float(selectedInterfaceParameter.step), 1)
    if selectedInterfaceParameter.step == 0.01:
      step = round(float(selectedInterfaceParameter.step), 2)
    return step


  def calculate_next_value(self,value,step,direction):
    
    if direction == 0:
      new_value = value+step
    if direction == 1:
      new_value = value-step
    return new_value


  def edit_param_value_new(self,api, interface, tradebot, param_num, new_val,):
    result = api(tradebot.guid, interface.guid, param_num, new_val)
    # print(result.errorCode, result.errorMessage)
    return result.result

  def backtest_bot(self,tradebot,interval):
      tradebot = self.c.tradeBotApi.backtest_trade_bot(tradebot.guid, interval).result
      # print(f"ROI: {tradebot.roi}                   ")
      return tradebot

  def iterate_parameter(self,interface,selectedInterfaceParmeter,param_num):
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
              "Select another parameter",
          ],
      )
      @action.register_kb("right")
      def _(_):
          self.value = self.calculate_next_value(self.value,step, 0)
          api = self.edit_interface(interface)
          tradebot = self.edit_param_value_new(api,interface,self.tradebot, param_num, self.value)
          tradebot= self.backtest_bot(self.tradebot, self.ticks)
          print(f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  ")
      @action.register_kb("left")
      def _(_):
          self.value = self.calculate_next_value(self.value,step,1)
          api = self.edit_interface(interface)
          tradebot= self.edit_param_value_new(api,interface,self.tradebot, param_num, self.value)
          tradebot = self.backtest_bot(self.tradebot, self.ticks)
          print(f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  ")
          
      @action.register_kb("escape")
      def _(_):
          pass
      @action.register_kb(",")
      def _(_):
        for i in range(10):
          self.value = self.calculate_next_value(self.value,step,1)
          api = self.edit_interface(interface)
          tradebot= self.edit_param_value_new(api,interface,self.tradebot, param_num, self.value)
          tradebot = self.backtest_bot(self.tradebot, self.ticks)
          print(f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  ")
      @action.register_kb(".")
      def _(_):
        for i in range(10):
          self.value = self.calculate_next_value(self.value,step,0)
          api = self.edit_interface(interface)
          tradebot= self.edit_param_value_new(api,interface,self.tradebot, param_num, self.value)
          tradebot = self.backtest_bot(self.tradebot, self.ticks)
          print(f"{selectedInterfaceParmeter.title} : {self.value} ROI:{tradebot.roi}%                  ")
      kb_activate = True

      action = action.execute()
      if action == "Select another parameter":
        self.select_interface()
      print(action)


