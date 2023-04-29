from django.shortcuts import render
from restaurants.models import Restaurant


def home_view(request):
    context = {
        "restaurants": Restaurant.objects.filter(is_open=True)
    }
    template_name = "home.html"
    return render(request, template_name, context)

