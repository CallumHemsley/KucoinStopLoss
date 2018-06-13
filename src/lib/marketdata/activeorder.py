class ActiveOrder:
    def __init__(self, currency, side):
        self.symbol = currency
        self.orderId = None
        self.soldPrice = 0.00
        self.buyPrice = 0.00
        self.side = side
        self.buyAmount = 0.00
        self.quantity = 0.00
        self.rotationCount = 0
        self.isPartial = False

    def getIsPartial(self):
        return self.isPartial

    def setIsPartial(self, isPartial):
        self.isPartial = isPartial
    def getRotationCount(self):
        return self.rotationCount

    def addRotationCount(self):
        self.rotationCount = self.rotationCount + 1

    def getId(self):
        return self.orderId

    def setId(self, orderId):
        self.orderId = orderId

    def isEmpty(self):
        if float(self.quantity) > 0.0:
            return False
        else:
            return True

    def getSoldPrice(self):
        return self.soldPrice

    def getBuyPrice(self):
        return self.buyPrice

    def setBuyPrice(self, price):
        self.buyPrice = price

    def setSoldPrice(self, price):
        self.soldPrice = price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def add(self, quantity=0.00000000, buyPrice=0, soldPrice=0, currency='VEN-ETH', ethQuant=0.000000):
        self.quantity = quantity
        self.buyPrice = buyPrice
        self.soldPrice = soldPrice
        self.symbol = currency
        self.ethQuant = ethQuant

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getQuantity(self):
        return self.quantity

    def getEthQuantity(self):
        return self.ethQuant

    def getSide(self):
        return self.side

    def clear(self):
        self.orderId = None
        self.soldPrice = 0.00
        self.buyPrice = 0.00
        self.quantity = 0.00
        self.rotationCount = 0

    def save(self):
        # strictly for the wait queue
        # need to create a file, to be able to load in, encase of a bot restart.
        pass

    def load(self):
        # load in any wait queues if any...
        pass

