from django.db import models
from django.urls import reverse

from master.models import Master


class Post(models.Model):
    """Посты"""
    image = models.ImageField("Изображение", upload_to='posts/')
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Url', max_length=255, unique=True,
                            help_text='Генерируется автоматически!')
    author = models.ForeignKey(Master, on_delete=models.CASCADE,
                               verbose_name='Автор')
    content = models.TextField('Контент')
    tags = models.ManyToManyField('Tag', related_name='post_tags',
                                  verbose_name='Теги')
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]


class Tag(models.Model):
    """Теги"""
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Url', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-title']


class Comment(models.Model):
    """Комментарии"""
    name = models.CharField('Имя', max_length=50)
    telegram_username = models.CharField('Username', max_length=100)
    message = models.TextField('Сообщение', max_length=500)
    create_at = models.DateTimeField('Дата', auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comment_post",
                             on_delete=models.CASCADE,
                             verbose_name='Пост')

    def __str__(self):
        return self.telegram_username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-id']



