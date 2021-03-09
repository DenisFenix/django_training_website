from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


# Вывод комментария в карточку
# StackedInline наследует другой класс админки
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    # Прописываем дату в read only
    readonly_fields = ('comment_dt',)
    # Назначение количества полей для комментария
    extra = 0


class OrderAdm(admin.ModelAdmin):
    # Создание таблицы из значений
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # Создание кликабельных полей
    list_display_links = ('id', 'order_name')
    # Создание поиска
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    # Создание фильтра (в кортеже при одном значении в конце всегда нужно указывать запятую,
    # чтобы Python понимал, что это последовательность объектов, даже если используется один объект)
    list_filter = ('order_status',)
    # Создание редактируемых полей
    list_editable = ('order_status', 'order_phone')
    # Пагинация
    # Количество отображаемых полей на странице
    list_per_page = 10
    # Количество всех полей на странице, если нажать на кнопку Показать все
    list_max_show_all = 100

    # Настройка карточки заказа
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    # Для удаления ошибки FieldError (дата не может быть изменена) назначаем поля для чтения
    readonly_fields = ('id', 'order_dt')
    # Поле класса Comment
    inlines = [Comment,]


# Register your models here.
admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
