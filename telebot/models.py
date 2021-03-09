from django.db import models


# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='ID чата')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.tg_chat

    class Meta:
        # Перевод заголовков
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
