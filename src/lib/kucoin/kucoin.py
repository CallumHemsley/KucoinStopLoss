from kucoin.client import Client
import math

class KuCoin:
    lastTimestamp = None

    def __init__(self, Config):
        self.publicKey = Config.getPublicKey()
        self.secretKey = Config.getSecretKey()
        self.client = Client(self.publicKey, self.secretKey)

    def checkKeys(self):
        try:
            b = self.client.get_api_keys()
            if 'code' not in b: # If code is there, it means an error code so wrong.
                return True
            #else:
            #    self.errorMessage(b)
            #    return False
        except(Exception): #TO DO: extract kucoin exception message directly
            self.errorMessage("KuCoin API error.")
            return False

    def getBalance(self, limit=None, page=None):
        try:
            jsonD = self.client.get_all_balances()
        except Exception as e:
            print("Error getting balance.")
            return

        balances = []
        for x in jsonD:
            if x['balance'] != 0.0:
                balances.append(x) #TO DO, MAKE IT SAME NAMES AS HITBTC
        for b in balances:
            for key in b.keys():
                if(key == "coinType"):
                    newKey = key.replace("coinType","currency")
                    b[newKey] = b[key]
                    del b[key]
                if(key == "balanceStr"):
                    newKey = key.replace("balanceStr","available")
                    b[newKey] = b[key]
                    del b[key]

        return balances
    def getSymbols(self):

        jsonD = self.client.get_trading_symbols()
        symbols = []
        for x in jsonD:
            symbols.append(x['symbol'])


        return symbols

    def getOrderHistory(self, Config):
        try:
            orders = self.client.get_dealt_orders(symbol=Config.getCurrency())
            return orders
        except Exception as e:
            print("ERROR GETTING ORDER HISTORY:")
            print(e)
            return None

    def getActiveOrders(self, Config):
        try:
            orders = self.client.get_active_orders(symbol=Config.getCurrency())
            return orders
        except Exception as e:
            print("ERROR GETTING ACTIVE ORDERS")
            print(e)
            return None

    def getOrderBook(self, Config, request):
        try:
            orders = self.client.get_order_book(Config.getCurrency())

            if (request == 'SELL'):
                return orders['SELL']

            if (request == 'BUY'):
                return orders['BUY']

        except Exception as e:
            print(e)
            return None

    def cancelBuyOrders(self, Config):
        try:
            cancelAttempt = self.client.cancel_all_orders(Config.getCurrency(), 'BUY')
            if cancelAttempt is None:
                return True
        except Exception as e:
            print(e)
        return False

    def cancelSellOrders(self, Config):
        try:
            cancelAttempt = self.client.cancel_all_orders(Config.getCurrency(), 'SELL')
            if cancelAttempt is None:
                return True
        except Exception as e:
            print(e)
        return False

    def cancelOrders(self, Config):
        try:
            cancelAttempt = self.client.cancel_all_orders(Config.getCurrency(), 'BUY')
            cancelAttempt = self.client.cancel_all_orders(Config.getCurrency(), 'SELL')
            if cancelAttempt is None:
                return True
        except Exception as e:
            print(e)
        return False

    def createOrder(self, symbol, side, price, amount):
        try:
            #sellPrice = str(round(float(price), 6))
            transaction = self.client.create_order(symbol, side.upper(), price, amount)
            return transaction # returns orderOid
        except Exception as e:
            print("Took too long.. mismatch I think??")
            print(e)
    def errorMessage(self, b):
        print('\n =================== CyrCraft - Errrr Errorrrrrr ======================= \n')
        print(b)
        print('Keys are wrong..\nType 1 to set your keys.. or else any key to go Configuration Menu..')
        print('\n ======================================================================= \n')
