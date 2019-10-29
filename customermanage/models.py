from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	telephone=models.CharField(max_length=30)

class Purchase_order(models.Model):
    Purchase_number=models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_order=models.CharField(max_length=30)
    date_of_supply=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    amount=models.IntegerField(max_length=10)
    price_per_unit=models.FloatField()



   