# Generated by Django 3.1.6 on 2021-03-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(related_name='posts', to='blog.Author'),
        ),
    ]
