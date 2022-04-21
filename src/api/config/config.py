from typing import Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot

toolbox_settings_path = "./toolbox_settings.ini"

custom_bot_types: dict[int, Type] = dict({
    3: ScalperBot,
    15: MadHatterBot
})
