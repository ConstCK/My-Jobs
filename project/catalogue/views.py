from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import ProjectForm
from .models import Project, Language, Technology, Feature
from .utils import CategoriesMixin, ProjectsDataMixin


# Представление для получения всех проектов
class AllProjects(CategoriesMixin, ProjectsDataMixin, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        category = 'Все'
        context = super().get_context_data(**kwargs)
        initial_context = self.get_user_context(title='Главная страница',
                                                category=category)
        context.update(initial_context)
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Project.objects.filter(author=self.request.user).order_by('-created_at')
        else:
            queryset = []
        return queryset


# Представление для получения проектов с указанным языком программирования
class ProjectsByLanguage(CategoriesMixin, ProjectsDataMixin, ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        category = f'Язык программирования -> {self.kwargs.get('name')}'
        context = super().get_context_data(**kwargs)
        initial_context = self.get_user_context(title='Главная страница',
                                                category=category)
        context.update(initial_context)
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Project.objects.filter(author=self.request.user,
                                              languages__name=self.kwargs.get('name')).order_by('-created_at')
        else:
            queryset = []
        return queryset


# Представление для получения проектов с указанной использованной технологией
class ProjectsByTechnology(CategoriesMixin, ProjectsDataMixin, ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        category = f'Использование {self.kwargs.get('name')}'
        context = super().get_context_data(**kwargs)
        initial_context = self.get_user_context(title='Главная страница',
                                                category=category)

        context.update(initial_context)
        context['description'] = initial_context.get('technologies').filter(name=self.kwargs.get('name'))[0].description
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Project.objects.filter(author=self.request.user,
                                              technologies__name=self.kwargs.get('name')).order_by('-created_at')
        else:
            queryset = []
        return queryset


# Представление для получения проектов с указанной использованной особенностью
class ProjectsByFeature(CategoriesMixin, ProjectsDataMixin, ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        category = f'Использование {self.kwargs.get('name')}'
        context = super().get_context_data(**kwargs)
        initial_context = self.get_user_context(title='Главная страница',
                                                category=category)
        context.update(initial_context)
        context['description'] = initial_context.get('features').filter(name=self.kwargs.get('name'))[0].description
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Project.objects.filter(author=self.request.user,
                                              features__name=self.kwargs.get('name')).order_by('-created_at')
        else:
            queryset = []
        return queryset


# Представление для добавления языка программирования
class LanguageAdd(LoginRequiredMixin, CreateView):
    model = Language
    template_name = 'language_create.html'
    context_object_name = 'object'
    extra_context = {'title': 'Добавление языка программирования'}
    fields = ['name', ]
    success_url = reverse_lazy('successful_create')


# Представление для добавления технологии
class TechnologyAdd(CreateView):
    model = Technology
    template_name = 'technology_create.html'
    context_object_name = 'object'
    extra_context = {'title': 'Добавление технологии'}
    fields = '__all__'
    success_url = reverse_lazy('successful_create')


# Представление для добавления особенности
class FeatureAdd(CreateView):
    model = Feature
    template_name = 'feature_create.html'
    context_object_name = 'object'
    extra_context = {'title': 'Добавление особенности'}
    fields = '__all__'
    success_url = reverse_lazy('successful_create')


# Представление для добавления проекта
class ProjectAdd(CreateView):
    form_class = ProjectForm
    template_name = 'project_create.html'
    context_object_name = 'project'
    extra_context = {'title': 'Добавление проекта'}
    success_url = reverse_lazy('successful_create')

    # Добавления автора (текущего пользователя) проекта в форму
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Представление для получения полной информации о проекте
class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_details.html'
    context_object_name = 'project'
    extra_context = {'title': 'Детали проекта'}

    # Переопределения метода для оптимизации запроса (Использование жадной загрузки)
    def get_queryset(self):
        queryset = (Project.objects.filter(pk=self.kwargs.get('pk'))
                    .prefetch_related('languages', 'technologies', 'features'))
        return queryset


# Представление для изменения данных в существующем проекте
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_update.html'
    context_object_name = 'project'
    extra_context = {'title': 'Обновление данных проекта'}
    fields = ['name', 'description', 'type', 'git_url', 'pc_url', 'languages',
              'technologies', 'features']
    success_url = reverse_lazy('successful_update')


# Представление для выбора языка программирования для удаления
class LanguageSelect(LoginRequiredMixin, ListView):
    model = Language
    context_object_name = 'languages'
    template_name = 'language_list.html'
    extra_context = {'title': 'Выбор языка программирования для удаления'}


# Представление для выбора технологии для удаления
class TechnologySelect(LoginRequiredMixin, ListView):
    model = Technology
    context_object_name = 'technologies'
    template_name = 'technology_list.html'
    extra_context = {'title': 'Выбор технологии для удаления'}


# Представление для выбора особенности для удаления
class FeatureSelect(LoginRequiredMixin, ListView):
    model = Feature
    context_object_name = 'features'
    template_name = 'feature_list.html'
    extra_context = {'title': 'Выбор особенности для удаления'}


# Представление для удаления технологии
class LanguageDelete(LoginRequiredMixin, DeleteView):
    model = Language
    template_name = 'language_delete.html'
    extra_context = {'title': 'Удаление языка программирования'}
    success_url = reverse_lazy('successful_delete')

    # Способ передачи данных в функцию-обработчик успешного удаления объекта
    def get_success_url(self, *args, **kwargs):
        obj = Language.objects.get(pk=self.get_object().id)
        return reverse_lazy('successful_delete',
                            kwargs={'obj': f'Язык программирования {obj.name}'})


# Представление для удаления технологии
class TechnologyDelete(LoginRequiredMixin, DeleteView):
    model = Technology
    template_name = 'technology_delete.html'
    extra_context = {'title': 'Удаление технологии'}
    success_url = reverse_lazy('successful_delete')

    # Способ передачи данных в функцию-обработчик успешного удаления объекта
    def get_success_url(self, *args, **kwargs):
        obj = Technology.objects.get(pk=self.get_object().id)
        return reverse_lazy('successful_delete',
                            kwargs={'obj': f'Технология {obj.name}'})


# Представление для удаления особенности
class FeatureDelete(LoginRequiredMixin, DeleteView):
    model = Feature
    template_name = 'feature_delete.html'
    extra_context = {'title': 'Удаление особенности'}
    success_url = reverse_lazy('successful_delete')

    # Способ передачи данных в функцию-обработчик успешного удаления объекта
    def get_success_url(self, *args, **kwargs):
        obj = Feature.objects.get(pk=self.get_object().id)
        return reverse_lazy('successful_delete',
                            kwargs={'obj': f'Особенность {obj.name}'})

    # Альтернативный способ передачи данных в функцию-обработчик успешного удаления объекта
    # def get_success_url(self, *args, **kwargs):
    #     obj = Feature.objects.get(pk=self.get_object().id)
    #     data = f"Особенность {obj}"
    #     return reverse_lazy('successful_delete') + '?' + 'obj=' + data


# Представление для удаления проекта
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'
    extra_context = {'title': 'Удаление проекта'}
    success_url = reverse_lazy('successful_delete')

    # Способ передачи данных в функцию-обработчик успешного удаления объекта
    def get_success_url(self, *args, **kwargs):
        obj = Project.objects.get(pk=self.get_object().id)
        return reverse_lazy('successful_delete',
                            kwargs={'obj': f'Проект {obj.name}'})


# Представления для вывода страницы с меню добавления различных объектов (Проект,
# Язык программирования, Технология, Особенность)
class DataView(LoginRequiredMixin, TemplateView):
    template_name = 'data_page.html'


# Представления для вывода страницы "О проекте"
class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {'title': 'О приложении'}


# Представления для вывода страницы "Успешное создание объекта"
class SuccessfulCreateView(TemplateView):
    template_name = 'successful_create.html'
    extra_context = {'title': 'Удачное создание объекта'}


# Представления для вывода страницы "Успешное обновление объекта"
class SuccessfulUpdateView(TemplateView):
    template_name = 'successful_update.html'
    extra_context = {'title': 'Удачное обновление проекта'}


# Представления для вывода страницы "Успешное удаление объекта"
class SuccessfulDeleteView(TemplateView):
    template_name = 'successful_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удачное удаление объекта'
        context['object'] = self.kwargs.get('obj')
        return context

