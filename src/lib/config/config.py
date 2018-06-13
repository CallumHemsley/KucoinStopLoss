from os.path import exists

class Config:

    def __init__(self):
        # All variables are of the type str / string. They have to be casted inside the get/set methods.
        # Any variable that contains None or str(None) will be treated as not set.
        self.public_key = None
        self.secret_key = None
        self.currency = None
        self.discordWebhookURL = None
        self.loadConfig()

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency
        self.saveConfig()
        return

    def getPublicKey(self):
        return self.public_key

    def setPublicKey(self, newKey):
        self.public_key = newKey
        self.saveConfig()
        return

    def getSecretKey(self):
        return self.secret_key

    def setSecretKey(self, newKey):
        self.secret_key = newKey
        self.saveConfig()
        return

    def getDiscordWebhookURL(self):
        return self.discordWebhookURL

    def setDiscordWebhookURL(self, newUrl):
        self.discordWebhookURL = newUrl
        self.saveConfig()
        return

    def configExists(self):
        if exists("configurationFile"):
            return True
        else:
            return False

    def loadConfig(self):
        if (exists("configurationFile")):
            fileobj = open("configurationFile","r")
            contents = fileobj.read().splitlines(False)
            fileobj.close()
            cdic = dict()
            for line in contents:
                sstr = line.split("':'")
                key = sstr[0][1:]
                val = sstr[1][:-1]
                cdic[key]=val

            confChanged = False
            values = vars(self)
            for value in values:
                if (cdic.keys().__contains__(value) and cdic[value] != str(None)):
                    values[value] = cdic[value]
                else:   # TODO add function call for every variable that might be missing
                    print("It looks like the variable '"+value+"' was not set before. Please enter the value now:")
                    newVal = input()
                    values[value] = newVal
                    confChanged = True
            if (confChanged):
                self.saveConfig()
        else:
            fileobj = open("configurationFile","w") # create file
            fileobj.close()
            self.loadConfig() # try again

    def saveConfig(self):
        values = vars(self)
        fileobj = open("configurationFile","w")
        firstpass = True
        for value in values:
            if not firstpass:
                fileobj.write("\n")
            fileobj.write("'"+value+"':'"+str(values[value])+"'")
            firstpass = False
        fileobj.close()