from src.lib.config import Config
from src.lib.start import StopLoss

def run():
    Configuration = Config()
    bot = StopLoss()

    bot.start()

run()



