from typing import Union
from haasomeapi.HaasomeClient import HaasomeClient
from haasomeapi.apis.TradeBotApi import TradeBotApi
from api.Haas import Haas
from api.config_manager import ConfigManager
from loguru import logger as log
import time


class MainContext:
    """
    Main context class, that manages
    unique objects needed for service
    """

    def __init__(self) -> None:
        self.haas: Haas = Haas()
        self.config_manager: ConfigManager = self.haas.config_manager
        self.haasome_client: HaasomeClient = HaasomeClient(
            self.config_manager.url,
            self.config_manager.secret
        )

        self._check_config()

        self.trade_bot_api: TradeBotApi = TradeBotApi(
            self.config_manager.url,
            self.config_manager.secret
        )


    def _check_config(self) -> None:
        error_code: int = self._get_client_error_code()

        if error_code == 100:
            log.debug("Successfully connected!")
        elif error_code == 9002:
            self._wait_server_startup()
        else:
            self._check_config()

    def _wait_server_startup(self) -> Union[bool, None]:
        for _ in range(10):
            log.warning("Server may be offline...")
            time.sleep(5)
            if self._get_client_error_code == 100:
                return True
        log.error("Server can't be reached")
        exit(666)

    def _get_client_error_code(self) -> int:
        return self.haasome_client.accountDataApi.get_all_wallets().\
            errorCode.value


main_context: MainContext = MainContext()
