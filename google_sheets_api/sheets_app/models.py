from django.db import models


class Order(models.Model):
    order_number = models.SmallIntegerField('заказ №')
    dollar_price = models.SmallIntegerField('стоимость,$')
    delivery_time = models.DateField('срок поставки')
    ruble_price = models.SmallIntegerField('стоимость, руб')

    def __str__(self):
        return str(self.order_number)

