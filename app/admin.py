from django.contrib import admin
from app import models

class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate', 'moviename', 'hero', 'heroine', 'rating']
admin.site.register(models.Movie, MovieAdmin)