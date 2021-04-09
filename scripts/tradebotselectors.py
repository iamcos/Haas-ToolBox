from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy import get_style
import time


class TradeBotSellectors:
    def select_tradebot(self):
        self.tradebots = self.tradebotapi.get_all_trade_bots().result
        self.tradebot = inquirer.select(
            message="Select Trade Bot",
            choices=[Separator(" ")]
            + [{"name": x.name, "value": x} for x in self.tradebots],
        ).execute()

    def indicator_selector(self):
        while True:
            if len(self.tradebot.indicators) > 0:
                action = inquirer.select(
                    message="Select Indicator",
                    choices=[Separator(" ")]
                    + [
                        {"name": y.indicatorName, "value": y}
                        if y.enabled == True
                        else Separator(f"{y.indicatorName} ")
                        for x, y in self.tradebot.indicators.items()
                    ]
                    + ["Back"],
                    style=get_style({"seprator": "#658bbf bg:#ffffff"}),
                )

                kb_activate = True
                result = action.execute()
                if result == "Back":
                    break
                else:
                    self.indicator = result
                if len(self.indicator.indicatorInterface) > 0:
                    self.indicator_parameter_selector()

                else:
                    print(
                        f"\nNo selectable parameters were detected in {self.indicator.indicatorInterface.indicatorName}\n"
                    )
                    time.sleep(2)
                    self.indicator_selector()

    def indicator_parameter_selector(self):
        self.selected_parameter = None
        result = None
        while result != "Select another parameter":

            self.selected_parameter = inquirer.select(
                message="Select Parameter",
                choices=[Separator(" ")]
                + [
                    {"name": x.title, "value": i}
                    for i, x in enumerate(self.indicator.indicatorInterface)
                ]
                + ["Select another indicator"],
            ).execute()
            if self.selected_parameter == "Select another indicator":
                self.indicator_selector()
            if self.selected_parameter == "Go Back":
                break
            print("selected_parameter", self.selected_parameter)

            self.value = self.indicator.indicatorInterface[
                int(self.selected_parameter)
            ].value
            self.step = self.indicator.indicatorInterface[
                int(self.selected_parameter)
            ].step

            # try:
            action = inquirer.select(
                message="",
                choices=[
                    Separator(
                        f"{self.indicator.indicatorInterface[self.selected_parameter].title}:{self.indicator.indicatorInterface[self.selected_parameter].value} | step: {self.step} | ROI: {self.tradebot.roi}%"
                    ),
                    Separator(f"'left' - 1 | 'right' +1 | ',' +10 | '.' -10"),
                    f"Select another parameter",
                ],
            )

            @action.register_kb("right")
            def _(_):

                self.edit_indicator(direction=0)

            @action.register_kb("left")
            def _(_):
                self.edit_indicator(direction=1)

            @action.register_kb("space")
            def _(_):
                self.indicator_parameter_selector()

            @action.register_kb(",")
            def _(_):
                for i in range(10):
                    self.edit_indicator(direction=1)

            @action.register_kb(".")
            def _(_):
                for i in range(10):
                    self.edit_indicator(direction=0)

            kb_activate = True

            result = action.execute()
            print(result)

        else:
            result = None
            self.indicator_parameter_selector()

            # except Exception as e:
            # 		print("2nd try", e)
            #

    def safety_parameter_selector(self):
        result = None

        while result is not str:
            if type(self.safety) == None:

                self.selected_parameter = inquirer.select(
                    message="Select Parameter",
                    choices=[Separator(" ")]
                    + [
                        {"name": x.title, "value": i}
                        for i, x in enumerate(self.safety.safetyInterface)
                    ]
                    + ["Select another safety"],
                ).execute()
                if self.selected_parameter == "Select another safety":
                    self.safety_selector()
                if self.selected_parameter == "Go Back":
                    break
                print("selected_parameter", self.selected_parameter)

                while type(self.selected_parameter) == int:
                    self.value = self.safety.safetyInterface[
                        int(self.selected_parameter)
                    ].value
                    self.step = self.safety.safetyInterface[
                        int(self.selected_parameter)
                    ].step

                    action = inquirer.select(
                        message="",
                        choices=[
                            Separator(
                                f"{self.safety.safetyInterface[self.selected_parameter].title}:{self.safety.safetyInterface[self.selected_parameter].value} | step: {self.step} | ROI: {self.tradebot.roi}%"
                            ),
                            Separator(f"'left' - 1 | 'right' +1 | ',' +10 | '.' -10"),
                            "Select another parameter",
                        ],
                    )

                    @action.register_kb("right")
                    def _(_):

                        self.edit_safety(direction=0)

                    @action.register_kb("left")
                    def _(_):
                        self.edit_safety(direction=1)

                    @action.register_kb(",")
                    def _(_):
                        for i in range(10):
                            self.edit_safety(direction=1)

                    @action.register_kb(".")
                    def _(_):
                        for i in range(10):
                            self.edit_safety(direction=0)

                    kb_activate = True

                    result = action.execute()
                else:
                    self.safety_selector()
            else:
                print(
                    "\n\n   ERROR: \n   Bot has no safties, \n   please add safeties before selecting \n   this option\n\n"
                )
                break

        else:
            self.safety_parameter_selector()

    def insurance_parameter_selector(self):
        result = None
        while result != "Select another parameter":
            self.selected_parameter = inquirer.select(
                message="Select Parameter",
                choices=[Separator(" ")]
                + [
                    {"name": x.title, "value": i}
                    for i, x in enumerate(self.insurance.insuranceInterface)
                ]
                + ["Select another insurance"],
            ).execute()
            if selected_parameter == "Select another insurance":
                self.insurance_selector()
            if selected_parameter == "Go Back":
                break
            print("selected_parameter", self.selected_parameter)
            while type(self.selected_parameter) == int:
                self.value = self.insurance.insuranceInterface[
                    int(self.selected_parameter)
                ].value
                self.step = self.insurance.insuranceInterface[
                    int(self.selected_parameter)
                ].step

                action = inquirer.select(
                    message="",
                    choices=[
                        Separator(
                            f"{self.insurance.insuranceInterface[self.selected_parameter].title}:{self.insurance.insuranceInterface[self.selected_parameter].value} | step: {self.step} | ROI: {self.tradebot.roi}%"
                        ),
                        Separator(f"'left' - 1 | 'right' +1 | ',' +10 | '.' -10"),
                        "Select another parameter",
                    ],
                )

                @action.register_kb("right")
                def _(_):

                    self.edit_insurance(direction=0)

                @action.register_kb("left")
                def _(_):
                    self.edit_insurance(direction=1)

                @action.register_kb("space")
                def _(_):
                    self.insurance_parameter_selector()

                @action.register_kb(",")
                def _(_):
                    for i in range(10):
                        self.edit_insurance(direction=1)

                @action.register_kb(".")
                def _(_):
                    for i in range(10):
                        self.edit_insurance(direction=0)

                kb_activate = True

                result = action.execute()
            else:
                self.insurance_selector()
        else:
            self.insurance_parameter_select()

    def safety_selector(self):
        if len(self.tradebot.safeties) > 0:
            self.safety = inquirer.select(
                message="Select Safety",
                choices=[Separator(" ")]
                + [
                    {"name": y.safetyName, "value": y}
                    for x, y in self.tradebot.safeties.items()
                ],
            ).execute()
            if len(self.safety.safetyInterface) > 0:
                self.safety_parameter_selector()
            else:
                print(
                    f"\nNo selectable parameters were detected in {self.safety.safetyInterface.safetyName}\n"
                )
                time.sleep(2)
        else:
            self.safety_parameter_selector()

            time.sleep(2)

    def insurance_selector(self):
        if len(self.tradebot.insurances) > 0:
            self.insurance = inquirer.select(
                message="Select Insurance",
                choices=[Separator(" ")]
                + [
                    {"name": y.insuranceTypeFullName, "value": y}
                    for x, y in self.tradebot.insurances.items()
                ],
            ).execute()
            if len(self.insurance.insuranceInterface) > 0:
                self.insurance_parameter_selector()
            else:
                print(
                    f"\nNo selectable parameters were detected in {self.insurance.insuranceTypeFullName}\n"
                )
                time.sleep(2)
        else:
            self.insurance_parameter_selector()
            time.sleep(2)

    def edit_indicator(self, direction=None):

        if direction == 0:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) + int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_indicator_settings(
                self.tradebot.guid,
                self.indicator.guid,
                self.selected_parameter,
                self.value,
            )
            # print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result

            print(
                f"{self.tradebot.indicators[self.indicator.guid].indicatorInterface[self.selected_parameter].title} — {self.value} ROI: {self.tradebot.roi}%\n\n"
            )
        elif direction == 1:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) - int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_indicator_settings(
                self.tradebot.guid,
                self.indicator.guid,
                self.selected_parameter,
                self.value - self.step,
            )
            # print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result
            self.tradebotapi.backtest_trade_bot(self.tradebot.guid, self.ticks)

            print(
                f"{self.tradebot.indicators[self.indicator.guid].indicatorInterface[self.selected_parameter].title} — {self.value} ROI: {self.tradebot.roi}%"
            )

    def edit_safety(self, direction=None):

        if direction == 0:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) + int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_safety_settings(
                self.tradebot.guid,
                self.safety.guid,
                self.selected_parameter,
                self.value,
            )
            # print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result
            print(
                f"{self.tradebot.safeties[self.safety.guid].safetyInterface[self.selected_parameter].title}: {self.value} {self.tradebot.roi}%"
            )
        elif direction == 1:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) - int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_safety_settings(
                self.tradebot.guid,
                self.safety.guid,
                self.selected_parameter,
                self.value,
            )
            # print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result
            self.tradebotapi.backtest_trade_bot(self.tradebot.guid, self.ticks)
            print(
                f"{self.tradebot.safeties[self.safety.guid].safetyInterface[self.selected_parameter].title}: {self.value} {self.tradebot.roi}%"
            )

    def edit_insurance(self, direction=None):

        if direction == 0:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) + int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) + float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_insurance_settings(
                self.tradebot.guid,
                self.insurance.guid,
                self.selected_parameter,
                self.value,
            )
            # print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result
            self.tradebotapi.backtest_trade_bot(self.tradebot.guid, self.ticks)
            print(
                f"{self.tradebot.insurances[self.insurance.guid].insuranceInterface[self.selected_parameter].title}:{self.value} ROI: {self.tradebot.roi}%\n\n"
            )
        elif direction == 1:
            if self.step == 1.0:
                self.step = int(self.step)
                self.value = int(self.value) - int(self.step)
            if self.step == 0.1:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 1)
            if self.step == 0.01:
                self.step = float(self.step)
                self.value = float(self.value) - float(self.step)
                self.value = round(self.value, 2)

            configured_tradebot = self.tradebotapi.edit_bot_insurance_settings(
                self.tradebot.guid,
                self.insurance.guid,
                self.selected_parameter,
                self.value,
            )
            print(configured_tradebot.errorCode, configured_tradebot.errorMessage)
            self.tradebot = configured_tradebot.result
            self.tradebot = self.tradebotapi.backtest_trade_bot(
                self.tradebot.guid, self.ticks
            ).result
            self.tradebotapi.backtest_trade_bot(self.tradebot.guid, self.ticks)
            print(
                f"{self.tradebot.insurances[self.insurance.guid].insuranceInterface[self.selected_parameter].title}:{self.value} ROI: {self.tradebot.roi}%\n\n"
            )
