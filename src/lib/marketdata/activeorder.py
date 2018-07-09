class ActiveOrder:
    def __init__(self, currency, side):
        self.symbol = currency
        self.orderId = None
        self.price = 0.00
        self.side = side
        self.highestPrice = 0.00
        self.quantity = 0.00

    def getId(self):
        return self.orderId

    def setId(self, orderId):
        self.orderId = orderId

    def isEmpty(self):
        if float(self.quantity) > 0.0:
            return False
        else:
            return True

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getHighestPrice(self):
        return self.highestPrice

    def setHighestPrice(self, price):
        self.highestPrice = price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def add(self, quantity=0.00000000, price=0.00):
        self.quantity = quantity
        self.price = price

    def getSide(self):
        return self.side

    def clear(self):
        self.orderId = None
        self.price = 0.00
        self.quantity = 0.00

