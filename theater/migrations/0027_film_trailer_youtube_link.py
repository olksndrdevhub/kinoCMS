# Generated by Django 3.0.4 on 2020-03-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0026_auto_20200325_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='trailer_youtube_link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
