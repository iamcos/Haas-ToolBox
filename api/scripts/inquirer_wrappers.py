from InquirerPy import inquirer
from loguru import logger as log


def input_float(message: str, default: float) -> float:
    result: str = inquirer.text(
        message=message,
        default=str(default)
    ).execute()

    try:
        return float(result)
    except ValueError:
        log.warning("Input a float number")
        return input_float(message, default)


def input_int(message: str, default: int) -> int:
    result: str = inquirer.text(
        message=message,
        default=str(default)
    ).execute()

    try:
        return int(result)
    except ValueError:
        log.warning("Input a digit number")
        return input_int(message, default)

