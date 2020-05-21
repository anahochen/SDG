from django.db import models
import random, datetime


# Create your models here.

class Series(models.Model):
    series_name = models.CharField(max_length=100)
    number_seasons = models.IntegerField()

    def __str__(self):
        return self.series_name

    def pick_random_season(self):
        r_season = random.randint(1, self.number_seasons)
        r_episode = r_season.pick_random_episode(r_season)

        t_season_episode = [r_season, r_episode]

        return t_season_episode


class Seasons(models.Model):
    season_number = models.IntegerField(primary_key=True)

    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name="series of the season")
    episodes = models.IntegerField()

    @staticmethod
    def pick_random_episode(self):
        return random.randint(range(1, self.episodes))
