# Generated by Django 3.2.8 on 2021-11-18 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20211112_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personmovie',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='personmovie',
            old_name='person_id',
            new_name='person',
        ),
    ]