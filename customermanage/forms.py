from django import forms
from django.forms import ModelForm
from .models import Customer,Purchase_order



choices=(
			('db value','Waffle'),
        	('db balue 1','tape n reel')
         )
class ModelForm1(forms.Form):
    model_name = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'model name'}))
    Tolerence = forms.CharField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'Tolerence'}))
    Amount=forms.IntegerField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'Amount'}))
    Resistence=forms.FloatField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'Resistence'}))
    markup=forms.FloatField(label="",widget= forms.TextInput
                           (attrs={'placeholder':'Markup'}))
    options=forms.CharField(label="",widget=forms.Select(choices=choices))


class CustomerForm(ModelForm):

	class Meta:
		model = Customer
		fields=("last_name","first_name","telephone","email")
		labels={
			"last_name":(""),
			"first_name":(""),
			"telephone":(""),
			"email":("")
			#"date_of_supply":("")
		}
		widgets = {
            'last_name': forms.TextInput(attrs={'placeholder':'last_name'}),
            'first_name': forms.TextInput(attrs={'placeholder':'first_name'}),
            'email': forms.TextInput(attrs={'placeholder':'email'}),

            'telephone': forms.TextInput(attrs={'placeholder':'telephone'})

           # 'date_of_supply': forms.TextInput(attrs={'placeholder':'date_of_supply'})
            } 

class PurchaseForm(ModelForm):

	class Meta:

		model = Purchase_order
		fields = ('amount',"date_of_supply","Customer_number","date_of_order","type",
		"purchase_number","price_per_unit")
		labels={
			"amount":(""),
			"date_of_supply":(""),
			"Customer_number":(""),
			"date_of_order":(""),
			"type":(""),
		    "price_per_unit":(""),
			"purchase_number":("")
		}
		widgets = {
		    
            'amount': forms.TextInput(attrs={'placeholder':'amount'}),
            'date_of_supply': forms.DateInput(attrs={'placeholder':'date_of_supply'}),
            'Customer_number': forms.Select(), 

            "date_of_order": forms.TextInput(attrs={'placeholder':'date_of_order'}),
            "type":forms.TextInput(attrs={'placeholder':'type'}),
            "price_per_unit":forms.TextInput(attrs={'placeholder':'price_per_unit'}),
            "purchase_number":forms.TextInput(attrs={'placeholder':'purchase_number'})
           
            } 
