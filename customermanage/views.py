from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template import Context, loader
from .models import Customer,Purchase_order
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from datetime import date
from datetime import timedelta
from .forms import ModelForm1
from .forms import CustomerForm,PurchaseForm

# Create your views here.

def create(request):
    form1=CustomerForm(request.POST or None)
  
    form2=PurchaseForm(request.POST or None)
    if form1.is_valid():
            form1.save()
    
   # save.save()

    context={"form1":form1,"form2":form2}
    #print(context)
    return render(request, 'create.html', context)


def index(request):

    
    d = date.today()
    enddate = d + timedelta(days=6)
    form=ModelForm1(request.POST or None)
    for item in form.visible_fields():
    	print(item)
    if form.is_valid():
    	print(form.cleaned_data)
    	print(form.cleaned_data.get("Amount"))
    product_list=Purchase_order.objects.filter(date_of_supply__gte=enddate)
    if product_list.exists():
        toggle =5
        x=product_list[0].purchase_number
    else:
    	toggle=0 
    context={"d":d,"toggle":toggle,"form":form}
    print(toggle)
    return render(request, 'index.html',context)
    




def SearchResultsView(request):
	search=request.GET.get('search parameter')
	query=request.GET.get('q')

	if search=="3":
		try:
			
			product_list=Purchase_order.objects.filter(purchase_number=query)
			context={"product_list":product_list}
			return render(request,'search_results.html',context)
		except:


			return HttpResponseNotFound('<h1>customer not found</h1>')
	

	if search=="1":
	
		try:

			object_list=Customer.objects.filter(first_name=query)
			customer_id=object_list[0].id
			product_list=Purchase_order.objects.filter(Customer_number=customer_id)
			context= {"product_list":product_list,"object_list":object_list}
			return render(request, 'search_results.html',context)
		except:
			return HttpResponseNotFound('<h1>customer not found</h1>')
	if search=="2":
		try:
			object_list=Customer.objects.filter(last_name=query)
			print(object_list)
			customer_id=object_list[0].id
			product_list=Purchase_order.objects.filter(Customer_number=customer_id)
			context= {"product_list":product_list,"object_list":object_list}
			return render(request, 'search_results.html',context)
		except:
			return HttpResponseNotFound('<h1>customer not found</h1>')
	


