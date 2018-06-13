class OrderBook:
    def __init__(self):
        self.size = None
        self.price = None

    def set(self, newSize, newPrice):
        self.size = newSize
        self.price = newPrice

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.price
