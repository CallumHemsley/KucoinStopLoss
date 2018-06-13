from src.lib.discord import DiscordWebhook

class ConfigMenu:
    def menuController(self, Config, ExchangeClass):
        self.mainDisplay(Config)
        userInput = self.getUserInput()

        self.switch(userInput, Config, ExchangeClass)


    def mainDisplay(self, Config):
        print('================== CyrCraft - Configuration Menu ===================== \n')
        print(
                    '[ - | Public Key: ' + Config.getPublicKey() + ' | Secret Key: ' + Config.getSecretKey() + '| - ] \n[ - | Current Currency: ' + Config.getCurrency() + ' | Current Strategy: Not Set | - ]\n\n')
        print('[ - | 1. Set Keys | 2. Set Currency | 3. Set Discord Webhook URL | 4. Get Balances | 5. Main Menu | - ]')
        print('\n =================================================================== \n')


    def getUserInput(self):
        this = input()
        return this


    def switch(self,userInput, Config, ExchangeClass):
        if (userInput == '1'):
            ## SET KEYS ##
            self.setKeys(Config, ExchangeClass)

        elif (userInput == '2'):
            ## SET NEW CURRENCY ##
            self.setNewCurrency(Config, ExchangeClass)
            return

        elif (userInput == '3'):
            ## SET NEW DISCORD WEBHOOK URL ##
            self.setNewDiscordWebhookUrl(Config)
            return

        elif (userInput == '4'):
            ## GET BALANCES ##

            ## AUTH CHECK THE BOT ##
            status = ExchangeClass.checkKeys()

            ## REDIRECT IF FALSE DUE TO BAD KEYS ##
            if status is False:
                confirm = input()
                if (confirm == '1'):
                    self.setKeys(Config, ExchangeClass)
                else:
                    self.menuController(Config, ExchangeClass)

            balances = ExchangeClass.getBalance()
            for x in balances:
                print('                  Currency: ' + x['currency'] + ' | Available: ' + x['available'])
            print('\n =================================================================== \n'
                  'Pres 1 to go back, or any key to return to main menu')
            print('\n =================== CyrCraft - Balance Report ======================= \n')
            back = input()

            if (back == '1'):
                self.menuController(Config, ExchangeClass)
            else:
                return

        elif (userInput == '5'):
            ## BACK TO MAIN MENU ##
            return


    def setKeys(self,Config, ExchangeClass):
        print('Enter Public Key:')
        key = input()
        key.strip()
        Config.setPublicKey(key)

        print('Enter Secret Key:')
        key = input()
        key.strip()
        Config.setSecretKey(key)
        ExchangeClass.__init__( Config )
        status = ExchangeClass.checkKeys()

        if status is False:
            confirm = input()
            if (confirm == '1'):
                self.setKeys(Config, ExchangeClass)
            else:
                self.menuController(Config, ExchangeClass)


    def setNewCurrency(self,Config, ExchangeClass):
        status = ExchangeClass.checkKeys()

        if status is False:
            confirm = input()
            if (confirm == '1'):
                self.setKeys(Config, ExchangeClass)
            else:
                self.menuController(Config, ExchangeClass)
        else:
            currencies = ExchangeClass.getSymbols()

            options = ''
            currencyRow = 7
            numCurrency = 0
            cnt = 0
            filter = self.filterSymbols(currencies)

            for y in filter:
                cnt = cnt + 1
                numCurrency = numCurrency + 1

                if cnt >= currencyRow:
                    filter.insert(numCurrency, '\n')
                    cnt = 0

            for z in filter:
                options = options + " | " + z
            print(options)

            while True:
                print('Please select a currency..')
                inputString = input()
                if inputString in filter:
                    break
                print('Err... Please select a currency in the above list, THANKS.')
            Config.setCurrency(inputString)
            return
    def filterSymbols(self,currencies):
        success = False
        while success is False:
            print('Please type the cryptocurrency you wish to trade (e.g BTC or VEN)')
            inputString = input()
            for x in currencies:
                if inputString in x:
                    success = True
                    break
            if not success:
                print("Err... can't find this currency, try again or try a different one.")
        option = []
        for x in currencies:
            if inputString in x:
                option.append(x)
        return option
    def setNewDiscordWebhookUrl(self,Config):
        print("Please enter the new webhook url. If you need help creating one, please follow the steps below (The URL will be validated afterwards):\n"
              + "How to create a Webhook:\n"
              + "1. Find the channel in the channel tree that should receive the messages.\n"
              + "2. Click on the gear to access the channel settings.\n"
              + "3. In the 'Webhook'-category click 'Add Webhook'\n"
              + "4. Adjust the settings to your liking and copy the webhook url by clicking the button next to it.\n"
              + "5. Paste the complete url into this console and hit [Enter] (whitespaces will be removed)."
              )
        inputString = input().replace(' ','')

        Webhook = DiscordWebhook.DiscordWebhook(inputString)
        try:
            Webhook.sendMessage("This is a test message sent by CyrCraft. Seeing this means the that entered URL is valid. Messages can now be sent into here.", username="Cyrcraft")
            Config.setDiscordWebhookURL(inputString)
            print("Webhook url set successfully.")
        except:
            print("Test failed. Invalid webhook URL entered.")