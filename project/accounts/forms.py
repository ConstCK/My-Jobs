from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Форма регистрации
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Форма авторизации
class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
