from django.db import models

from .utils.file_validations import validator


class AnimeFile(models.Model):
    file = models.FileField(validators=[validator], upload_to='files/%Y_%m_%d/%H:%M:%S')


class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=120)
    type = models.CharField(max_length=100)
    episodes = models.IntegerField()
    rating = models.FloatField()
    members = models.IntegerField()


class AnimeRating(models.Model):
    user_id = models.IntegerField()
    anime_fk = models.ForeignKey('Anime', on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()
