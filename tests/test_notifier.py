import unittest
import sys
import os
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.notifier import Notifier

class TestNotifier(unittest.TestCase):
    def setUp(self):
        self.notifier = Notifier(telegram_token="dummy_token", discord_webhook="http://dummy_webhook")

    @patch('core.notifier.requests.post')
    def test_send_telegram_message(self, mock_post):
        mock_post.return_value.status_code = 200
        try:
            self.notifier.send_telegram_message("dummy_chat_id", "Test message")
        except Exception as e:
            self.fail(f"send_telegram_message raised an exception: {e}")
        mock_post.assert_called()

    @patch('core.notifier.requests.post')
    def test_send_discord_message(self, mock_post):
        mock_post.return_value.status_code = 200
        try:
            self.notifier.send_discord_message("Test message")
        except Exception as e:
            self.fail(f"send_discord_message raised an exception: {e}")
        mock_post.assert_called()

if __name__ == "__main__":
    unittest.main()
