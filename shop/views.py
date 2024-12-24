from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import Product

def home(request):
    latest_products = Product.objects.order_by('-id')[:5]
    context = {
        'latest_products': latest_products,
    }
    return render(request, 'shop/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались.')
            return redirect('authorized_home')
    else:
        form = RegistrationForm()
    return render(request, 'shop/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('authorized_home')
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

def service(request):
   products = Product.objects.all()
   context = {
        'products': products,
    }
   return render(request, 'shop/service.html', context)

def logout_view(request):
   logout(request)
   messages.success(request, 'Вы вышли из системы.')
   return redirect('home')

def authorized_home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/authorized_home.html', context)