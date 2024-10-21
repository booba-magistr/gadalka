from django.contrib import admin
from .models import MainModel

# Register your models here.
@admin.register(MainModel)
class MainAdmin(admin.ModelAdmin):
    fields = 'question', 'get_answer', 'session_key', 'time_create'
    list_display = 'pk', 'question', 'get_answer', 'session_key', 'time_create'
    readonly_fields = 'time_create', 'get_answer', 'question', 'session_key'
    ordering = 'pk',
    list_per_page = 20
    search_fields = 'question',
    list_display_links = 'question', 
    
    @admin.display(description='Ответ')
    def get_answer(self, model:MainModel):
        if model.answer:
            return 'Да'
        return 'Нет'