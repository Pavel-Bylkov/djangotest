# Generated by Django 3.1.7 on 2021-03-05 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210305_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['name'], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
    ]