import random
from restaurants.models import Restaurant
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate random restaurants with coordinates and names"
    
    def handle(self, *args, **options):
        restaurants_names = ["MacDonald's", "Lara", "Le Chef", "Black and White", "Queen's restaurant", "La manne", "Chez Mami"]
        for i in range(10):
            Restaurant.objects.create(
                name=random.choice(restaurants_names),
                longitude=random.uniform(7, 8),
                latitude=random.uniform(-5.1, -4),
            )
            print("Restaurant created!")
        print(f"\n\nRestaurants have been created successfully. There are {Restaurant.objects.count()} restaurants now.\n\n")
