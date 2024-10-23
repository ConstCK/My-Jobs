from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import RegisterView, LogInView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    # Маршрут для страницы после выхода из аккаунта с передачей дополнительного контекста к встроенному обработчику
    path('logout/', LogoutView.as_view(extra_context={'title': 'Успешный выход'}),
         {'next_page': 'registration/logged_out.html'}, name='logout'),
]
