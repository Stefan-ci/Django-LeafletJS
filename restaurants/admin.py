from django.contrib import admin
from restaurants.models import Restaurant


class Restaurantadmin(admin.ModelAdmin):
    list_display = ["name", "longitude", "latitude", "theme_color", "date"]


admin.site.register(Restaurant, Restaurantadmin)
