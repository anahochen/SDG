from django.db import models
import random, datetime

# Create your models here.

class Series(models.Model):
    series_name = models.CharField(max_length=100)
    number_seasons = models.IntegerField()

    def __str__(self):
        return self.series_name

    def pick_random_season_episode(self, number_seasons):

        random_season = self.pick_random_season()

        # IDEALLY
        # find the Season object in order to call the pick_random_episode_number method
        # using random_season_id

        # QUICK AND NOT ELEGANT AT ALL
        # generate a random episode number regardless of the season

        random_episode = random.randrange(1,self.number_seasons,1)

        t_season_episode = [random_season, random_episode]

        return t_season_episode

    def pick_random_season(self):
        season_id = random.randrange(1,self.number_seasons,1)
        return season_id


class Seasons(models.Model):
    season_number = models.IntegerField(primary_key=True)

    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name="series of the season")
    episodes = models.IntegerField()

    @staticmethod
    def pick_random_episode_number(self):
        return random.randrange(1,self.episodes,1)
