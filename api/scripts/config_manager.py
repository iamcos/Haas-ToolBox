from configparser import NoSectionError, SafeConfigParser

from InquirerPy import inquirer
import datetime
from loguru import logger as log


class ConfigManager:

    def __init__(self):
        self.config_parser: SafeConfigParser = SafeConfigParser()
        # TODO: add full path 
        self.config_parser.read('config.ini')
        self.url, self.secret = self._get_ip_and_secret()

    def _get_ip_and_secret(self) -> tuple[str, str]:
        if 'SERVER DATA' in self.config_parser:
            url: str = self.config_parser.get("SERVER DATA", "server_address")
            secret: str = self.config_parser.get("SERVER DATA", "secret")
            return (url, secret)
        else:
            self.config_parser.add_section("SERVER DATA")
            ip = inquirer.text(message="Type Haas Local api IP like so: 127.0.0.1", default="127.0.0.1").execute()
            port = inquirer.text(message="Type Haas Local api PORT like so: 8095", default="8095").execute()
            secret = inquirer.text(message="Type Haas Local Key (Secret) like so: 123", ).execute()
            url = f"http://{ip}:{port}"
            self._save_new_url_secret(url, secret)
            return (url, secret)

    def _save_new_url_secret(self, url: str, secret: str) -> None:
        log.info(f"{self.config_parser.sections()=}")
        self.config_parser.set("SERVER DATA", "server_address", url)
        self.config_parser.set("SERVER DATA", "secret", secret)

        with open("config.ini", "w") as f:
            self.config_parser.write(f)

    def write_date(self):

        choices = [
            f"Write Year ({str(datetime.datetime.today().year)}): ",
            f"Write month (current is {str(datetime.datetime.today().month)}): ",
            f"Write day (today is {str(datetime.datetime.today().day)}): ",
            f"Write  hour (now is {str(datetime.datetime.today().hour)}): ",
            f"Write min (now {str(datetime.datetime.today().minute)}): ",
        ]

        y = inquirer.text(message=choices[0]).execute()
        m = inquirer.text(message=choices[1]).execute()
        d = inquirer.text(message=choices[2]).execute()
        h = inquirer.text(message=choices[3]).execute()
        min = inquirer.text(message=choices[4]).execute()

        self.config_parser.add_section("BT DATE")
        self.config_parser["BT DATE"] = {
            "year": y,
            "month": m,
            "day": d,
            "hour": h,
            "min": min,
        }

        self.write_file()

    def read_ticks(self):
        try:
            dt_from = datetime.datetime(
                int(self.config_parser.get("BT DATE", "year")),
                int(self.config_parser.get("BT DATE", "month")),
                int(self.config_parser.get("BT DATE", "day")),
                int(self.config_parser.get("BT DATE", "hour")),
                int(self.config_parser.get("BT DATE", "min")),
            )

            delta = datetime.datetime.now() - dt_from
            delta_minutes = delta.total_seconds() / 60

            return int(delta_minutes)
        except NoSectionError as e:
            log.warning(f"No BT DATE section, requesting grom user... {e=}")
            self.write_date()
            return self.read_ticks()

    def write_file(self) -> None:
        with open("config.ini", "a") as f:
            self.config_parser.write(f)
