Приложение для управления своими проектами и полезными ссылками на документацию библиотек
и другую полезную информацию. 

* Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/My-Jobs.git
* Перейдите в папку проекта
* В терминале создайте виртуальное окружение (например python -m venv venv) и активируйте его (venv\scripts\activate)
* Установите все зависимости при помощи pip install -r requirements.txt
* Создайте файл .env в каталоге проекта и пропишите в нем настройки по примеру .env.example
Например ключ для Django можно сгенерировать по пути https://realorangeone.github.io/django-secret-key-generator/
или в python консоли при помощи "from django.core.management.utils import get_random_secret_key, get_random_secret_key()"
* Запустите сервер из каталога проекта (project/python manage.py runserver)

