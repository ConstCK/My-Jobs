from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .constants import ProjectType, LinkType


class Language(models.Model):
    name = models.CharField(max_length=9, unique=True, verbose_name='Язык программирования')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
        ordering = ['name']


class Technology(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Технология')
    description = models.CharField(max_length=256, null=True, blank=True,
                                   verbose_name='Описание технологии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'
        ordering = ['name']


class Feature(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Особенность')
    description = models.CharField(max_length=256, null=True, blank=True,
                                   verbose_name='Описание особенности')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'
        ordering = ['name']


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название проекта')
    description = models.CharField(max_length=512, verbose_name='Описание проекта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор проекта')
    created_at = models.DateField(verbose_name='Дата создания проекта')
    type = models.CharField(max_length=64, choices=ProjectType.choices, default=ProjectType.PET,
                            verbose_name='Тип проекта')
    git_url = models.URLField(unique=True, null=True, blank=True, verbose_name='Ссылка на GitHub')
    pc_url = models.CharField(max_length=512, unique=True, verbose_name='Ссылка на папку проекта')
    languages = models.ManyToManyField('Language',
                                       verbose_name='Используемый язык программирования')
    technologies = models.ManyToManyField('Technology',
                                          verbose_name='Используемая технология')
    features = models.ManyToManyField('Feature', blank=True,
                                      verbose_name='Особенности проекта')

    def __str__(self):
        return f'Проект {self.name} создан {self.author}'

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['name']


class Link(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название ссылки')
    type = models.CharField(max_length=64, choices=LinkType.choices,
                            default=LinkType.OFFICIAL,
                            verbose_name='Тип ссылки')
    link_url = models.URLField(unique=True, null=True, blank=True,
                               verbose_name='Ссылка на полезную страницу')
    important = models.BooleanField(default=False, verbose_name='Важная ссылка?')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['name']
        constraints = (models.UniqueConstraint(fields=('name', 'type'), name='Unique constraint'), )
