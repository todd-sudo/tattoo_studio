from django.db import models

from master.models import Master


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField('Имя', max_length=50)
    telegram_username = models.CharField('Username', max_length=100, default='')
    message = models.TextField('Текст сообщения', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["-name"]


class AdminTelegramId(models.Model):
    master = models.ForeignKey(Master,
                               on_delete=models.CASCADE,
                               related_name='telegram_id',
                               verbose_name='Мастер')
    telegram_id = models.CharField('Телеграм ID', max_length=15)

    def __str__(self):
        return self.telegram_id

    class Meta:
        verbose_name = "Телеграм ID"
        verbose_name_plural = "Телеграм ID"



