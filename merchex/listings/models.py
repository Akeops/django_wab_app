from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Band(models.Model):
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        PHONK = 'PK'
        LOFI = 'LF'

    def __str__(self):
        return f'{self.name}'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    name = models.fields.CharField(max_length=100)
class Song(models.Model):
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    name = models.fields.CharField(max_length=100)
    duration = models.fields.FloatField(max_length=4)

