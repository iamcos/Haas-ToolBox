from api.domain.types import GUID, Bot, Interface, InterfaceOption
from api.exceptions import ScalperException
from re import sub
from typing import Any, Optional, Type, cast
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode


class ScalperApiProvider:
    def __init__(self, api: CustomBotApi) -> None:
        self._api: CustomBotApi = api

    def get_all_bots(self) -> tuple[ScalperBot, ...]:
        bots = self._process_error(
            self._api.get_all_custom_bots(), "Can't get bots list")
        res = tuple(bot for bot in bots if bot.botType == 3)
        return res

    def get_all_bot_interfaces(self, bot_guid: GUID) -> tuple[Interface, ...]:
        bot: ScalperBot = self.get_refreshed_bot(bot_guid)

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
        start.value = str(start_value)
        start.step = step_value

        return [start]


    def get_bot_interfaces_by_type(
        self,
        guid_or_bot: GUID | Bot,
        interface_type: Type[Interface]
    ) -> tuple[Interface, ...]:
        bot: ScalperBot
        if type(guid_or_bot) is GUID:
            bot = self.get_refreshed_bot(guid_or_bot)
        else:
            bot = cast(ScalperBot, guid_or_bot)

        if interface_type is Safety:
            stop_loss_value: float = bot.maxAllowedReverseChange
            return tuple([self._create_stop_loss(stop_loss_value)])
        elif interface_type is Indicator:
            target_percentage_value: float = bot.minimumTargetChange
            return tuple([
                self._create_target_percentage(target_percentage_value)])

        return self._process_error(f"{interface_type} type is not supported")


    def get_refreshed_bot(self, bot_guid: GUID) -> ScalperBot:
        response: HaasomeClientResponse = self._api.get_custom_bot(
            bot_guid, EnumCustomBotType.SCALPER_BOT
        )
        return self._process_error(response, "Error while refreshing bot")

    def update_bot_interface_option(
        self,
        bot_guid: GUID,
        interface_name: str,
        option: InterfaceOption
    ) -> None:
        bot: ScalperBot = self.get_refreshed_bot(bot_guid)

        if option.title == "Target Percentage":
            bot.minimumTargetChange = float(option.value)
        elif option.title == "Stop Loss":
            bot.maxAllowedReverseChange = float(option.value)
        else:
            self._process_error(f"Option with title {option.title} "
                                "is not supported")

        res = self._api.setup_scalper_bot(
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

        self._process_error(res, "Error in editing bot")

    def get_available_interface_types(self) -> tuple[Type[Interface], ...]:
        return tuple([Indicator, Safety])

    def clone_and_save_bot(self, guid_or_bot: GUID | Bot) -> Bot:
        if type(guid_or_bot) is GUID:
            bot = self.get_refreshed_bot(guid_or_bot)
        else:
            bot = cast(Bot, guid_or_bot)

        name: str = sub(r"\s\[.*\]", "", bot.name)

        res = self._api.clone_custom_bot(
            bot.accountId,
            bot.guid,
            EnumCustomBotType.SCALPER_BOT,
            f"{name} [{self.get_refreshed_bot(bot.guid).roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage
        )

        return self._process_error(res, "Clone bot error")

    def delete_bot(self, bot_guid: GUID) -> None:
        self._api.remove_custom_bot(bot_guid)

    def backtest_bot(self, bot_guid: GUID, ticks: int) -> None:
        self._api.backtest_custom_bot(bot_guid, ticks)

    def _process_error(
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

