from django.db import models

# Create your models here.
class Toilet(models.Model):
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reviews = models.IntegerField(default=0)
    toilet_id = models.IntegerField()

    def __str__(self):
        return self.address

class Review(models.Model):
    toilet_id = models.IntegerField()
    text = models.CharField(max_length=1000,default="None")
    
    def __str__(self):
        return self.text