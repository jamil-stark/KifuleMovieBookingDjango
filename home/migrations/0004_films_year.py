# Generated by Django 4.0.5 on 2022-08-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_films_actors_films_runtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]
