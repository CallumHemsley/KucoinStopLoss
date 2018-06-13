from src.lib.marketdata.activeorder import ActiveOrder

class RuntimeOperations:

    def initiate(self, CyrCraft, Config, Exchange):
        currentOrder = ActiveOrder()
        # lets start the runtime loop
        while CyrCraft.getState() != 'Standby':
            # lets determine which strategy to use
            # run stop loss
    def checkForRestore(self, Config, buyQueue, waitQueue, sellQueue):
        # lets restore queue data
        check = 0
        for bQueue in buyQueue:
            if bQueue.getQuantity() is not 0:
                check += 1
        for wQueue in waitQueue:
            if wQueue.getQuantity() is not 0:
                check += 1
        if sellQueue.getQuantity() is not 0:
                check += 1

        if check is 21:
            print('[x] Loading.. Restoring queues if necessary')
            Queue = RestoreQueues(Config)
            Queue.restore(buyQueue, waitQueue, sellQueue)
