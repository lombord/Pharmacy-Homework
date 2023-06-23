from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    distance = models.PositiveIntegerField()
    coefficient = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self) -> str:
        return f"{self.name} {self.distance}km {self.coefficient}%"


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    amount = models.PositiveSmallIntegerField()
    pharmacies = models.ManyToManyField(Pharmacy)

    def __str__(self) -> str:
        return f"{self.name}-{self.amount}, {self.price}$"
