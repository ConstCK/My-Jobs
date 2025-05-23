# Generated by Django 5.1.2 on 2024-11-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_project_features_alter_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название ссылки')),
                ('type', models.CharField(choices=[('Официальная документация', 'Official'), ('Api', 'Api'), ('Шаблоны', 'Templates'), ('Шрифты', 'Fonts'), ('Обои, иконки и аватарки', 'Pics'), ('Проверка и редактирование', 'Modify'), ('Хостинг', 'Hosting'), ('Шпаргалки и советы', 'Tips'), ('Практика', 'Practice'), ('Примеры', 'Examples'), ('Для собеседования', 'Interview'), ('Разное', 'Other')], max_length=64, verbose_name='Тип ссылки')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['name'], 'verbose_name': 'Особенность', 'verbose_name_plural': 'Особенности'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name'], 'verbose_name': 'Язык программирования', 'verbose_name_plural': 'Языки программирования'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name': 'Технология', 'verbose_name_plural': 'Технологии'},
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Тестовый проект', 'Test'), ('Pet проект', 'Pet'), ('Шаблон проекта', 'Template'), ('Учебный проект', 'School'), ('Коммерческий проект', 'Commercial')], default='Pet проект', max_length=64, verbose_name='Тип проекта'),
        ),
    ]
