from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Customer



# Create your views here.
def index(request):
    t=loader.get_template('templates/index.html')
    Customers = Customer.objects.all()
    c={'object_list': Customers}
    return HttpResponse(t.render(c))