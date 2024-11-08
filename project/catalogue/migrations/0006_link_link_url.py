# Generated by Django 5.1.2 on 2024-11-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_link_alter_feature_options_alter_language_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на полезную страницу'),
        ),
    ]
