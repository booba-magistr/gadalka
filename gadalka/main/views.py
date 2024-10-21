from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from random import choice
from .models import MainModel
from .forms import MainForm

# Create your views here.
class HomeView(CreateView, ListView):
    form_class = MainForm
    model = MainModel
    template_name = 'main/index.html'
    context_object_name = 'answers'
    extra_context = {'count': MainModel.objects.all().count}
    success_url = reverse_lazy('main:home')

    def get_initial(self):
        initial = super().get_initial()
        initial['answer'] = choice([1, 0])
        return initial
    
    def get_queryset(self):
        return super().get_queryset().order_by('-pk')
