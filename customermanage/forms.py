from django import forms

class ModelForm(forms.Form):
    model_name = forms.CharField(label='model_name', max_length=100)
    Tolerence = forms.CharField(label='Tolerence', max_length=100)
    Amount=forms.IntegerField(label="Amount")
    Resistence=forms.FloatField(label="Resistence")
    markup=forms.FloatField(label="markup")