from django.db import models

# Create your models here.
class Toilet(models.Model):
    name = models.CharField(max_length=100,default="Unknown Location")
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reviews = models.IntegerField(default=0)
    latitude = models.DecimalField(default=0.0, decimal_places=6,max_digits=10)
    longitude = models.DecimalField(default=0.0, decimal_places=6,max_digits=10)
    sexes = models.CharField(max_length=30,default="Male/Female")

    def __str__(self):
        return self.address

class Review(models.Model):
    toilet_id = models.IntegerField()
    text = models.CharField(max_length=1000,default="None")
    
    def __str__(self):
        return self.text

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.username