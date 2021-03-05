from django.db import models


# Create your models here.
class Order(models.Model):
    # auto_now=True, чтобы дата автоматически фиксировалась в момент создания экземпляра класса
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.order_name

    class Meta:
        # Перевод заголовков
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

