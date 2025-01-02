from django.db import models
import rest_framework

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name