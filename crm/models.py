from django.db import models


# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.Status_name

    class Meta:
        # Перевод заголовков
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    # auto_now=True, чтобы дата автоматически фиксировалась в момент создания экземпляра класса
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    # Создание нового поля order_status с привязкой к новому классу StatusCrm
    # (класс StatusCrm становится родителем поля order_status)
    # CASCADE будет использоваться для комментариев, PROTECT - для статуса,
    # чтобы запретить пользователям удалять статусы
    # null=True и blank=True добавляются после создания базы данных
    # null=True нужен для одобрения пустоты в базе данных,
    # blank=True - для пустоты в полях админ-панели Django
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.order_name

    class Meta:
        # Перевод заголовков
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    # Используем TextField, т.к. он больше CharField в количестве символов.
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.comment_text

    class Meta:
        # Перевод заголовков
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
