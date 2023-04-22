from django.shortcuts import render
from restaurants.models import Restaurant


def home_view(request):
    context = {
        "restaurants": list(Restaurant.objects.values("id", "name", "longitude", "latitude"))
    }
    template_name = "home.html"
    return render(request, template_name, context)

