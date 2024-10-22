from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from random import choice
from .models import MainModel
from .forms import MainForm

# Create your views here.
class HomeView(CreateView):
    form_class = MainForm
    model = MainModel
    template_name = 'main/index.html'
    extra_context = {'count': MainModel.objects.all().count}
    success_url = reverse_lazy('main:home')

    def get_initial(self):
        initial = super().get_initial()
        initial['answer'] = choice([1, 0])
        initial['session_key'] = self.request.session.session_key
        return initial

