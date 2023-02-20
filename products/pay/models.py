from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=300, default='some_value', verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')  # если целые числа в стоимости

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
