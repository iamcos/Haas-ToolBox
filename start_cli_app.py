from cli.CliContext import cli_context
from datetime import datetime
from loguru import logger as log


def main():
    # try:
        cli_context.main_menu.start_session()
    # except Exception as e:
    #     log.error(e)
    #     write_error_log(str(e))


def write_error_log(error: str):
    with open("error.log", "a") as f:
        f.write(f"{datetime.now()} {error}")


if __name__ == "__main__":
    main()
