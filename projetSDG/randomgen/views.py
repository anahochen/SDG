# Some standard Django stuff
from typing import List, Any, Union

import django.http
from django.template import context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

import random

from .models import Series


def index(request):
    """Render the index page"""

    series_list = Series.objects.all()
    output = ' - '.join([s.series_name for s in series_list])

    series_length = len(Series.objects.all())
    random_series_key = random.randint(1, series_length)
    random_series = Series.objects.get(pk=random_series_key)
    random_series_name = random_series.series_name
    random_series_season_episode = random_series.pick_random_season_episode(random_series)

    res = {
        "series_list": Series.objects.all(),
        "series_name": random_series_name,
        "season": random_series_season_episode[0],
        "episode":random_series_season_episode[1]
    }
    return render(request, "index.html", res)
    #return HttpResponse(chose_series)
