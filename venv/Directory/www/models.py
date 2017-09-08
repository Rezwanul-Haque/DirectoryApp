from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 100)
    title = models.CharField(max_length = 100)
    roll = models.CharField(max_length = 20)
    image = models.CharField(max_length = 200)
    
    
    def __str__(self):
        return self.name