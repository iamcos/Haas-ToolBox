"""Config for ignoring some options in CLI selection promt"""


from typing import DefaultDict


ignored_options: DefaultDict[str, DefaultDict[str, tuple[str, ...]]] = \
    DefaultDict(lambda: DefaultDict(lambda: ()))

ignored_options["Mad Hatter Bot"]["Mad Hatter RSI"] = tuple(["Length"])
ignored_options["Mad Hatter Bot"]["Mad Hatter BBands"] = tuple(["Length"])

