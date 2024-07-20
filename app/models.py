from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField(max_length=5)
    mobile = models.IntegerField(max_length=12)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
