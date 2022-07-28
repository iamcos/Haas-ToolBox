from collections import defaultdict
from api.wrappers.interface_wrapper import InterfaceWrapper
import pytest

from api.providers.bot_api_provider import BotApiProvider
from api import factories

from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


@pytest.fixture
def mad_api():
    return factories.get_provider(MadHatterBot)


@pytest.fixture
def mad_guid(mad_api):
    bot_name = "testing_bot"
    for bot in mad_api.get_all_bots():
        if bot.name == bot_name:
            return bot.guid

    raise Exception(f"MadHatter bot with name {bot_name} not found")


@pytest.fixture
def mad_interfaces_names():
    return ("Mad Hatter MACD", "Mad Hatter RSI", "Mad Hatter BBands")

def test_get_all_bots(mad_api: BotApiProvider):
    bots = mad_api.get_all_bots();
    for bot in bots:
        assert(bot.botType == 15)


def test_get_all_bot_interfaces(mad_guid, mad_interfaces_names, mad_api: BotApiProvider):
    interfaces = mad_api.get_all_bot_interfaces(mad_guid)

    counters = defaultdict(lambda: 0);
    for interface in interfaces:
        name = InterfaceWrapper(interface).name
        counters[name] += 1

    assert len(interfaces) == 3
    for name in mad_interfaces_names:
        assert counters[name] == 1


def test_bot_interfaces_by_type(mad_guid, mad_interfaces_names, mad_api: BotApiProvider):
    interfaces = mad_api.get_bot_interfaces_by_type(mad_guid, Indicator)
    names = tuple([InterfaceWrapper(i).name for i in interfaces])
    assert names == mad_interfaces_names


def test_update_bot_interface_option_from_custom_class(
    mad_guid,
    mad_api: BotApiProvider
):
    option = IndicatorOption()



def test_update_bot_interface_option(mad_guid, mad_api: BotApiProvider):
    interfaces = mad_api.get_bot_interfaces_by_type(mad_guid, Indicator)
    interface = interfaces[0];
    wrapped = InterfaceWrapper(interface)
    options = wrapped.options
    interface_name = wrapped.name
    option = options[0];
    option.value = 15

    try:
        mad_api.update_bot_interface_option(mad_guid, interface_name, option)

        new_interface = mad_api.get_bot_interfaces_by_type(mad_guid, Indicator)[0]
        new_option = InterfaceWrapper(new_interface).options[0]

        assert new_option.value == '15'
    finally:
        option.value = 12
        mad_api.update_bot_interface_option(mad_guid, interface_name, option)


def test_get_available_interface_types(mad_api: BotApiProvider):
    types = mad_api.get_available_interface_types();
    assert types == (Indicator,)


def test_clone_and_save_bot(mad_api: BotApiProvider):
    pass


def test_get_refreshed_bot(mad_guid, mad_api: BotApiProvider):
    pass

