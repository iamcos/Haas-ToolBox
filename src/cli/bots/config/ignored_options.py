"""Config for ignoring some options in CLI selection promt"""
from typing import DefaultDict


ignored_options: DefaultDict[str, DefaultDict[str, tuple[str, ...]]] = \
    DefaultDict(lambda: DefaultDict(lambda: ()))

ignored_options["MadHatterBot"]["Mad Hatter BBands"] = tuple([
    "MA Type",
    "Require FCC",
    "Reset Middle",
    "Allow Mid Sells"
])

