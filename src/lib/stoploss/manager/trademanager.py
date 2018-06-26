from src.lib.discord import DiscordAlert
class TradeManager:

    def validateQueues(self, Config, CurrentOrder, KuCoinObj):
        print('[x] Loading.. Validating the queues..')

        if self.checkForOrders(Config, CurrentOrder, KuCoinObj) is True:
            return True
        return False
    def checkForOrders(self, Config, CurrentOrder, KuCoinObj):
        orders = KuCoinObj.getOrderHistory(Config) #get dealt orders
        while orders is None:
            orders = KuCoinObj.getOrderHistory(Config)

        if float(orders['total']) == 0:
            return False

        else:
            for o in orders['datas']:
                orderId = o['orderOid']
                # lets check for any trades from the active order were succesful or partial
                if CurrentOrder.getId() == orderId:
                    print("Something got bought/sold!")
                    print(o['dealValue'])
                    amountBought = float(o['dealValue'])
                    # let's update active order to this amount so we dont try to buy back in with too little!
                    CurrentOrder.setQuantity(amountBought)

                    '''amountBought = float(CurrentOrder.getAmount()) - amountBought
                    point1Perecent = amountBought / 1000
                    amountBought = amountBought - point1Perecent
                    amountBought -= 0.000001
                    quantity = amountBought / float(CurrentOrder.getSoldPrice())
                    print(type(amountBought))
                    print(str(amountBought))
                    # what's left 
                    CurrentOrder.add(quantity=quantity, soldPrice=CurrentOrder.getSoldPrice(), amount=amountBought)'''

                    # lets alert discord
                    self.discordAlert(Config, orderId, o['amount'],
                                      o['dealPrice'], o['fee'], o['direction'], o['createdAt'])
                    KuCoinObj.cancelBuyOrders(Config)
                    return True
            #if self.checkPartial(Config,buyQueue,sellQueue,KuCoinObj) is True:
             #   return True
            return False







    def discordAlert(self, Config, clientOrderId, amountTraded, priceAtTrade, tradeFee, side, time):
        testusername = "Stop Loss 0.1"

        discordAlert = DiscordAlert(Config.getDiscordWebhookURL(),username=testusername)

        discordAlert.sendAlert("Successful Trade Alert", DiscordAlert.DiscordAlertColor.INFORMATION,
                               {
                                   "Exchange": str(Config.getExchange()),
                                   "Currency Trading": str(Config.getCurrency()),
                                   "Coin Allowance": str(Config.getCoinAllowance()),
                                   "Side":  str(side),
                                   "Quantity Traded": str(amountTraded),
                                   "Price traded at": str(priceAtTrade),
                                   "Fee":   str(tradeFee),
                                   "Traded At": str(time),
                                   "Order ID": str(clientOrderId),
                               })