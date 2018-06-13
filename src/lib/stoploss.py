import _thread
from src.lib.kucoin import KuCoin
from src.lib.menu import Menu, ConfigMenu
from src.lib.runtime import RuntimeOperations
class StopLoss:
    def __init__(self):
        self.state = 'Standby'

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def start(self, Config):
        exchange = KuCoin.KuCoin(Config)
        MainMenu = Menu()
        while self.state != 'Close':

            # display main menu
            MainMenu.display(Config, self.state)
            update = MainMenu.getUserInput()
            self.switch(Config, update, exchange)

    def switch(self, Config, update, ExchangeClass):

        if update == '1':
            configMenu = ConfigMenu()
            configMenu.menuController(Config, ExchangeClass)
            return

        elif update == '2':
            # lets change the state of the bot to running
            self.setState('Running')

            # lets start the runtime operations
            start = RuntimeOperations()
            _thread.start_new_thread(start.initiate, (self, Config, ExchangeClass))
            #_thread.start_new_thread(data.run, (Config, ExchangeClass))
        elif update == '4':
            ExchangeClass.cancelOrders(Config)
            self.state = 'Standby'

            return

        elif update == '5':
            self.state = 'Close'
            print('Closing')
            return