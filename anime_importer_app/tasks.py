import csv
import itertools

from .models import Anime, AnimeRating
from ScrapperInmobiliaria.celery import app as celery_app
import os
import time


@celery_app.task
def process_file(path):
    with open(path) as f:
        reader1, reader = itertools.tee(csv.DictReader(f))
        columns = len(next(reader1))
        del reader1
        if columns >= 7:
            canceled_rows = 0
            saved_rows = 0
            for row in reader:
                try:
                    print("Saved anime with name: ", row['name'])
                    data_anime = Anime(anime_id=row['anime_id'], name=row['name'], genre=row['genre'], type=row['type'],
                                       episodes=row['episodes'], rating=row['rating'], members=row['members'])
                    data_anime.save()
                    saved_rows += 1
                except Exception:
                    canceled_rows += 1
            print(f"Canceled rows = {canceled_rows}")
            print(f"Saved rows = {saved_rows}")
        elif columns >= 3:
            canceled_rows = 0
            saved_rows = 0
            for row in reader:
                try:
                    if Anime.objects.filter(anime_id=row['anime_id']).exists():
                        print("Save animeRating with id: ", row['anime_id'])
                        anime = Anime.objects.get(anime_id=row['anime_id'])
                        AnimeRating.objects.update_or_create(user_id=row['user_id'], anime_fk=anime,
                                                             rating=row['rating'])
                        saved_rows += 1
                    else:
                        print(f"The animeRating with id '{row['anime_id']}' no exist: ")
                except Exception:
                    canceled_rows += 1
            print(f"Canceled rows = {canceled_rows}")
            print(f"Saved rows = {saved_rows}")
