from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from sheets_app.models import Order


class SheetsListView(ListView):
    model = Order


class DbUpdateView(View):
    pass
