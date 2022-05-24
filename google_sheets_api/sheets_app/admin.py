from django.contrib import admin

from sheets_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

