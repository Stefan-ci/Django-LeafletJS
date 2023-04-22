from django.db import models

class Restaurant(models.Model):
    name = models.CharField(null=True, max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    class Meta:
        ordering = ["name"]
    
    
    def __str__(self):
        return self.name
