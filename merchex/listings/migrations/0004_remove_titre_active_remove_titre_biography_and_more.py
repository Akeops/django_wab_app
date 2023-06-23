# Generated by Django 4.2.2 on 2023-06-20 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_genre_titre_active_titre_biography_titre_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titre',
            name='active',
        ),
        migrations.RemoveField(
            model_name='titre',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='titre',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='titre',
            name='official_homepage',
        ),
        migrations.RemoveField(
            model_name='titre',
            name='year_formed',
        ),
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
            preserve_default=False,
        ),
    ]