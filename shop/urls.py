from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('service/', views.service, name='service'),
    path('logout/', views.logout_view, name='logout'),
    path('authorized_home/', views.authorized_home, name='authorized_home'),
]