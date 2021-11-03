from django.contrib import admin

from .models import ContactModel, AdminTelegramId


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_username')
    list_display_links = ('name', 'telegram_username')


@admin.register(AdminTelegramId)
class AdminTelegramIdAdmin(admin.ModelAdmin):
    list_display = ('master', 'telegram_id')
    list_display_links = ('master', 'telegram_id')
