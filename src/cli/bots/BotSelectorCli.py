from api.bots.BotManager import BotManager
from api.bots.BotApiProvider import Bot
from loguru import logger as log
from typing import cast
from InquirerPy.separator import Separator
from InquirerPy import inquirer


class BotSelectorCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager
        self.bot_name: str = manager.bot_name()

    def select_bots(self) -> list[Bot]:
        log.info("Starting processing selecting bot..")

        bots_chain: list[dict[str, str | Bot]] = self._get_bots_chain()

        if not bots_chain:
            self._wait_bot_creating()
            return self.select_bots()

        return self._process_selecting_bot(bots_chain)

    def choose_bot(self) -> None:
        if self.manager.bot_not_selected():
            log.info(f"{self.bot_name} isn't selected")
            bots: list[Bot] = self.select_bots()
            self.manager.set_bot(bots[0])
        else:
            log.info(f"{self.bot_name} selected")

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
            for bot in self.manager.get_available_bots()
        ]

    def _wait_bot_creating(self) -> None:
        msg: str = f"NO {self.bot_name} DETECTED! Please create one by hand"

        while not self.manager.get_available_bots():
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

