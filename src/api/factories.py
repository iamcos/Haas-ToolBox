from typing import Callable, Type, cast

from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from api.backtesting.backtesting_cache import BacktestingCache, SetBacktestingCache
from api.backtesting.backtesting_strategy import BacktestingStrategy, FloatBacktestingStrategy, IntBacktestingStrategy
from api.backtesting.bot_backtester import ApiV3BotBacketster, BotBacktester
from api.backtesting.fine_tune_backtester import FineTuneBacktester
from api.backtesting.interface_fine_tune_backtester import InterfaceFineTuneBacktester
from api.loader import main_context
from api.bot_manager import ApiV3BotManager, BotManager

from api.domain.types import Bot
from api.exceptions import BacktestingStrategyCreationException, BotApiProviderCreationException
from api.providers.bot_api_provider import BotApiProvider
from api.providers.impl.mad_hatter_api_provider import MadHatterApiProvider
from api.providers.impl.scalper_api_provider import ScalperApiProvider
from api.providers.impl.trade_bot_api_provider import TradeBotApiProvider
from api.type_specifiers import get_bot_type


_api_providers: dict[Type[Bot], Callable[[], BotApiProvider]] = {
    TradeBot: (
        lambda: TradeBotApiProvider(main_context.trade_bot_api)
    ),
    MadHatterBot: (
        lambda: MadHatterApiProvider(main_context.haas.client.customBotApi)
    ),
    ScalperBot: (
        lambda: ScalperApiProvider(main_context.haas.client.customBotApi)
    ),
}


def get_provider(t: Type[Bot]) -> BotApiProvider:
    if t in _api_providers:
        return _api_providers[t]()

    raise BotApiProviderCreationException(
        f"Passed type {t} is wrong or not implemented"
    )


def get_bot_manager_by_type(bot_type: Type[Bot]) -> BotManager:
    return ApiV3BotManager(get_provider(bot_type))


def get_bot_manager_by_bot(bot: Bot) -> BotManager:
    bot_type: Type = type(bot)
    if bot_type is BaseCustomBot:
        bot_type = get_bot_type(bot)
        return get_bot_manager_by_type(bot_type)
    else:
        return get_bot_manager_by_type(bot_type)


def get_backtesting_strategy(value) -> BacktestingStrategy:
    if type(value) is int or str(value).replace(".0", "").isdigit():
        return IntBacktestingStrategy()
    elif type(value) is str and "." in value and value.replace(".", "").isdigit():
        return FloatBacktestingStrategy()
    elif type(value) is float:
        return FloatBacktestingStrategy()

    raise BacktestingStrategyCreationException(
        f"Strategy for {value} not implemented")


def get_bot_backtester(provider: BotApiProvider) -> BotBacktester:
    cache: BacktestingCache = SetBacktestingCache();
    return ApiV3BotBacketster(provider, cache, get_backtesting_strategy)


def get_fine_tune_backtester(
    provider_or_backtester: BotApiProvider | BotBacktester
) -> FineTuneBacktester:
    if type(provider_or_backtester) is BotApiProvider:
        provider_or_backtester = get_bot_backtester(provider_or_backtester)
    else:
        provider_or_backtester = cast(BotBacktester, provider_or_backtester)

    return FineTuneBacktester(provider_or_backtester)


def get_interface_fine_tune_backtester(
    provider: BotApiProvider
) -> InterfaceFineTuneBacktester:
    backtester: BotBacktester = get_bot_backtester(provider)
    fine_tune_backtester: FineTuneBacktester = get_fine_tune_backtester(
            backtester)
    return InterfaceFineTuneBacktester(fine_tune_backtester)

