from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import LogInForm, RegisterUserForm


# Обработчик регистрации нового пользователя с автоматической авторизацией
class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    extra_context = {'title': 'Регистрация'}

    # настройка автоматической авторизации при успешной регистрации пользователя
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            login(request, user)

            return render(request, 'registration/successful_signup.html',
                          context={'title': 'Успешная регистрация пользователя'})
        else:
            return render(request, self.template_name, {'form': form})


# Обработчик авторизации пользователя
class LogInView(LoginView):
    form_class = LogInForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация'}

# Альтернативный вариант (URLPatterns) использования данных для контекста встроенного класса
# class LogOutView(LogoutView):
#     extra_context = {'title': 'Успешный выход'}
