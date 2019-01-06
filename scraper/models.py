from django.db import models

class PopularCurrencyModel(models.Model):
    name = models.CharField(max_length=20)
    rate = models.CharField(max_length=10)
    change = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class AllCurrencyModel(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)
    change = models.CharField(max_length=10)

    def __str__(self):
        return self.name