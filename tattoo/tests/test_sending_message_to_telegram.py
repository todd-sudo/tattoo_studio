import requests
from django.conf import settings
from django.test import TestCase

from contact.models import ContactModel


class SendTelegramTestCase(TestCase):
    """Тест на отправку сообщения в Telegram"""

    def setUp(self):
        ContactModel.objects.create(name="test_name",
                                    telegram_username="@crot20",
                                    message='test_message')

    def test_sending_msg_to_telegram(self):
        """Проверка отправки сообщения в телеграм"""
        first_contact = ContactModel.objects.get(name="test_name")

        appeal = requests.get(
            f'https://api.telegram.org/bot{settings.TOKEN_BOT}'
            f'/sendmessage?chat_id=939392408&text={first_contact.name}\n'
            f'{first_contact.telegram_username}\n{first_contact.message}'
        )

        self.assertEqual(appeal.status_code, 200)
