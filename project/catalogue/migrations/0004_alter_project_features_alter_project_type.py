# Generated by Django 5.1.2 on 2024-10-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_feature_description_alter_project_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='features',
            field=models.ManyToManyField(blank=True, to='catalogue.feature', verbose_name='Особенности проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('Тестовый проект', 'Test'), ('Pet проект', 'Pet'), ('Шаблон проекта', 'Template'), ('Учебный проект', 'School')], default='Pet проект', max_length=64, verbose_name='Тип проекта'),
        ),
    ]
