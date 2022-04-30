from typing import DefaultDict



toolbox_settings_path = "./toolbox_settings.ini"

bots_config_path = "./bot_configs/{bot_config_name}Config.json"

ignored_options: DefaultDict[str, DefaultDict[str, tuple[str, ...]]] = \
    DefaultDict(lambda: DefaultDict(lambda: ()))

ignored_options["MadHatterBot"]["Mad Hatter BBands"] = tuple([
    "MA Type",
    "Require FCC",
    "Reset Middle",
    "Allow Mid Sells"
])
