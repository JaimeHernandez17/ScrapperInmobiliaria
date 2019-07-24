from django.db import models


class AnimeFile(models.Model):
    file = models.FileField(upload_to='files/%Y_%m_%d/%H:%M:%S')


class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=120)
    type = models.CharField(max_length=100)
    episodes = models.IntegerField()
    rating = models.FloatField()
    members = models.IntegerField()
