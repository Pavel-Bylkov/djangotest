# Generated by Django 3.1.7 on 2021-03-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210305_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='published',
        ),
        migrations.AlterField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(to='blog.Author'),
        ),
    ]