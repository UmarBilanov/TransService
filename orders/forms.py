from django import forms
from .models import *
from products.models import Product


class OrderForm(forms.ModelForm):
	product = forms.ModelMultipleChoiceField(queryset=Product.objects.all())

	class Meta:
		model = Order
		exclude = [""]

