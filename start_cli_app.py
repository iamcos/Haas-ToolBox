from cli.CliContext import cli_context
from datetime import datetime
from loguru import logger as log


log.add("out.log", backtrace=True, diagnose=True)


@log.catch
def main():
    cli_context.main_menu.start_session()


if __name__ == "__main__":
    main()
