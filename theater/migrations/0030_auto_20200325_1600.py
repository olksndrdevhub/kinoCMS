# Generated by Django 3.0.4 on 2020-03-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0029_auto_20200325_1214'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FilmGallery',
            new_name='FilmImages',
        ),
    ]