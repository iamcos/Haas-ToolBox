from cli.ToolBoxMainMenu import ToolBoxMainMenu


class CliContext:
    def __init__(self):
        self.main_menu: ToolBoxMainMenu = ToolBoxMainMenu()

cli_context = CliContext()
