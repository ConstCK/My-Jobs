# Generated by Django 5.1.2 on 2024-11-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_alter_link_type_link_unique_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название ссылки'),
        ),
    ]
