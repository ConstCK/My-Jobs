from django.db import models


class Type(models.TextChoices):
    TEST = 'Тестовый проект'
    PET = 'Pet проект'
    TEMPLATE = 'Шаблон проекта'
    SCHOOL = 'Учебный проект'
    COMMERCIAL = 'Коммерческий проект'
