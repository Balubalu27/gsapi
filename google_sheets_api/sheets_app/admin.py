from django.contrib import admin
from sheets_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'order_number', 'dollar_price', 'delivery_time', 'ruble_price')
    ordering = ('number', )
