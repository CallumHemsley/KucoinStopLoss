class ActiveOrder:
    def __init__(self):
        self.clientOrderId = None
        self.symbol = None
        self.side = None
        self.status = None
        self.quantity = None
        self.price = None
        self.cumQuantity = None
        self.createdAt = None
        self.updatedAt = None

    def set(self, newClientOrderId, newSymbol, newSide, newStatus, newQuantity,
            newPrice, newCumquantity, newCreatedAt, newUpdatedAt):
        self.clientOrderId = newClientOrderId
        self.symbol = newSymbol
        self.side = newSide
        self.status = newStatus
        self.quantity = newQuantity
        self.price = newPrice
        self.cumQuantity = newCumquantity
        self.createdAt = newCreatedAt
        self.updatedAt = newUpdatedAt

    def getClientOrderId(self):
        return self.clientOrderId

    def getSide(self):
        return self.side

    def getStatus(self):
        return self.status

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price


