from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	telephone=models.CharField(max_length=30)

class Purchase_order(models.Model):
    
    Customer_number=models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_order=models.DateField()
    date_of_supply=models.DateField()
    type=models.CharField(max_length=30)
    amount=models.IntegerField()
    price_per_unit=models.FloatField()
    purchase_number=models.CharField(max_length=30,default=1)
    #def __str__(self):
     #   return self.name



   