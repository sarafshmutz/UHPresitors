from django.contrib import admin


# Register your models here.
from .models import Customer,Purchase_order

admin.site.register(Customer)
admin.site.register(Purchase_order)
