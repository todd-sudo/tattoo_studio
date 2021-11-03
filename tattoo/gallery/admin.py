from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.CategoryTattoo)
class CategoryTattooAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 7:
            self.message_user(
                request,
                'Вы можете добавить всего 7 категорий!',
                messages.ERROR
            )
        return super().add_view(request, form_url, extra_context)


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('category', 'get_image')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'
