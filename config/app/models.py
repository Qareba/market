from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    discription = models.TextField()
    #модель категория связвать



    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 255)


class Markets(models.Model):
    name = models.CharField(max_length = 255)
    geolocation = models.CharField(max_length = 255)