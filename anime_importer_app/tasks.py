import csv
from .models import Anime
from ScrapperInmobiliaria.celery import app as celery_app
import os
import time


@celery_app.task
def process_file(path):
    count = 0
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                p = Anime(anime_id=row['anime_id'], name=row['name'], genre=row['genre'], type=row['type'],
                          episodes=row['episodes'], rating=row['rating'], members=row['members'])
                p.save()
            except Exception:
                count += 1
        print(f"Cancel files = {count}")
