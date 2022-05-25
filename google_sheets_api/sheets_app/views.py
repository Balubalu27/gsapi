from django.shortcuts import render
from django.views import View

from sheets_app.google_sheets_read import get_records_from_gsheets
from sheets_app.models import Order
from sheets_app.convert_to_rub import ConvertDollarToRuble


class DbUpdateView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_values_list_from_gsheet = []
        self.list_of_values_from_db = []
        self.delete_from_db_list = []
        self.change_obj_list = []
        self.gsheets_list_of_dicts = get_records_from_gsheets()  # Получаем значения из гугл таблиц

    def get(self, request):
        self.add_ruble_column_in_list()
        self.get_list_of_values_from_db()
        self.detect_unuse_values_from_db()
        self.detect_new_in_google_sheets()
        return render(request, 'sheets_app/index.html')

    def add_ruble_column_in_list(self):
        for i_row in self.gsheets_list_of_dicts:
            rubles = ConvertDollarToRuble(i_row['стоимость,$']).ruble_amount
            values_list = list(i_row.values())
            values_list.append(rubles)
            self.list_of_values_list_from_gsheet.append(values_list)

    def get_list_of_values_from_db(self):
        objects = Order.objects.all().values('number', 'order_number', 'dollar_price', 'delivery_time', 'ruble_price')
        for i_obj in objects:
            value_list = list(i_obj.values())
            self.list_of_values_from_db.append(value_list)

    def detect_unuse_values_from_db(self):
        for j in self.list_of_values_from_db:
            if j not in self.list_of_values_list_from_gsheet:
                Order.objects.get(
                    order_number=j[1]
                ).delete()

                self.delete_from_db_list.append(j)
        if self.delete_from_db_list:
            print(f'Записи, которые отсутствуют в GoogleSheets и подлежат удалению: {self.delete_from_db_list}')

    def detect_new_in_google_sheets(self):
        for i in self.list_of_values_list_from_gsheet:
            if i not in self.list_of_values_from_db:
                new_obj = Order(
                    number=i[0],
                    order_number=i[1],
                    dollar_price=i[2],
                    delivery_time=i[3],
                    ruble_price=i[4]
                )
                self.change_obj_list.append(new_obj)
        Order.objects.bulk_create(self.change_obj_list)
        if self.change_obj_list:
            print(f'Новые/измененные записи: {self.change_obj_list}')
