from re import sub

from typing import Any, Callable, Optional, Type, cast
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from api.domain.dtos import InterfaceOptionInfo
from api.loader import main_context
from api.domain.types import GUID, Interface, Bot, InterfaceOption
from api.exceptions import ScalperException
from api.wrappers.interface_wrapper import InterfaceWrapper


class ScalperApiProvider:
    def __init__(self, api: CustomBotApi) -> None:
        self._api: CustomBotApi = api

    def get_all_bots(self) -> tuple[ScalperBot]:
        bots = self._process_error(
            self._api.get_all_custom_bots(), "Can't get bots list")
        res = tuple(bot for bot in bots if bot.botType == 3)
        return res

    def get_all_bot_interfaces(self, bot_guid: GUID) -> tuple[Interface, ...]:
        bot: ScalperBot = self.get_refreshed_bot(bot_guid)

        target_percentage_value: float = vars(bot)["minimumTargetChange"]
        stop_loss_value: float = vars(bot)["maxAllowedReverseChange"]

        return tuple([
            self._create_target_percentage(target_percentage_value),
            self._create_stop_loss(stop_loss_value)
        ])

    def _create_target_percentage(
        self,
        target_percentage_value: float
    ) -> Indicator:

        target_percentage: Indicator = Indicator()
        target_percentage.indicatorName = "Target Percentage"
        target_percentage.enabled = True # type: ignore
        target_percentage.guid = target_percentage.indicatorName
        target_percentage.indicatorInterface = self._create_options(
            target_percentage_value, 0.2
        )

        return target_percentage


    def _create_stop_loss(self, stop_loss_value: float) -> Safety:
        stop_loss: Safety = Safety()
        stop_loss.safetyName = "Stop loss"
        stop_loss.enabled = True # type: ignore
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
        start.value = start_value # type: ignore
        start.step = step_value # type: ignore

        return [start]


    def get_bot_interfaces_by_type(
        self,
        guid_or_bot: GUID | Bot,
        interface_type: Type[Interface]
    ) -> tuple[Interface]:

        guid: GUID

        if type(guid_or_bot) is GUID:
            guid = guid_or_bot
        elif "guid" in vars(guid_or_bot):
            guid = cast(Bot, guid_or_bot).guid
        else:
            raise ScalperException(
                    "GUID or Bot must be passed as guid_or_bot, "
                    f"got {guid_or_bot}")

        bot: ScalperBot = self.get_refreshed_bot(guid)

        if interface_type is Safety:
            stop_loss_value: float = bot.maxAllowedReverseChange
            return tuple([self._create_stop_loss(stop_loss_value)])
        elif interface_type is Indicator:
            target_percentage_value: float = bot.minimumTargetChange
            return tuple([
                self._create_target_percentage(target_percentage_value)])

        raise ScalperException(f"{interface_type} type is not supported")


    def get_refreshed_bot(self, bot_guid: GUID) -> ScalperBot:
        response: HaasomeClientResponse = self._api.get_custom_bot(
            bot_guid, EnumCustomBotType.SCALPER_BOT
        )
        return self._process_error(response, "Error while refreshing bot")

    def update_bot_interface_option(
        self,
        option: InterfaceOption,
        bot_guid: GUID
    ) -> None:
        bot: ScalperBot = self.get_refreshed_bot(bot_guid)
        option_info = self._get_option_info(option, bot_guid)

        if option_info.option_num == 1:
            bot.minimumTargetChange = float(option.value)
        elif option_info.option_num == 2:
            bot.maxAllowedReverseChange = float(option.value)
        else:
            raise ScalperException(
                f"No param with num {option_info.option_num}")

        self._api.setup_scalper_bot(
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

    def _get_option_info(
        self,
        option: InterfaceOption,
        bot_guid: GUID
    ) -> InterfaceOptionInfo:

        for interface in self.get_all_bot_interfaces(bot_guid):
            interface_wrapper: InterfaceWrapper = InterfaceWrapper(interface)
            options: tuple[InterfaceOption, ...] = interface_wrapper.options

            for opt_number, opt in enumerate(options):
                if opt.title == option.title: 
                    return InterfaceOptionInfo(
                            interface,
                            interface_wrapper.guid,
                            opt_number)

        raise ScalperException(f"Option {option} not found")

    def get_available_interface_types(self) -> tuple[Type[Interface], ...]:
        return tuple([Indicator, Safety])

    def clone_and_save_bot(self, bot: Bot) -> Bot:
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
        response: HaasomeClientResponse,
        message: str = "Scalper Error"
    ) -> Any:
        if response.errorCode is not EnumErrorCode.SUCCESS:
            raise ScalperException(
                f"{message}"
                f" [Error code: {response.errorCode} "
                f" Error message: {response.errorMessage}]"
            )

        return response.result

