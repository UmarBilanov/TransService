# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	height = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	length = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	width = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % (self.name)

	class Meta:
		verbose_name = 'Транспорт'
		verbose_name_plural = 'Транспорты'


class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='static/ProductImage/')
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s" % (self.id)

	class Meta:
		verbose_name = 'фотография'
		verbose_name_plural = 'фотографии'
