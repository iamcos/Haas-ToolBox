import itertools
from api.providers.bot_api_provider import BotApiProvider
from api.domain.types import GUID, ROI, Bot
from api.wrappers.interface_wrapper import InterfaceWrapper
from api.wrappers.bot_wrapper import BotWrapper
from contextlib import contextmanager
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from typing import Generator, Protocol, Type, Optional


class BotManager(Protocol):
    def set_bot(self, bot: Bot) -> None: ...

    def refresh_bot(self) -> None: ...

    def is_bot_selected(self) -> bool: ...

    @contextmanager
    def new_bot(self) -> Generator: ...


class ApiV3BotManager:
    def __init__(self, provider: BotApiProvider) -> None:
        self._provider: BotApiProvider = provider
        self._bot_wrapper: BotWrapper = BotWrapper()

    def set_bot(self, bot: Bot) -> None:
        self._bot_wrapper.bot = bot

    def refresh_bot(self) -> None:
        self._bot_wrapper.bot = self._provider.get_refreshed_bot(
                self._bot_wrapper.bot.guid)

    def is_bot_selected(self) -> bool:
        return self._bot_wrapper.is_bot_selected()

    @contextmanager
    def new_bot(self) -> Generator:
        new_bot = self._bot_wrapper.bot
        clone_bot: Bot = self._provider.clone_and_save_bot(self._bot_wrapper.bot)
        self.set_bot(clone_bot)

        yield

        self._provider.delete_bot(clone_bot.guid)
        self.set_bot(new_bot)

    def _get_all_bot_options(self) -> tuple[IndicatorOption]:
        return tuple(itertools.chain(*[
            InterfaceWrapper(i).options
            for i in self._provider.get_all_bot_interfaces(self._bot_wrapper.guid)
        ]))

