# Generated by Django 3.2.8 on 2021-11-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(verbose_name='Start Year'),
        ),
    ]
