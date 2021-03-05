from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.
def first_page(request):
    """
    Order - это класс и объект, который хранит в себе данные.
    С помощью класса Order и обращению к objects.all() происходит
    получение всех данных в этом классе, затем все данные отправляются в шаблон index.html
    """
    form  = OrderForm()
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list, 'form': form})


def thanks_page(request):
    """
    request получает запись вида <WSGIRequest: POST '/thanks/?name=value&phone=value'>,
    затем с помощью метода POST происходит получение нужного значения name и phone.

    GET отображает данные в адресной строке, POST - нет, при этом важно
    прописать в html файле csrf токен: {% csrf_token %}, который позволяет защитить данные от csrf аттак.
    Данная защита не позволит сторонним сайтам напрямую обратиться к странице с обработчиком формы
    и сделать собственную запись. Сервер будет обрабатывать только те запросы,
    который пришли с нашего сайта с данной страницы.

    В класс Order добавляются два значения, затем создается экземпляр класса,
    после чего происходит сохранение в базу данных и отправление в шаблон thanks_page.html
    """
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks_page.html', {'name': name, 'phone': phone})
