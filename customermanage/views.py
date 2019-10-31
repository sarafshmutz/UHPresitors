from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template import Context, loader
from .models import Customer,Purchase_order
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.

def index(request):
	
    return render(request, 'index.html')

def SearchResultsView(request):
	search=request.GET.get('search parameter')
	query=request.GET.get('q')
	print(search)
	if search=="1":
		try:
			object_list=Customer.objects.filter(first_name=query)
			customer_id=object_list[0].id
			product_list=Purchase_order.objects.filter(Purchase_number=customer_id)
			context= {"product_list":product_list,"object_list":object_list}
			return render(request, 'search_results.html',context)
		except:
			return HttpResponseNotFound('<h1>customer not found</h1>')
	if search=="2":
		try:
			object_list=Customer.objects.filter(last_name=query)
			print(object_list)
			customer_id=object_list[0].id
			product_list=Purchase_order.objects.filter(Purchase_number=customer_id)
			context= {"product_list":product_list,"object_list":object_list}
			return render(request, 'search_results.html',context)
		except:
			return HttpResponseNotFound('<h1>customer not found</h1>')


	


