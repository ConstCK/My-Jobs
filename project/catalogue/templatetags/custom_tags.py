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
