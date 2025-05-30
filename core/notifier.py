"""
Notification system supporting Telegram and Discord.
"""

import requests

class Notifier:
    def __init__(self, telegram_token=None, discord_webhook=None):
        self.telegram_token = telegram_token
        self.discord_webhook = discord_webhook

    def send_telegram_message(self, chat_id, message):
        """
        Send a message via Telegram.
        """
        if not self.telegram_token:
            raise ValueError("Telegram token is not set")
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        response = requests.post(url, json=payload)
        response.raise_for_status()

    def send_discord_message(self, message):
        """
        Send a message via Discord webhook.
        """
        if not self.discord_webhook:
            raise ValueError("Discord webhook URL is not set")
        payload = {"content": message}
        response = requests.post(self.discord_webhook, json=payload)
        response.raise_for_status()
