# Generated by Django 3.2.8 on 2021-11-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_year',
            field=models.DateField(null=True, verbose_name='Birth Year'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_year',
            field=models.DateField(null=True, verbose_name='Death Year'),
        ),
    ]
