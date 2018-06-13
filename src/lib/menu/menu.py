class Menu:
    def display(self, Config, state):
        print('======================= CyrCraft - Main Menu ======================= \n')
        print(
            '[ - | Current Currency: ' + Config.getCurrency() + ' | Current State: ' + state + ' | Current Exchange: KuCoin | - ]')
        print(
            '[ - | 1. Configure Bot | 2. Start Trading | 3. Stop Trading | 4. Shutdown Bot | - ]')
        print('\n =================================================================== \n')

    def getUserInput(self):
        this = input()
        return this