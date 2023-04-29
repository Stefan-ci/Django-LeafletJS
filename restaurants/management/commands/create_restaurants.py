import random
from restaurants.models import Restaurant
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Generate randomly restaurants with coordinates and names.
        Restaurants list from https://www.goafricaonline.com/ci/annuaire/restaurants/
    """
    
    help = "Generate random restaurants with coordinates and names"
    
    def handle(self, *args, **options): 
        restaurants_names = ["MacDonald's", "Lara", "Le Chef", "Black and White", "Queen's restaurant", "La manne",
            "Chez Mami", "Ô Delices" "L'ART DE VIVRE RESTAURANT LOUNGE", "LES DELICES DU CIEL", "AGHA", "AFRICAFE",
            "RESTAURANT LES DELICES DE CANAAN", "UNIVERSAL HÔTEL YAMOUSSOUKRO", "RESTAURANT LE PELICAN",
            "100% Live", "1ST CHOISE RESTAURANT", "2 SANS 3", "5EME AVENUE", "7 EPICES", "8 POLL", "A L'AVIKAM",
            "A L'USINE CHEZ ROSE", "ABIDJAN CAFE BRASSERIE", "ABIDJAN CONTINUE", "ABIDJAN LOISIRS (AZITO PALACE)",
            "ABIDJAN RESTAURANT AWARDS", "ABOLLA SUPER", "ABOU HASSAN", "ACADEMIE DU ZOUGLOU", "AFFESS BEACH",
            "AFRICA DOMINI", "AFRICAN QUEEN'S", "AFRO GOUTER", "AFTER WORK", "AGNEBY DELICE ET BLUE BIRD BAR"]
        bool_vars = [True, False]
        hex_colors = ["#10b0ff", "#ff50f0", "#90a0ff", "#90a0ff", "#f0ff00", "#30c000", "#30c000", "#c0c000",
            "#e01000", "#20ff00", "#1010ff", "#00a080", "#ff50a0", "#100030", "#100030", "#b0ff70", "#300080"]
        
        
        for i in range(35):
            restaurant = Restaurant.objects.create(
                name = random.choice(restaurants_names),
                longitude = random.uniform(5.55, 9.5),
                latitude = random.uniform(-7.55, -3.50),
                is_open = random.choice(bool_vars),
                theme_color = random.choice(hex_colors)
            )
            print(f"{restaurant.name} created!")
