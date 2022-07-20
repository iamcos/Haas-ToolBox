import pytest

from collections import defaultdict
from typing import Type, cast

from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.marketdata.Market import Market
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from api.exceptions import TradeBotException
from api.providers.impl.trade_bot_api_provider import TradeBotApiProvider
from api.providers.bot_api_provider import BotApiProvider
from api.domain.types import GUID, ROI, Bot, Interface, InterfaceOption


class FakeTradeBot:
    def __init__(self, guid="guid"):
        self.guid: GUID = guid
        self.accountId: str = "accountId"
        self.name: str = "name"
        self.roi: ROI = 100.0

        priceMarket = Market()
        priceMarket.primaryCurrency = "primaryCurrency"
        priceMarket.secondaryCurrency = "secondaryCurrency"
        priceMarket.contractName = "contractName"
        self.priceMarket: Market = priceMarket

        self.leverage: float = 0.9
        self.indicators: defaultdict[str, Indicator] = defaultdict(Indicator)
        self.safeties: defaultdict[str, Safety] = defaultdict(Safety)
        self.insurances: defaultdict[str, Insurance] = defaultdict(Insurance)


class FakeTradeBotApi:
    _bots: tuple[FakeTradeBot] = tuple([
        FakeTradeBot()
        for _ in range(10)
    ]) 

    def __init__(self) -> None:
        self.rising: bool = False

    def get_all_trade_bots(self) -> HaasomeClientResponse:
        msg: str = "test get all trade bots"
        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS,
                    msg,
                    self._bots)

    def get_trade_bot(self, guid: GUID) -> HaasomeClientResponse:
        msg: str = "test get trade bot"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS,
                    msg,
                    FakeTradeBot())

    def edit_bot_indicator_settings(self, *args) -> HaasomeClientResponse:
        msg: str = "test edit bot indicator settings"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS, msg, None)

    def edit_bot_insurance_settings(self, *args) -> HaasomeClientResponse:
        msg: str = "test edit bot insurance settings"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS, msg, None)

    def edit_bot_safety_settings(self, *args) -> HaasomeClientResponse:
        msg: str = "test edit bot safety settings"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS, msg, None)

    def clone_trade_bot(self, *args) -> HaasomeClientResponse:
        msg: str = "test clone trade bot"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS, msg, FakeTradeBot(guid="another"))

    def remove_trade_bot(self, guid: GUID) -> HaasomeClientResponse:
        msg: str = "test edit bot safety settings"

        if self.rising:
            return HaasomeClientResponse(
                    EnumErrorCode.UNKNOWN_ERROR, msg, None)
        else:
            return HaasomeClientResponse(
                    EnumErrorCode.SUCCESS, msg, None)

    def backtest_bot(self, guid: GUID, ticks: int) -> HaasomeClientResponse:
        msg: str = "test edit bot safety settings"
        return HaasomeClientResponse(
                EnumErrorCode.SUCCESS, msg, None)


@pytest.fixture
def provider() -> BotApiProvider:
    api = FakeTradeBotApi()
    return TradeBotApiProvider(cast(TradeBotApi, api))


@pytest.fixture
def erroring_provider() -> BotApiProvider:
    api = FakeTradeBotApi()
    api.rising = True
    return TradeBotApiProvider(cast(TradeBotApi, api))


def test_gets_all_bots(provider: BotApiProvider) -> None:
    bots = provider.get_all_bots()
    assert bots == FakeTradeBotApi._bots


def test_fails_to_get_all_bots_on_api_error(
    erroring_provider: BotApiProvider
) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.get_all_bots()


def test_get_all_bot_interfaces(provider: BotApiProvider) -> None:
    after: tuple[Interface] = provider.get_all_bot_interfaces("guid")

    bot = FakeTradeBot();

    mustbe: tuple[Interface] = tuple([
            *bot.indicators.values(),
            *bot.insurances.values(),
            *bot.safeties.values()])

    msg: str = f"{after=}, {mustbe=}"

    assert after == mustbe, msg


def test_fails_to_get_all_bot_interfaces_on_api_error(
    erroring_provider: BotApiProvider
) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.get_all_bot_interfaces("guid")


def test_get_bot_interfaces_by_type(
    provider: BotApiProvider
) -> None:
    bot = FakeTradeBot()
    types: dict[str, Type[Interface]] = {
        "indicators": Indicator,
        "safeties": Safety,
        "insurances": Insurance
        }

    for name, t in types.items():
        after: tuple[Interface] = provider.get_bot_interfaces_by_type(
                "guid", t)

        mustbe: tuple[Interface] = tuple(
                getattr(bot, name).values())

        msg: str = f"{after=}, {mustbe=}"
        
        assert after == mustbe, msg


def test_get_bot_interfaces_by_type_works_with_bot(
    provider: BotApiProvider
) -> None:
    after: tuple[Interface] = provider.get_bot_interfaces_by_type(
            cast(Bot, FakeTradeBot()), Safety)

    mustbe: tuple[Interface] = tuple(FakeTradeBot().safeties.values())

    msg: str = f"{after=}, {mustbe=}"

    assert after == mustbe


def test_fails_to_get_bot_interfaces_by_type(
    erroring_provider: BotApiProvider
) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.get_bot_interfaces_by_type("guid", Indicator)


def test_get_refreshed_bot(provider: BotApiProvider) -> None:
    after: Bot = provider.get_refreshed_bot("guid")
    assert isinstance(after, FakeTradeBot)


def test_fails_to_get_refreshed_bot(erroring_provider: BotApiProvider) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.get_refreshed_bot("guid")


def test_update_bot_interface_option(provider: BotApiProvider) -> None:
    pass


def test_fails_to_update_bot_interface_option(
    erroring_provider: BotApiProvider
) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.update_bot_interface_option(InterfaceOption(), "")


def test_get_available_interface_types(provider: BotApiProvider) -> None:
    after: tuple[Type[Interface], ...] = \
            provider.get_available_interface_types()

    mustbe: tuple[Type[Interface], ...] = tuple([Indicator, Safety, Insurance])

    msg: str = f"{after=}, {mustbe=}"

    assert after == mustbe, msg


def test_clone_bot_and_save(provider: BotApiProvider) -> None:
    before: Bot = cast(Bot, FakeTradeBot())
    print(before.priceMarket.primaryCurrency)
    after: Bot = provider.clone_and_save_bot(before)

    msg: str = f"{before=}, {after=}"

    assert before.guid != after.guid, msg


def test_fails_to_clone_bot_and_save(
    erroring_provider: BotApiProvider
) -> None:
    with pytest.raises(TradeBotException):
        erroring_provider.clone_and_save_bot(cast(Bot, FakeTradeBot()))


def test_delete_bot(provider: BotApiProvider) -> None:
    pass


def test_fails_to_delete_bot(erroring_provider: BotApiProvider) -> None:
    pass


def test_backtest_bot(provider: BotApiProvider) -> None:
    pass


def test_fails_to_backtest_bot(erroring_provider: BotApiProvider) -> None:
    pass


