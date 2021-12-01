from bots.mad_hatter.mad_hatter_bot import MadHatterBot
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType

mh = MadHatterBot()
botlist = mh.return_bots_by_15_type()
botlist_guid = [x.guid for x in botlist]
print(botlist)


def test_return_botlist():
    assert botlist[0]


bot = botlist[0]

mh.ticks = 600
mh.bot = bot


def test_create_mh():
    name = 'Test Bot'

    new = mh.create_mad_hatter_bot(bot, name)
    print(new)
    botlist2 = mh.return_bots_by_15_type()
    botlist2_guid = [x.guid for x in botlist2]
    created = []
    for b in botlist2_guid:
        if b not in botlist_guid:
            created.append(mh.c.customBotApi.get_custom_bot(b, EnumCustomBotType(15).name).result)

    for i in created:
        if i.name == name:
            assert i.name == name


def test_bot_config():
    mh.set_configs_file()


def test_set_ranges():
    mh.set_ranges()
    assert mh.ranges is not None


def test_setup_bot_from_df():
    config = mh.configs.iloc[1]

    mh.setup_bot_from_df(bot, config)
    bot2 = mh.c.customBotApi.get_custom_bot(bot.guid, EnumCustomBotType(15).name).result
    bot_new_config = mh.get_bot_config_as_dataframe(bot2)
    pc = config.values[0:-3]
    nc = bot_new_config.values[0][1:-3]
    print(pc, '\n', nc)
    assert all([a == b for a, b in zip(pc, nc)])


def test_bt():
    mh.num_configs = 2
    mh.limit = 2
    print('bot', mh.bot)
    results = mh.bt()
    print('results', results)

    assert len(results.index) == mh.num_configs


def test_create_top_bots():
    mh.limit = 2
    botlist = mh.return_bots_by_15_type()
    botlist_guid = [x.guid for x in botlist]
    print('LIMIT', mh.limit)
    mh.create_top_bots()
    botlist2 = mh.return_bots_by_15_type()
    botlist2_guid = [x.guid for x in botlist2]
    created = []
    for b in botlist2_guid:
        if b not in botlist_guid:
            created.append(b)
    for a in created:
        mh.c.customBotApi.remove_custom_bot(a)
        print(f'{a} been deleted')

    assert len(created) == len(range(mh.limit))
