import requests


class DiscordWebhook:
    def __init__(self, url, username = "CyrCraft"):
        self.fields = []
        self.url = url
        self.username = username

    def sendMessage(self, message):
        json = '{"content":"' + message + '"'
        if self.username is not None:
            json += ', "username":"' + self.username + '"'

        json += '}'
        result = requests.post(self.url, data=json, headers={'Content-Type': 'application/json'})
        if result.status_code == 401:  # wrong url (not authorized)
            raise ConnectionRefusedError("Discord returned a 401 - Not Authorized. Webhook URL may be invalid.")
        elif result.status_code == 400:
            raise ValueError("Received BAD REQUEST statuscode on sending an embed to discord. Json Body: " + json)

    def sendEmbed(self, content, color, title, fields):
        json = '{'
        if self.username is not None:
            json += '"username":"' + self.username + '",'

        json += '"embeds":[{'

        if content:
            json += '"description":"' + content + '",'

        if color:
            json += '"color":"' + str(color) + '",'

        if title:
            json += '"title":"' + title + '",'

        if self.fields:
            fields += self.fields
            self.fields.clear()

        if fields:
            json += '"fields":['

            for field in fields:
                if len(field) == 0:
                    continue

                json += '{"name":"' + field['name'] + '",'
                json += '"value":"' + field['value'] + '",'
                json += '"inline":' + field['inline'] + '},'

            json = json[:-1]  # remove comma at the end
            json += '],'

        json = json[:-1]  # remove comma at the end
        json = json + '}]}'
        result = requests.post(self.url, data=json, headers={'Content-Type': 'application/json'})

        if result.status_code == 401:  # wrong url (not authorized)
            raise ConnectionRefusedError("Discord returned a 401 - Not Authorized. Webhook URL may be invalid.")
        elif result.status_code == 400:
            raise ValueError("Received BAD REQUEST statuscode on sending an embed to discord. Json Body: " + json)

    def addField(self, name: str, value: str, inline: bool):
        self.fields.append({'name': name, 'value': value, 'inline': str(inline).lower()})

    def sendImage(self, imageUrl):
        json = '{"embeds":[{"image":{"url":"' + imageUrl + '"}}]'
        if self.username is not None:
            json += ', "username":"' + self.username + '"'

        json += '}'
        result = requests.post(self.url, data=json, headers={'Content-Type': 'application/json'})
        if result.status_code == 401:  # wrong url (not authorized)
            raise ConnectionRefusedError("Discord returned a 401 - Not Authorized. Webhook URL may be invalid.")
        elif result.status_code == 400:
            raise ValueError("Received BAD REQUEST statuscode on sending an embed to discord. Json Body: " + json)

    def setUsername(self, newUsername):
        self.username = newUsername