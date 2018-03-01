# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class StatusAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]

	class Meta:
		model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)