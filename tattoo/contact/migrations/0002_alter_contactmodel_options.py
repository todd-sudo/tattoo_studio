# Generated by Django 3.2.4 on 2021-06-13 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'ordering': ['-name'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
    ]