from django.db import models

# Create your models here.

# blueprint for the db table
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    #string representations of the tours
    def __str__(self):
        return (f"ID {self.id}: FROM {self.origin_country}, TO {self.destination_country}, NIGHTS: {self.number_of_nights}, PRICE: {self.price}")
        #id added only when instance is saved to the db