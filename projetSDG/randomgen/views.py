# Some standard Django stuff
from typing import List, Any, Union

import django.http
from django.template import context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

import random

from .models import Series, Seasons


def index(request):
    """Render the index page"""

    series_list = Series.objects.all()
    output = ' - '.join([s.series_name for s in series_list])
    #return HttpResponse(output)

    series_number = len(Series.objects.all())
    random_key = random.randint(1, series_number)
    chose_serie = Series.objects.get(pk=random_key)
    nom_resultat = chose_serie.series_name

    random_season = Series.pick_random_season_episode(chose_serie)

    res = {
        "series": Series.objects.all(),
        "nom": nom_resultat,
        "saison": random_season
    }
    return render(request, "index.html", res)
    #return HttpResponse(chose_series)
