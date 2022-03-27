import json
import pandas as pd


config = pd.read_csv("./api/config/mad_hatter_config.csv")

result_dict = {
    "tests": []
}

for i, row in config.iterrows():
    modes = {
        "Interval": row.interval,
        "Indicator Signal Consensus": row.signalconsensus,
    }

    indicator = {
        "Mad Hatter MACD": {
            "MACD Fast": row.macdfast,
            "MACD Slow": row.macdslow,
            "MACD Signal": row.macdsign
        },
        "Mad Hatter RSI": {
            "Length": row.rsil,
            "Buy level": int(row.rsib),
            "Sell level": int(row.rsis)
        },
        "Mad Hatter BBands": {
            "MA Type": row.matype,
            "Length": row.bbl,
            "Dev.Up": int(row.devup),
            "Dev.Down": int(row.devdn),
            "Require FCC": row.fcc,
            "Reset Middle": row.resetmiddle,
            "Allow Mid Sells": row.allowmidsells
        }
    }

    result_dict["tests"].append(
        {
            i: {
                "modes": modes,
                "Indicator": indicator
            }
        }
    )

with open("./api/config/MadHatterBotConfig.json", "w") as f:
    f.write(json.dumps(result_dict, indent=4))


