from configparser import NoOptionError, NoSectionError, ConfigParser, DuplicateSectionError
from typing import Optional
from api.domain.dtos import SclaperBacktestSample, BacktestRange
from api.config import toolbox_settings_path
from InquirerPy import inquirer
from datetime import datetime
from loguru import logger as log


class ConfigManager:

    def __init__(self):
        self.config_parser: ConfigParser = ConfigParser()
        self.config_parser.read(toolbox_settings_path)
        self.url, self.secret = self._get_ip_and_secret()

    def _get_ip_and_secret(self) -> tuple[str, str]:
        if "SERVER DATA" in self.config_parser:
            url: str = self.config_parser.get("SERVER DATA", "server_address")
            secret: str = self.config_parser.get("SERVER DATA", "secret")
            return (url, secret)
        else:
            self.config_parser.add_section("SERVER DATA")
            ip = inquirer.text(message="Type Haas Local api IP like so: 127.0.0.1", default="127.0.0.1").execute()
            port = inquirer.text(message="Type Haas Local api PORT like so: 8095", default="8095").execute()
            secret = inquirer.text(message="Type Haas Local Key (Secret) like so: 123", default="123").execute()
            url = f"http://{ip}:{port}"
            self._save_new_url_secret(url, secret)
            return (url, secret)

    def _save_new_url_secret(self, url: str, secret: str) -> None:
        self.config_parser.set("SERVER DATA", "server_address", url)
        self.config_parser.set("SERVER DATA", "secret", secret)

        self.write_file()

    def write_date(self):
        today = datetime.today()
        choices = (
            ("Write Year: ", str(today.year)),
            ("Write month: ", str(today.month)),
            ("Write day: ", str(today.day)),
            ("Write  hour: ", str(today.hour)),
            ("Write min: ", str(today.minute))
        )

        time: list[str] = [
            inquirer.text(message=msg[0], default=msg[1]).execute()
            for msg in choices
        ]

        self.config_parser.add_section("BT DATE")
        self.config_parser["BT DATE"] = {
            "year": time[0] if time[0] else str(today.year),
            "month": time[1] if time[1] else str(today.month),
            "day": time[2] if time[2] else str(today.day),
            "hour": time[3] if time[3] else str(today.hour),
            "min": time[4] if time[4] else str(today.minute),
        }

        self.write_file()

    def read_ticks(self):
        try:
            dt_from = datetime(
                int(self.config_parser.get("BT DATE", "year")),
                int(self.config_parser.get("BT DATE", "month")),
                int(self.config_parser.get("BT DATE", "day")),
                int(self.config_parser.get("BT DATE", "hour")),
                int(self.config_parser.get("BT DATE", "min")),
            )

            delta = datetime.now() - dt_from
            delta_minutes = delta.total_seconds() / 60

            return int(delta_minutes)
        except NoSectionError:
            log.warning(f"No BT DATE section, requesting from user...")
            self.write_date()
            return self.read_ticks()

    @property
    def config_backtesting_batch_size(self) -> int:
        try:
            return int(self.config_parser.get(
                "CONFIG BACKTESTING", "batch_size"))
        except (NoSectionError, NoOptionError):
            log.info("Batch size not set")

        return -1

    def set_config_backtesting_batch_size(self, n: int) -> None:
        try:
            self.config_parser.add_section("CONFIG BACKTESTING")
        except DuplicateSectionError:
            pass

        self.config_parser.set("CONFIG BACKTESTING", "batch_size", str(n))
        self.write_file()

    @property
    def config_backtesting_top_bots_count(self) -> int:
        try:
            return int(self.config_parser.get(
                "CONFIG BACKTESTING", "top_bots"))
        except (NoSectionError, NoOptionError):
            log.info("Top bots not set")

        return -1

    def set_config_backtesting_top_bots_count(self, n: int) -> None:
        try:
            self.config_parser.add_section("CONFIG BACKTESTING")
        except DuplicateSectionError:
            pass

        self.config_parser.set("CONFIG BACKTESTING", "top_bots", str(n))
        self.write_file()

    @property
    def scalper_range_backtest_sample(self) -> Optional[SclaperBacktestSample]:
        try:
            target_percentage: BacktestRange = BacktestRange(
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "target_percentage_start")
                    ),
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "target_percentage_end")
                    ),
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "target_percentage_step")
                    )
            )

            stop_loss: BacktestRange = BacktestRange(
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "stop_loss_start")
                    ),
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "stop_loss_end")
                    ),
                    float(self.config_parser.get(
                        "RANGE BACKTESTING", "stop_loss_step")
                    )
            )

            return SclaperBacktestSample(target_percentage, stop_loss)

        except (NoSectionError, NoOptionError):
            log.info("No Scalper range backtesting config found")

    def set_scalper_range_backtest_sample(
        self,
        s: SclaperBacktestSample
    ) -> None:

        try:
            self.config_parser.add_section("RANGE BACKTESTING")
        except DuplicateSectionError:
            pass

        self.config_parser.set(
                "RANGE BACKTESTING",
                "target_percentage_start",
                str(s.target_percentage.start)
        )
        self.config_parser.set(
                "RANGE BACKTESTING",
                "target_percentage_end",
                str(s.target_percentage.end)
        )
        self.config_parser.set(
                "RANGE BACKTESTING",
                "target_percentage_step",
                str(s.target_percentage.step)
        )

        self.config_parser.set(
                "RANGE BACKTESTING",
                "stop_loss_start",
                str(s.stop_loss.start)
        )
        self.config_parser.set(
                "RANGE BACKTESTING",
                "stop_loss_end",
                str(s.stop_loss.end)
        )
        self.config_parser.set(
                "RANGE BACKTESTING",
                "stop_loss_step",
                str(s.stop_loss.step)
        )

        self.write_file()


    def write_file(self) -> None:
        with open(toolbox_settings_path, "w") as f:
            self.config_parser.write(f)

