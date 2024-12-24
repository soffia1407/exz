from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")
    avatar = forms.ImageField(required=False, label="Аватар пользователя") # требуется False, если не хотите, чтобы поле было обязательным

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email'] # username - это логин
        labels = {
          'username': "Логин",
          'first_name': "Имя пользователя",
          'email': "Почта"
        }


