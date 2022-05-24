from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from read import test
from sheets_app.models import Order
from sheets_app.scripts import ConvertToRuble


class DbUpdateView(View):
    def get(self, request):
        a = list(Order.objects.all().values(
            'order_number'
        ))

        print(a)

        print('====================================================================')
        list_from_gsheets = test()
        print(list_from_gsheets)

        # list_of_objects = []
        #
        # for i in d:
        #     rubles = ConvertToRuble(i['стоимость,$']).dollar_amount
        #
        #     p = Order(
        #         order_number=i['заказ №'],
        #         dollar_price=i['стоимость,$'],
        #         delivery_time=i['срок поставки'],
        #         ruble_price=rubles
        #     )
        #     list_of_objects.append(p)
        # Order.objects.bulk_create(list_of_objects)
        # print(list_of_objects)

