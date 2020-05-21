# Some standard Django stuff
from typing import List, Any, Union

import django.http
from django.template import context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

import random

from .models import Series, Seasons

# list of mobile User Agents
mobile_uas: List[Union[str, Any]] = [
    'w3c ', 'acs-', 'alav', 'alca', 'amoi', 'audi', 'avan', 'benq', 'bird', 'blac',
    'blaz', 'brew', 'cell', 'cldc', 'cmd-', 'dang', 'doco', 'eric', 'hipt', 'inno',
    'ipaq', 'java', 'jigs', 'kddi', 'keji', 'leno', 'lg-c', 'lg-d', 'lg-g', 'lge-',
    'maui', 'maxo', 'midp', 'mits', 'mmef', 'mobi', 'mot-', 'moto', 'mwbp', 'nec-',
    'newt', 'noki', 'oper', 'palm', 'pana', 'pant', 'phil', 'play', 'port', 'prox',
    'qwap', 'sage', 'sams', 'sany', 'sch-', 'sec-', 'send', 'seri', 'sgh-', 'shar',
    'sie-', 'siem', 'smal', 'smar', 'sony', 'sph-', 'symb', 't-mo', 'teli', 'tim-',
    'tosh', 'tsm-', 'upg1', 'upsi', 'vk-v', 'voda', 'wap-', 'wapa', 'wapi', 'wapp',
    'wapr', 'webc', 'winw', 'winw', 'xda', 'xda-'
]

mobile_ua_hints = ['SymbianOS', 'Opera Mini', 'iPhone']


def mobileBrowser(request):
    """ Super simple device detection, returns True for mobile devices """

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if ua in mobile_uas:
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser


def index(request):
    """Render the index page"""

    if mobileBrowser(request):
        t = loader.get_template('m_index.html')
    else:
        t = loader.get_template('index.html')

    series_list = Series.objects.all()
    output = ' - '.join([s.series_name for s in series_list])
    #return HttpResponse(output)

    series_number = len(Series.objects.all())
    random_key = random.randint(1, series_number)
    chose_series = Series.objects.get(pk=random_key)
    nom_resultat = chose_series.series_name

    random_season = Series.pick_random_season(chose_series)

    res = {
        "series": Series.objects.all(),
        "nom": nom_resultat,
        "saison": random_season
    }
    return render(request, "index.html", res)
    #return HttpResponse(chose_series)
