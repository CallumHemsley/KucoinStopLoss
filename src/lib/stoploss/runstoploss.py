from src.lib.marketdata import OrderBook
from src.lib.stoploss.manager import TradeManager
class RunStopLoss:
    def determineAction(self, Config, currentOrder, Exchange):
        # create array of order objects, only want first 5 for buy and sell orders.
        buyOrders = [OrderBook() for x in range(5)]
        sellOrders = [OrderBook() for p in range(5)]

        # fill the orders.
        buyOrders = self.updateBuyOrders(Config, buyOrders, Exchange)
        sellOrders = self.updateSellOrders(Config, sellOrders, Exchange)

        Manager = TradeManager()
        Manager.validateQueues(Config, currentOrder, Exchange)

    def updateBuyOrders(self, Config, buyOrders, KuCoinObj):
        print('[x] Loading.. Updating buy orders.')
        orders = KuCoinObj.getOrderBook(Config, 'BUY')
        while orders is None:
            orders = KuCoinObj.getOrderBook(Config, 'BUY')
        # we only want the top 5 now...
        cnt = 0
        for order in orders:
            if cnt <= 4:
                buyOrders[cnt].set(order[1], order[0])
                cnt = cnt + 1
        # lets return it and keep on trucking
        return buyOrders

    def updateSellOrders(self, Config, sellOrders, KuCoinObj):
        print('[x] Loading.. Updating sell orders..')
        orders = KuCoinObj.getOrderBook(Config, 'SELL')
        while orders is None:
            orders = KuCoinObj.getOrderBook(Config, 'SELL')
        # we only want the top 5 now...
        cnt = 0
        for order in orders:
            if cnt <= 4:
                sellOrders[cnt].set(order[1], order[0])
                cnt = cnt + 1
        # lets return it and keep on trucking
        return sellOrders