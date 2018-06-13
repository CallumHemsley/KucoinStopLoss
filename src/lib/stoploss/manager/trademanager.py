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
                    print("Something got bought!")
                    print(o['dealValue'])
                    amountBought = float(o['dealValue'])
                    amountBought = float(CurrentOrder.getAmount()) - amountBought
                    point1Perecent = amountBought / 1000
                    amountBought = amountBought - point1Perecent
                    amountBought -= 0.000001
                    quantity = amountBought / float(CurrentOrder.getSoldPrice())
                    print(type(amountBought))
                    print(str(amountBought))
                    CurrentOrder.add(quantity=quantity, soldPrice=CurrentOrder.getSoldPrice(), amount=amountBought)

                    # lets alert discord
                    self.discordAlert(Config, orderId, o['amount'],
                                      o['dealPrice'], o['fee'], o['direction'], o['createdAt'])
                    KuCoinObj.cancelBuyOrders(Config)
                    return True
                if sellQueue.getId() == orderId:
                    print("Sold!")
                    # we got a match

                    # put that what's sold into buy queue.
                    for b in buyQueue:
                        if b.isEmpty():
                            venQuan = o['amount']
                            print(o['dealValue'])
                            ethAmount = float(o['dealValue'])
                            #ethAmount = ethAmount - 0.0001
                            point1Perecent = ethAmount / 1000
                            ethAmount = ethAmount - point1Perecent
                            ethAmount -= 0.000001
                            quantity = ethAmount / float(sellQueue.getSoldPrice())
                            print(type(ethAmount))
                            print(str(ethAmount))
                            b.add(quantity=quantity, soldPrice=sellQueue.getSoldPrice(), ethQuant=ethAmount)
                            break
                    sellQueue.clear()


                    # refresh the backup logs
                    #sellLog = SaveQueues()
                    #sellLog.saveSellQueue(sellQueue)


                    # lets alert discord
                    self.discordAlert(Config, orderId, o['amount'],
                                      o['dealPrice'], o['fee'], o['direction'], o['createdAt'])

                    # send to log
                    #Log = FileManager()
                    #Log.add(o['id'], o['orderId'], o['clientOrderId'], o['side'],
                     #       o['price'], o['quantity'], o['timestamp'], o['fee'])
                    KuCoinObj.cancelSellOrders(Config)
                    return True
            #if self.checkPartial(Config,buyQueue,sellQueue,KuCoinObj) is True:
             #   return True
            return False







    def discordAlert(self, Config, clientOrderId, amountTraded, priceAtTrade, tradeFee, side, time):
        testusername = "CyrCraft V2.4"


        discordAlert = DiscordAlert.DiscordAlert(Config.getDiscordWebhookURL(),username=testusername)

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