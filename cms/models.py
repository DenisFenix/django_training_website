from django.db import models


# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/', verbose_name='Изображение')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    # null=True стоит делать для всех полей, которые могут быть пустыми, default='-' - значение по-умолчанию
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        # Перевод значений в таблице в виде имени
        return self.cms_title

    class Meta:
        # Перевод заголовков
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
