import json
from json import JSONDecodeError

from django.core.management.base import BaseCommand
import csv

from apps.movies.models import PersonMovie, Movie, Person


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file')

    def handle(self, *args, **options):
        with open(options['file']) as csvfile:
            data = csv.DictReader(csvfile, delimiter='\t', quotechar='|')

            for row in data:
                movie, created = Movie.objects.get_or_create(imdb_id=row['tconst'])
                person, created = Person.objects.get_or_create(imdb_id=row['nconst'])
                person_movie, created = PersonMovie.objects.get_or_create(movie=movie, person=person)
                person_movie.order = row['ordering']
                person_movie.category = row['category']
                person_movie.job = row['job']
                try:
                    characters = json.loads(row['characters'])
                except JSONDecodeError:
                    characters = []
                person_movie.characters = characters
                person_movie.save()
