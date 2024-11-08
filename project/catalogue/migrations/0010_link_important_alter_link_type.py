# Generated by Django 5.1.2 on 2024-11-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_alter_link_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='type',
            field=models.CharField(choices=[('OFFICIAL', 'Официальная документация'), ('API', 'Api'), ('TEMPLATES', 'Шаблоны'), ('FONTS', 'Шрифты'), ('PICS', 'Изображения, иконки и аватары'), ('MODIFY', 'Проверка и редактирование'), ('HOSTING', 'Хостинг'), ('TIPS', 'Шпаргалки и советы'), ('PRACTICE', 'Практика'), ('EXAMPLES', 'Примеры'), ('INTERVIEW', 'Для собеседования'), ('VIDEO', 'Видео материалы'), ('OTHER', 'Разное')], default='OFFICIAL', max_length=64, verbose_name='Тип ссылки'),
        ),
    ]