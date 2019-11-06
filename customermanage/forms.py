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
		fields=("last_name","first_name","telephone")
		labels={
			"last_name":(""),
			"first_name":(""),
			"telephone":("")
			#"date_of_supply":("")
		}
		widgets = {
            'last_name': forms.TextInput(attrs={'placeholder':'last_name'}),
            'first_name': forms.TextInput(attrs={'placeholder':'first_name'}),
            'telephone': forms.TextInput(attrs={'placeholder':'telephone'})

           # 'date_of_supply': forms.TextInput(attrs={'placeholder':'date_of_supply'})
            } 

class PurchaseForm(ModelForm):

	class Meta:
		model = Purchase_order
		fields = ('amount',"date_of_supply")
		labels={
			"amount":(""),
			"date_of_supply":("")
		}
		widgets = {
            'amount': forms.TextInput(attrs={'placeholder':'amount'}),
            'date_of_supply': forms.TextInput(attrs={'placeholder':'date_of_supply'})
            } 