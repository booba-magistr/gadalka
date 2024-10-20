# Generated by Django 5.1.2 on 2024-10-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=93, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=16, verbose_name='Ответ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время вопроса')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
