from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm

def home(request):
    # Получаем последние 5 добавленных товаров
    latest_products = Product.objects.order_by('-id')[:5]  #  '-id' для сортировки от новых к старым

    context = {
        'latest_products': latest_products,
    }

    return render(request, 'shop/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES) #  связываем данные с формой.
        if form.is_valid(): # валидируем данные
            user = form.save() # сохраняем данные пользователя в бд
            login(request, user) # автоматическая авторизация после регистрации
            messages.success(request, 'Вы успешно зарегистрировались.') # создаем сообщение об успехе
            return redirect('login') # перенаправляем на страницу авторизации
    else: # если метод GET
        form = RegistrationForm() # создаем пустую форму
    return render(request, 'shop/register.html', {'form': form}) # передаем форму в шаблон

def login_view(request):
    return render(request, 'shop/login.html')

def service(request):
    return render(request, 'shop/service.html')