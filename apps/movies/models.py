from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField


TITLE_TYPE_CHOICES = [

]
CATEGORY_CHOICES = [

]
JOB_CHOICES = [

]


class Movie(models.Model):
    imdb_id = models.CharField(_('Imdb ID'), max_length=255)
    title_type = models.CharField(_('Title Type'), max_length=255, choices=TITLE_TYPE_CHOICES)
    name = models.CharField(_('Name'), max_length=255)
    is_adult = models.BooleanField(_('Is Adult'))
    year = models.DateField(_('Start Year'))
    genres = ArrayField(
        ArrayField(
            models.CharField(_('Genres'), max_length=255, blank=True)
        )
    )


class Person(models.Model):
    imdb_id = models.CharField(_('Imdb ID'), max_length=255)
    name = models.CharField(_('Name'), max_length=255)
    birth_year = models.DateField(_('Birth Year'))
    death_year = models.DateField(_('Death Year'))


class PersonMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='tconst')
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='nconst')
    order = models.IntegerField(_('ordering'))
    category = models.CharField(_('category'), max_length=255, choices=CATEGORY_CHOICES)
    job = models.CharField(_('job'), max_length=255, choices=JOB_CHOICES)
    characters = ArrayField(
        ArrayField(
            models.CharField(_('characters'), max_length=255, blank=True)
        )
    )

