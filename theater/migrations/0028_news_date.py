# Generated by Django 3.0.4 on 2020-03-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0027_film_trailer_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата додавання новини'),
        ),
    ]