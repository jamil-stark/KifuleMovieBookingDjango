# Generated by Django 4.0.5 on 2022-08-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_films_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='is_coming_soon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='films',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='films',
            name='is_top_rated',
            field=models.BooleanField(default=False),
        ),
    ]
