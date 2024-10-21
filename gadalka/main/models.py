from django.db import models

# Create your models here.
class MainModel(models.Model):
    question = models.CharField(max_length=93, verbose_name='Вопрос')
    answer = models.IntegerField(verbose_name='Ответ')
    session_key = models.CharField(max_length=200, verbose_name='Ключ сессии', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время вопроса")

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'