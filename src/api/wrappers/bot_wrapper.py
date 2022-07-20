from typing import Optional
from api.domain.types import Bot
from api.exceptions import BotWrapperException


class BotWrapper:
    def __init__(self, bot: Optional[Bot] = None) -> None:
        self._bot: Optional[Bot] = bot

    @property
    def bot(self) -> Bot:
        if self._bot is None:
            raise BotWrapperException("Internal bot is None")
        return self._bot

    @bot.setter
    def bot(self, bot: Bot) -> None:
        if bot is None:
            raise BotWrapperException("Can't set None bot")
        self._bot = bot

    @property
    def guid(self) -> str:
        if self._bot is None:
            raise BotWrapperException("Can't get GUID from None")
        return self._bot.guid

    @property
    def roi(self) -> float:
        if self._bot is None:
            raise BotWrapperException("Can't get ROI from None")
        return self._bot.roi

    @property
    def name(self) -> str:
        return ""

    def is_bot_selected(self) -> bool:
        return self._bot is None

