from django.contrib import admin

# Register your models here.
from .models import Series, Seasons
admin.site.register(Series)
admin.site.register(Seasons)
