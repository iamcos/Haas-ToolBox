class HaasToolBoxException(Exception): pass

class BotException(HaasToolBoxException): pass

class MadHatterException(BotException): pass

class TradeBotException(BotException): pass

class ScalperException(BotException): pass

class BotWrapperException(HaasToolBoxException): pass

class BotApiProviderCreationException(HaasToolBoxException): pass

class BotManagerCreationException(HaasToolBoxException): pass

class BoostedInterfaceException(HaasToolBoxException): pass

class BotBacktesterException(HaasToolBoxException): pass

class AutobacktesterTypesFactryException(HaasToolBoxException): pass

