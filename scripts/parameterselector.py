from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance


def identify_interface_type(source):
	if type(source) == Safety:
		interface = source.safetyInterface
	if type(source) == Indicator:
		interface = source.indicatorInterface
	if type(source) == Insurance:
		interface = source.insuranceInterface
	return interface
	
def parameter_selector(self, interface):

	param_num = inquirer.select(
			message="Select Parameter",
			choices=[
					{"name": x.title, "value": i}
					for i, x in enumerate(interface)
			]
			+ ["Select another indicator"],
	).execute()
	print("selected_parameter number", param_num)

	return param_num


def get_param_value(interface, param_num):
	if interface[param_num].step == 1.0:
		value = int(interface[param_num].value)
	if interface[param_num].step == 0.1:
		value = round(float(interface[param_num].value), 1)
	if interface[param_num].step == 0.01:
		value = round(float(interface[param_num].value), 2)
		return value



def calculate_next_value(interface,param_num,direction):
	if direction == 0:
		value = get_param_value(interface,param_num)+interface[param_num].step
	if direction == 0:
		value = get_param_value(interface,param_num)+interface[param_num].step
	return value


def edit_param_value(api,tradebot,source,param_num, value):
	if type(source) == Safety:
		result = api.edit_bot_safety_settings(
								tradebot.guid,
								source.safety.guid,
								param_num,
								value
						).result
	if type(source) == Indicator:
		result = api.edit_bot_indicator_settings(
								tradebot.guid,
								source.guid,
								param_num,
								value
						).result
	if type(source) == Insurance:
		result = api.edit_bot_insurance_settings(
								tradebot.guid,
								source.guid,
								param_num,
								value
						).result
	return result

def backtest_bot(api,tradebot,interval):
		return api.backtest_trade_bot(tradebot.guid, interval).result


def iterate_parameter(api,tradebot,source,interface,param_num, interval):
	value = get_param_value(interface,param_num)
	value = calculate_next_value(value)
	action = inquirer.select(
			message="",
			choices=[
					Separator(
							f"{interface[param_num].title}:{interface[param_num].value} | step: {step} | ROI: {tradebot.roi}%"
					),
					Separator(f"Press right to backtest up"),
					Separator(f"Press left to backtest down"),
					Separator(f"Press '.' to backtest 10 steps down"),
					Separator(f"Press '.' to backtest 10 steps up"),
					"Select another parameter",
					"Select another indicator",
			],
	)
	@action.register_kb("right")
	def _(_):
			value = calculate_next_value(interface,param_num,0)
			edit_param_value(api, tradebot, source, param_num, value)
			tradebot = backtest_bot(api, tradebot, interval)

	@action.register_kb("left")
	def _(_):
			value = calculate_next_value(interface,param_num,1)
			edit_param_value(api, tradebot, source, param_num, value)
			tradebot = backtest_bot(api, tradebot, interval)

	@action.register_kb("escape")
	def _(_):
			pass
	@action.register_kb(",")
	def _(_):
		for i in range(10):
			self.edit_insurance(direction=1)
	@action.register_kb(".")
	def _(_):
		for i in range(10):
			self.edit_insurance(direction=0)
	kb_activate = True

	action.execute()
	print(action)
