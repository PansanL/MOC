from django.db import models

# Create your models here.
class BUILDING(models.Model):
    building = models.CharField(max_length=255,unique=True)
    
    def __str__(self) :
        return self.building