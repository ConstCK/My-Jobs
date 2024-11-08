from django import template
from django.urls import reverse

register = template.Library()


# Пользовательский тег для шаблона для изменения класса тега (Выбор текущего
# тега в зависимости от маршрута)
@register.simple_tag(takes_context=True)
def get_active_class(context, url: str, *args) -> str:
    if context.get('request').path == reverse(url, args=args):
        return "active"
    return ""


# Пользовательский тег для шаблона для изменения класса тега
# (Проверка ссылки на important=True)
@register.simple_tag(takes_context=False)
def is_important_link(data) -> str:
    if data:
        return "important-link"
    return ""


# Пользовательский тег для шаблона для добавления в шаблон смайлика
# (Проверка ссылки на important=True)
@register.simple_tag(takes_context=False)
def smile_for_important_link(data) -> str:
    if data:
        return "😍"
    return ""
