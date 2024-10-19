from django.db import models

# Create your models here.
class MainModel(models.Model):
    question = models.CharField(max_length=93, verbose_name='Вопрос')
    answer = models.CharField(max_length=16, verbose_name='Ответ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время вопроса")

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'