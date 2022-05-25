from django.db import models


class Order(models.Model):
    """ Модель описывающая заказ """

    number = models.IntegerField('№')
    order_number = models.IntegerField('заказ №')
    dollar_price = models.IntegerField('стоимость,$')
    delivery_time = models.DateField('срок поставки')
    ruble_price = models.FloatField('стоимость, руб')

    def __str__(self):
        return str(self.order_number)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
