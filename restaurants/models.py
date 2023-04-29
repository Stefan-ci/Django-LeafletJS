from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    theme_color = models.CharField(max_length=7)
    date = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField()
    
    class Meta:
        ordering = ["name", "date"]
    
    
    def __str__(self):
        return self.name
    
    def status(self):
        if self.is_open:
            return "Open"
        return "Closed"
