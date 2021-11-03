from django.db import models
from django.urls import reverse


class InformationBlock(models.Model):
    """Класс модели для информации на главной странице"""
    name = models.CharField('Название блока', max_length=80)
    description = models.TextField('Описание блока')
    views = models.IntegerField('Количество посещений', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        ordering = ["-name"]


class Article(models.Model):
    """Модель статьи"""
    title = models.CharField('Название', max_length=250)
    slug = models.SlugField('URL', max_length=255, unique=True)
    content = models.TextField('Контент', max_length=800)
    image = models.ImageField('Изображение', upload_to='about/')

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-title"]
