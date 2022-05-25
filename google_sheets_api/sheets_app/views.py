from django.shortcuts import render
from django.views import View
from sheets_app.convert_to_rub import ConvertDollarToRuble
from sheets_app.google_sheets_read import get_records_from_gsheets
from sheets_app.models import Order


class DbUpdateView(View):
    """ Класс, описывающий взаимодействие Google Sheets с БД """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_values_list_from_gsheet = []
        self.list_of_values_from_db = []
        self.delete_from_db_list = []
        self.change_obj_list = []
        self.gsheets_list_of_dicts = get_records_from_gsheets()  # Получаем значения из гугл таблиц

    def get(self, request):
        """ http get запрос на главную страницу запускает выполнение функций сравнения GS с БД """

        self.add_ruble_column_in_list()
        db_objects = self.get_list_of_values_from_db()
        self.detect_unuse_values_from_db()
        self.detect_new_in_google_sheets()
        return render(request, 'sheets_app/index.html', {'objects': db_objects})

    def add_ruble_column_in_list(self):
        """ Преобразует список значений из GS добавляя в него значение поля стоимость в руб. """

        for i_row in self.gsheets_list_of_dicts:
            rubles = ConvertDollarToRuble(i_row['стоимость,$']).ruble_amount  # Получаем стоимость в рублях
            values_list = list(i_row.values())
            values_list.append(rubles)                                # Добавляем поле стоимость, руб в список значений
            self.list_of_values_list_from_gsheet.append(values_list)  # Для дальнейшего сравнения со значениями из БД

    def get_list_of_values_from_db(self):
        """ Получаем значения из БД и преобразуем в список значений для сравнения с GS"""

        objects = Order.objects.all().order_by('number').values(
            'number',
            'order_number',
            'dollar_price',
            'delivery_time',
            'ruble_price'
        )
        for i_obj in objects:
            value_list = list(i_obj.values())
            self.list_of_values_from_db.append(value_list)
        return objects

    def detect_unuse_values_from_db(self):
        """ Ищет значения в БД, которые не совпадают с GS и заполняет список """

        for i_db_value in self.list_of_values_from_db:
            if i_db_value not in self.list_of_values_list_from_gsheet:  # Если значение в БД не совпадает с GS
                Order.objects.get(order_number=i_db_value[1]).delete()  # Ищем по ключу - номер заказа т.к. он уникален
                                                                        # И удаляем из БД
                self.delete_from_db_list.append(i_db_value)             # Формируем список изменений
        if self.delete_from_db_list:
            print(f'Записи, которые отсутствуют в GoogleSheets и подлежат удалению в БД: {self.delete_from_db_list}')

    def detect_new_in_google_sheets(self):
        """ Ищем значения в GS, которых нет в БД и добавляем """

        for i_gs_value in self.list_of_values_list_from_gsheet:
            if i_gs_value not in self.list_of_values_from_db:  # Если значения в БД нет - добавляем в список
                new_obj = Order(
                    number=i_gs_value[0],
                    order_number=i_gs_value[1],
                    dollar_price=i_gs_value[2],
                    delivery_time=i_gs_value[3],
                    ruble_price=i_gs_value[4]
                )
                self.change_obj_list.append(new_obj)
        Order.objects.bulk_create(self.change_obj_list)  # Заполняем БД одним запросом
        if self.change_obj_list:
            print(f'Новые/измененные записи: {self.change_obj_list}')
