from django import forms


class OrderForm(forms.Form):
    """
    Форма заполнения данных:
    name - поле ввода имени,
    аттрибут max_length - максимальная длина в количестве символов,
    required - обязательное ли поле для заполнения.

    Чтобы отображать форму как параграф, в шаблоне прописывается {{ form.as_p }}.

    Для отображения стилей, в шаблоне прописывается стиль и добавляется
    аттрибут widget с forms.TextInput с аттрибутом нужного класса:
    widget=forms.TextInput(attrs={'class': 'form-control'})
    """
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
