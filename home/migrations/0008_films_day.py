# Generated by Django 4.0.5 on 2022-08-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_films_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='day',
            field=models.IntegerField(default=2),
        ),
    ]
