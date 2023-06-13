from django import forms
from .models import Featured_Products
from .models import Sales_Information
class NewWearForm(forms.ModelForm):
    class Meta:
        model = Featured_Products
        fields = ['image', 'name', 'description','date_posted', 'rating', 'cost']
class NewWearForm1(forms.ModelForm):
    class Meta:
        model = Sales_Information
        fields = ['name', 'description', 'date_starts','date_ends', 'offer']

