from django.contrib import admin

from .models import AnimeFile, Anime, AnimeRating

admin.site.register(AnimeFile)
admin.site.register(Anime)
admin.site.register(AnimeRating)
