from django.shortcuts import render
from .models import Product

def home(request):
    # Получаем последние 5 добавленных товаров
    latest_products = Product.objects.order_by('-id')[:5]  #  '-id' для сортировки от новых к старым

    context = {
        'latest_products': latest_products,
    }

    return render(request, 'shop/home.html', context)


def register(request): # добавили функцию
    return render(request, 'shop/register.html')

def login_view(request):
    return render(request, 'shop/login.html')

def service(request):
    return render(request, 'shop/service.html')