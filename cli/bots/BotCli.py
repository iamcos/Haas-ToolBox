class BotCli:
    """
    Base interface for bot setting CLI
    """
    def menu(self) -> None:
        """
        To implement method for showing main menu for current Bot
        """
        raise NotImplementedError("Method must be implemented")
