from api.loader import log
from api.domain.types import Bot
from typing import cast
from InquirerPy.separator import Separator
from InquirerPy import inquirer

from api.providers.bot_api_provider import BotApiProvider


class BotSelectorCli:
    def __init__(self, api: BotApiProvider, bot_name: str) -> None:
        self._api: BotApiProvider = api
        self.bot_name: str = bot_name

    def select_bots(self) -> list[Bot]:
        log.info("Starting processing selecting bot..")

        bots_chain: list[dict[str, str | Bot]] = self._get_bots_chain()

        if not bots_chain:
            self._wait_bot_creating()
            return self.select_bots()

        return self._process_selecting_bot(bots_chain)

    def _process_selecting_bot(
            self,
            bots_chain: list[dict[str, Bot | str]]
    ) -> list[Bot]:
        actions: list[Bot | str] = inquirer.select(
                message=f"Select {self.bot_name}. "
                        + "You can choose multiple bots with pressing space",
            choices=[*bots_chain, "Refresh Botlist"],
            multiselect=True
        ).execute()

        for action in actions:
            if type(action) is str:
                return self.select_bots()

        return cast(list[Bot], actions)

    def _get_bots_chain(self) -> list[dict[str, Bot | str]]:
        return [
            {
                "name": f"{bot.name} {bot.priceMarket.primaryCurrency}/"
                        + f"{bot.priceMarket.secondaryCurrency}",
                "value": bot
            }
            for bot in self._api.get_all_bots()
        ]

    def _wait_bot_creating(self) -> None:
        msg: str = f"NO {self.bot_name} DETECTED! Please create one by hand"

        while not self._api.get_all_bots():
            log.warning(msg)
            inquirer.select(
                message=f"Select {self.bot_name}. "
                        + "You can choose multiple bots with pressing space",
                choices=[
                    Separator(msg),
                    "Refresh bots list",
                ],
            ).execute()

        log.info(f"{self.bot_name} detected!")

