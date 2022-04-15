from re import sub

from typing import Any, Callable, Optional, Type
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from api.bots.BotApiProvider import BotApiProvider, BotException
from api.MainContext import main_context
from api.models import Interfaces, Bot
from loguru import logger as log


class ScalperException(BotException): pass


class ScalperApiProvider(BotApiProvider):
    def __init__(self) -> None:
        self.api: CustomBotApi = main_context.haas.client.customBotApi

    def get_all_bots(self) -> tuple[ScalperBot]:
        bots = self.process_error(
            self.api.get_all_custom_bots(), "Can't get bots list")
        res = tuple(bot for bot in bots if bot.botType == 3)
        return res

    def get_all_interfaces(self, guid: str) -> tuple[Interfaces, ...]:
        bot: ScalperBot = self.get_refreshed_bot(guid)

        target_percentage_value: float = vars(bot)["minimumTargetChange"]
        stop_loss_value: float = vars(bot)["maxAllowedReverseChange"]

        res = tuple([
            self._create_target_percentage(target_percentage_value),
            self._create_stop_loss(stop_loss_value)
        ])
        return res

    def _create_target_percentage(
        self,
        target_percentage_value: float
    ) -> Indicator:

        target_percentage: Indicator = Indicator()
        target_percentage.indicatorName = "Target Percentage"
        target_percentage.enabled = True
        target_percentage.guid = target_percentage.indicatorName
        target_percentage.indicatorInterface = self._create_options(
            target_percentage_value, 0.2
        )

        return target_percentage


    def _create_stop_loss(self, stop_loss_value: float) -> Safety:
        stop_loss: Safety = Safety()
        stop_loss.safetyName = "Stop loss"
        stop_loss.enabled = True
        stop_loss.guid = stop_loss.safetyName
        stop_loss.safetyInterface = self._create_options(
            stop_loss_value, 0.1
        )
        return stop_loss


    def _create_options(
        self,
        start_value: float,
        step_value: float
    ) -> list[IndicatorOption]:

        start: IndicatorOption = IndicatorOption()
        start.title = "Value"
        start.value = start_value
        start.step = step_value

        return [start]


    def get_interfaces_by_type(
        self,
        guid: str,
        t: Type[Interfaces]
    ) -> tuple[Interfaces]:
        bot: ScalperBot = self.get_refreshed_bot(guid)

        if t is Safety:
            stop_loss_value: float = bot.maxAllowedReverseChange
            return tuple([self._create_stop_loss(stop_loss_value)])
        elif t is Indicator:
            target_percentage_value: float = bot.minimumTargetChange
            return tuple([
                self._create_target_percentage(target_percentage_value)])
        
        return self.process_error(f"{t} type is not supported")


    def get_refreshed_bot(self, guid: str) -> ScalperBot:
        response: HaasomeClientResponse = self.api.get_custom_bot(
            guid, EnumCustomBotType.SCALPER_BOT
        )
        return self.process_error(response, "Error while refreshing bot")

    def edit_interface(
        self,
        interface: Interfaces,
        param_num: int,
        value: Any,
        bot_guid: str
    ) -> None:
        bot: ScalperBot = self.get_refreshed_bot(bot_guid)

        if param_num == 1:
            bot.minimumTargetChange = value
        elif param_num == 2:
            bot.maxAllowedReverseChange = value
        else:
            self.process_error(f"No param with num {param_num}")

        self.api.setup_scalper_bot(
			accountguid=bot.accountId,
			botguid=bot.guid,
			botname=bot.name,
			primarycoin=bot.priceMarket.primaryCurrency,
			secondarycoin=bot.priceMarket.secondaryCurrency,
			templateguid=bot.customTemplate,
			contractname=bot.priceMarket.contractName,
			leverage=bot.leverage,
			amountType=bot.amountType,
			tradeamount=bot.currentTradeAmount,
			position=str(bot.coinPosition),
			fee=bot.currentFeePercentage,
			targetpercentage=bot.minimumTargetChange,
			safetythreshold=bot.maxAllowedReverseChange,
		)


    def get_backtest_method(self) -> Callable:
        return self.api.backtest_custom_bot

    def process_error(
        self,
        response: Optional[HaasomeClientResponse | Any] = None,
        message: str = "Scalper Error"
    ) -> Any:
        if response is None:
            raise ScalperException(message)

        if type(response) is HaasomeClientResponse:
            if response.errorCode is not EnumErrorCode.SUCCESS:
                raise ScalperException(
                    f"{message}"
                    f" [Error code: {response.errorCode} "
                    f" Error message: {response.errorMessage}]"
                )

            return response.result

        return response

    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        return tuple([Indicator, Safety])

    def clone_bot_and_save(self, bot: Bot) -> Bot:
        name: str = sub(r"\s\[.*\]", "", bot.name)

        res = self.api.clone_custom_bot(
            bot.accountId,
            bot.guid,
            EnumCustomBotType.SCALPER_BOT,
            f"{name} [{self.get_refreshed_bot(bot.guid).roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage
        )

        return self.process_error(res, "Clone bot error")

    def delete_bot(self, bot_guid: str) -> None:
        self.api.remove_custom_bot(bot_guid)


