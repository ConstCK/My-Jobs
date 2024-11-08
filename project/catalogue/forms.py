import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import Project, Link


# Форма для добавления нового проекта с дополнительной валидацией некоторых полей
class ProjectForm(forms.ModelForm):
    created_at = forms.CharField(label='Дата создания проекта',
                                 widget=DateInput(attrs={'placeholder': 'В формате 21.01.1999'}), )

    # Переопределение метода для валидации некоторых полей
    def clean(self):
        cleaned_data = super().clean()
        try:
            cleaned_data['created_at'] = (datetime.datetime.
                                          strptime(str(cleaned_data.get('created_at')),
                                                   '%d.%m.%Y'))
        except ValueError:
            raise ValidationError('Введите дату в формате ДД.ММ.ГГГГ')
        if not cleaned_data.get('pc_url').startswith('C:\\Users\\'):
            raise ValidationError('Неверно указан путь к директории проекта')
        return cleaned_data

    class Meta:
        model = Project
        exclude = ['author']


# Форма для добавления новой ссылки
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
