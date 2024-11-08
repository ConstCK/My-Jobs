from django.utils.translation import gettext_lazy as _
from django.db import models


class ProjectType(models.TextChoices):
    TEST = 'TEST', _('Тестовый проект')
    PET = 'PET', _('Пет-проект')
    TEMPLATE = 'TEMPLATE', _('Шаблон проекта')
    SCHOOL = 'SCHOOL', _('Учебный проект')
    COMMERCIAL = 'COMMERCIAL', _('Коммерческий проект')


class LinkType(models.TextChoices):
    OFFICIAL = 'OFFICIAL', _('Официальная документация')
    API = 'API', _('Api')
    TEMPLATES = 'TEMPLATES', _('Шаблоны')
    FONTS = 'FONTS', _('Шрифты')
    PICS = 'PICS', _('Обои, иконки и аватарки')
    MODIFY = 'MODIFY', _('Проверка и редактирование')
    HOSTING = 'HOSTING', _('Хостинг')
    TIPS = 'TIPS', _('Шпаргалки и советы')
    PRACTICE = 'PRACTICE', _('Практика')
    EXAMPLES = 'EXAMPLES', _('Примеры')
    INTERVIEW = 'INTERVIEW', _('Для собеседования')
    VIDEO = 'VIDEO', _('Видео материалы')
    OTHER = 'OTHER', _('Разное')
