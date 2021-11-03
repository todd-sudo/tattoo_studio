from django.db import models


class CategoryTattoo(models.Model):
    """Категории татуировок"""
    name = models.CharField('Название',
                            max_length=100,
                            help_text='Например: Спина, Руки, Ноги, Грудь')
    slug = models.SlugField('URL', max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Gallery(models.Model):
    """Галерея"""
    category = models.ForeignKey(CategoryTattoo,
                                 on_delete=models.CASCADE,
                                 related_name='gallery_category',
                                 verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='gallery/')

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = "Татуировку"
        verbose_name_plural = "Татуировки"
        ordering = ['-id']


