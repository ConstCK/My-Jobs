from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Language, Technology, Feature


# Создание объектов в БД при их отсутствии при регистрации нового пользователя
@receiver(post_save, sender=User)
def initial_task(sender, instance, created, **kwargs):
    if created:
        try:
            Language.objects.create(name='Python')
            Language.objects.create(name='JavaScript')
            Technology.objects.create(name='Django',
                                      description='Фреймворк для веб разработки')
            Technology.objects.create(name='FastAPI',
                                      description='Фреймворк для веб разработки')
            Technology.objects.create(name='DRF',
                                      description='Библиотека для создания REST API')
            Technology.objects.create(name='Aiogram',
                                      description='Библиотека для создания Telegram бота')
            Technology.objects.create(name='Redis',
                                      description='Библиотека для связи с Redis сервером управления No SQl DB')
            Technology.objects.create(name='React',
                                      description='Библиотека для FrontEnd разработки')
            Technology.objects.create(name='Vue',
                                      description='Библиотека для FrontEnd разработки')
            Technology.objects.create(name='Vuex',
                                      description='Библиотека для использование единого состояния (хранилища данных)')
            Technology.objects.create(name='Redux',
                                      description='Библиотека для использование единого состояния (хранилища данных)')
            Technology.objects.create(name='Pytest',
                                      description='Библиотека для тестирование проекта')
            Technology.objects.create(name='Jsonlines',
                                      description='Библиотека для работы с Json файлами')
            Technology.objects.create(name='pyTelegramBotAPI',
                                      description='Библиотека для создания Telegram бота')
            Technology.objects.create(name='Gspread',
                                      description='Библиотека для работы с Google таблицами')
            Technology.objects.create(name='Pandas',
                                      description='Библиотека для работы массивами данных')
            Technology.objects.create(name='Sqlite3',
                                      description='Библиотека для работы с Sqlite3 БД')
            Technology.objects.create(name='Requests',
                                      description='Библиотека для создания запросов')
            Technology.objects.create(name='ApScheduler',
                                      description='Библиотека для планирования задач')
            Technology.objects.create(name='Vue-chartjs',
                                      description='Библиотека для построения графиков')
            Technology.objects.create(name='V-calendar',
                                      description='Библиотека для создания виджета с календарем')
            Technology.objects.create(name='Axios',
                                      description='Библиотека для создания запросов')
            Technology.objects.create(name='Slowapi',
                                      description='Библиотека для лимитирования запросов')
            Technology.objects.create(name='Logging',
                                      description='Библиотека для логирования')
            Technology.objects.create(name='Yookassa',
                                      description='Библиотека для использования платежной системы Yookassa')
            Technology.objects.create(name='Drf-spectacular',
                                      description='Библиотека для использования Swagger')
            Technology.objects.create(name='Django-CKEditor',
                                      description='Библиотека для редактирования текста в Django панели администрирования')
            Technology.objects.create(name='Django-Apscheduler',
                                      description='Библиотека для выполнения запланированных задач')
            Feature.objects.create(name='Docker',
                                   description='Контейнеризация запуска приложения')
            Feature.objects.create(name='PostgreSQL',
                                   description='Использование PostgreSQL БД')
            Feature.objects.create(name='MySQL',
                                   description='Использование MySQL БД')
            Feature.objects.create(name='Async',
                                   description='Асинхронный подход')
            Feature.objects.create(name='SCSS',
                                   description='Использование CSS-предпроцессора')
            Feature.objects.create(name='CSS variables',
                                   description='Использование CSS переменных')
            Feature.objects.create(name='CSS mixins',
                                   description='Использование CSS примесей')
            Feature.objects.create(name='CSS mixins',
                                   description='Использование CSS примесей')
            Feature.objects.create(name='Pre-compile',
                                   description='Использование проверки на ошибки перед запуском проекта')
            Feature.objects.create(name='Django tests',
                                   description='Тестирование Django проекта')
            Feature.objects.create(name='JWT authorization',
                                   description='Авторизация при помощи JWT')
            Feature.objects.create(name='Custom tags',
                                   description='Использование пользовательских тегов в Django templates')
            Feature.objects.create(name='Email filters',
                                   description='Использование пользовательских фильтров в Django templates')
            Feature.objects.create(name='Кэширование',
                                   description='Использование кэширования данных')
            Feature.objects.create(name='Email sending',
                                   description='Почтовая рассылка')
            Feature.objects.create(name='Registration confirmation',
                                   description='Подтверждение регистрации')
        except IntegrityError:
            pass
