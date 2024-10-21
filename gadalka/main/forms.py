from django import forms
from .models import MainModel


class MainForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = 'question', 'answer', 'session_key'
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Задайте свой вопрос'}),
            'answer': forms.TextInput(attrs={'style': 'display:none'}),
            'session_key': forms.TextInput(attrs={'style': 'display:none'})
        }

    def clean_question(self):
        question = self.cleaned_data['question']
        if len([x for x in question if x.isalpha()])>=2:
            return question
        else:
            raise forms.ValidationError('Вопрос задан не корректно')
            

