import requests
from django.conf import settings


def send_message(_id: str, message: str):
    """
    Веб-сервис, который отправляет сообщения
    от пользователя в телеграм администраторам
    """
    message = requests.get(f'https://api.telegram.org/bot{settings.TOKEN_BOT}'
                           f'/sendmessage?chat_id={_id}&text={message}')
    return message
