# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from products.models import *

# Create your views here.
def landing(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True)
	return render(request, 'landing/home.html', locals())
