from django.core.management.base import BaseCommand
import csv
import datetime

from apps.movies.models import Person


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file')

    def handle(self, *args, **options):
        with open(options['file']) as csvfile:
            data = csv.DictReader(csvfile, delimiter='\t', quotechar='|')

            for row in data:
                person, created = Person.objects.get_or_create(imdb_id=row['nconst'])
                person.name = row['primaryName']
                if row['birthYear'] != '\\N':
                    person.birth_year = datetime.date(int(row['birthYear']), 1, 1)
                else:
                    person.birth_year = None
                if row['deathYear'] != '\\N':
                    person.death_year = datetime.date(int(row['deathYear']), 1, 1)
                else:
                    person.death_year = None
                person.save()
