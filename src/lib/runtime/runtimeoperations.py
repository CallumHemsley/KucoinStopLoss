from src.lib.marketdata.activeorder import ActiveOrder
from src.lib.stoploss import RunStopLoss
class RuntimeOperations:

    def initiate(self, CyrCraft, Config, Exchange):
        currentOrder = ActiveOrder(Config.getCurrency(),
                                   Config.getSide())
        # lets start the runtime loop
        while CyrCraft.getState() != 'Standby':
            # lets determine which strategy to use
            run = RunStopLoss()
            run.determineAction(Config, currentOrder, Exchange)
            # run stop loss
