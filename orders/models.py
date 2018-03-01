# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product

# Create your models here.
names = (
		('new', 'Новый'),
		('cancel', 'Отменен'),
		('completed', 'Выполнен'),)

class Status(models.Model):
	name = models.CharField(max_length=64, choices=names, blank=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	
	def __str__(self):
		return "Status %s" % self.name

	class Meta:
		verbose_name = 'Статус заказа'
		verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	surname = models.CharField(max_length=64, blank=True, null=True, default=None)
	phone = models.CharField(max_length=64, blank=True, null=True, default=None)
	email = models.EmailField()
	adress = models.CharField(max_length=128, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, blank=True, null=True, default=None)
	date_time = models.DateTimeField(null=True, blank=True)
	status = models.ForeignKey(Status, blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __str__(self):
		return "Order %s %s" % (self.id, self.status.name)


	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

