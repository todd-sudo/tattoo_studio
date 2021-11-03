from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator


class Master(models.Model):
    """Мастера"""
    name = models.CharField('Имя мастера', max_length=150)
    image = models.ImageField('Изображение мастера', upload_to='masters/')
    about_master = models.TextField('Информация о мастере', max_length=180)
    vk = models.CharField('Ссылка на ВК', max_length=255, blank=True, null=True)
    instagram = models.CharField('Ссылка на Instagram', max_length=255,
                                 blank=True, null=True)
    telegram = models.CharField('Ссылка на Telegram', max_length=255,
                                blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('master_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
        ordering = ["name"]


class MasterSkills(models.Model):
    """Умения мастера"""
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name='Мастер',
        default='',
        related_name='master_skills'
    )
    name = models.CharField('Название', max_length=50)
    value = models.PositiveSmallIntegerField(
        verbose_name='Значение (%)',
        default=1,
        validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Умение мастера"
        verbose_name_plural = "Умения мастера"
        ordering = ["name"]


class RecordToMasterModel(models.Model):
    """Класс модели для записи клиента на сеанс"""
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name='Мастер',
        related_name='master_to_record',
        default=''
    )
    name = models.CharField('Имя', max_length=50)
    telegram_username = models.CharField('Username', max_length=100, default='')
    message = models.TextField('Текст сообщения', max_length=500)

    def __str__(self):
        return f'{self.name} - {self.telegram_username}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["-name"]
