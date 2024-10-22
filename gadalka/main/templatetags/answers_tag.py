from django import template
from main.models import MainModel

register = template.Library()

@register.simple_tag()
def current_answer(request):
    return MainModel.objects.filter(session_key=request.session.session_key)

@register.simple_tag()
def list_answers():
    return MainModel.objects.all().order_by('-pk')