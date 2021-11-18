from django.contrib import admin

from apps.movies.models import Movie, Person, PersonMovie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['imdb_id', 'name', 'year']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['imdb_id', 'name', 'birth_year', 'death_year']


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ['movie', 'person', 'order', 'category', 'job', 'characters']
