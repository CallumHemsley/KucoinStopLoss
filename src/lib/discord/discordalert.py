from src.lib.discord.discordwebhook import DiscordWebhook
from enum import Enum


class DiscordAlertColor(Enum):
    ALERT = 0xFF0000
    WARNING = 0xFFFF00
    INFORMATION = 0xAAAAAA  # light grey
    GOOD = 0x00FF00  # represents a green message, that contains good news


class DiscordAlert:

    def __init__(self, url, username = "CyrCraft"):
        self.url = url
        self.username = username

    def sendAlert(self, message: str, colorCategory=DiscordAlertColor.INFORMATION, fields=dict):
        """Sends a colored message to the Discord-Webhook-URL that is set when constructing the object.
        The Argument colorCategory must be of the type DiscordAlertColors which represents different message categories
        fields is a list of key-value pairs representing the Name of the field along with its Value
        """
        categoryName = str(colorCategory).split(".")[1].title()
        if categoryName == "Good":
            categoryName = "Great news"

        processedFields = [dict()]

        for name, value in fields.items():
            processedFields.append({'name': name, 'value': value, 'inline': "true"})

        webhook = DiscordWebhook(self.url,username = self.username)
        webhook.sendEmbed(content=message, color=colorCategory.value,
                          title="-- " + categoryName + " --", fields=processedFields)
