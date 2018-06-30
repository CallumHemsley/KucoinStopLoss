from src.lib.marketdata.activeorder import ActiveOrder
from src.lib.stoploss import RunStopLoss
class RuntimeOperations:

    def initiate(self, Config, Exchange):
        currentOrder = ActiveOrder(Config.getCurrency(),
                                   Config.getSide())
        currentOrder.add(Config.getAmount(), Config.getEntryPrice())
        # place order!
        order = Exchange.createOrder(Config.getCurrency(), Config.getSide(), currentOrder.getPrice(), Config.getAmount())
        print("buy/sell response:\n" + str(order))
        if order is None:
            return False
        if 'orderOid' in order:
            # set the clientOrderId
            currentOrder.setId(order['orderOid'])
        # lets start the runtime loop
        #while CyrCraft.getState() != 'Standby':
            # lets determine which strategy to use
        run = RunStopLoss()
        run.determineAction(Config, currentOrder, Exchange)
            # run stop loss
