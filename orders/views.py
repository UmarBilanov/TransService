# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import OrderForm
from orders.models import *
from products.models import *



# Create your views here.
def orders(request):
	form = OrderForm(request.POST or None)
	products_images = ProductImage.objects.filter(is_active=True, is_main=True)

	if request.method == "POST" and form.is_valid():
		print (request.POST)
		print (form.cleaned_data)
		data  = form.cleaned_data
		print (data["name"])

		new_form = form.save()

	return render(request, 'landing/orders.html', locals())
