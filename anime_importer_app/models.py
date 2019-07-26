from django.db import models

from .utils.file_validations import validator


class AnimeFile(models.Model):
    file = models.FileField(validators=[validator], upload_to='files/%Y_%m_%d/%H:%M:%S')

    def __str__(self):
        return self.file


class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=120)
    type = models.CharField(max_length=100)
    episodes = models.IntegerField()
    rating = models.FloatField()
    members = models.IntegerField()

    def __str__(self):
        return self.name


class AnimeRating(models.Model):
    user_id = models.IntegerField()
    anime_fk = models.ForeignKey('Anime', on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.anime_fk.name
