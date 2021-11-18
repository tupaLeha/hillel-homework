from django.core.management.base import BaseCommand
import csv

from apps.movies.models import Movie


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file')

    def handle(self, *args, **options):
        with open(options['file']) as csvfile:
            data = csv.DictReader(csvfile, delimiter='\t', quotechar='|')

            for row in data:
                if row['titleType'] not in ['short', 'movie']:
                    continue
                movie, created = Movie.objects.get_or_create(imdb_id=row['tconst'])
                movie.title_type = row['titleType']
                movie.name = row['primaryTitle']
                movie.is_adult = row.get('isAdult') != '0'
                movie.genres = [g.lower() for g in row['genres'].split(',')]
                movie.save()
