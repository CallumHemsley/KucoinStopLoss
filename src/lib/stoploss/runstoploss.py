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
        bought = Manager.validateQueues(Config, currentOrder, Exchange)
        while bought is False: # Loop until order bought.
            bought = Manager.validateQueues(Config, currentOrder, Exchange)
        # Now it's bought.
        # see if stop loss gets hit.
        # if it does, we buy back in.
        check = self.checkStopLoss(buyOrders, sellOrders, currentOrder, Config)
        while check is 'none':
            # fill the orders.
            buyOrders = self.updateBuyOrders(Config, buyOrders, Exchange)
            sellOrders = self.updateSellOrders(Config, sellOrders, Exchange)
            check = self.checkStopLoss(buyOrders, sellOrders, currentOrder, Config)

        # Now stop loss has been hit.
        # time to buy back in

        if check is 'buy':
            # then we want to sell.
            quant = currentOrder.getQuantity()
            # below, shouldnt be currentOrder.getPrice() because we want to sell at stop loss price or around it
            # need to calculate the best price to just buy in, not bid price.
            # also we arent checking the whole amount is being bought.. need to do that after.

            #FOR NOW WE WILL TRY BUY ORDER PRICE[0] LETS SEE HOW IT GOES..
            order = Exchange.createOrder(Config.getCurrency(), 'sell', buyOrders[0].getPrice(),
                                         quant)

        else:
            # then we want to buy.
            # calculate new quant from price.
            total = float(currentOrder.getQuantity()) * float(currentOrder.getPrice())
            point1Perecent = total / 1000
            total = total - point1Perecent
            total -= 0.000001
            newQuant = total / float(Config.getStopLossPrice())
            order = Exchange.createOrder(Config.getCurrency(), 'buy', sellOrders[0].getPrice(), newQuant)

    def checkStopLoss(self, buyOrders, sellOrders, currentOrder, Config):
        print("Checking stop loss..")
        if currentOrder.getSide() == 'BUY':
            if buyOrders[0].getPrice() <= float(Config.getStopLossPrice()):
                print("Stop loss hit")
                return 'buy'
        else:
            if sellOrders[0].getPrice() >= float(Config.getStopLossPrice()):
                print("Stop loss hit")
                return 'sell'
        return 'none'
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