# Generated by Django 3.2.4 on 2021-06-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workstattoomasters',
            options={'ordering': ['-id'], 'verbose_name': 'Работы мастеров', 'verbose_name_plural': 'Работы мастеров'},
        ),
    ]
