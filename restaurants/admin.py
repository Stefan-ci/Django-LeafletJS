from django.contrib import admin
from restaurants.models import Restaurant


class Restaurantadmin(admin.ModelAdmin):
    list_display = ["name", "longitude", "latitude"]


admin.site.register(Restaurant, Restaurantadmin)
