from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    discription = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True ,blank=True)
    market = models.ForeignKey('Markets', on_delete=models.SET_NULL, null=True ,blank=True)
    #gfadsfdfgdsgfsdfdsggs



    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 255)


class Markets(models.Model):
    name = models.CharField(max_length = 255)
    geolocation = models.CharField(max_length = 255)