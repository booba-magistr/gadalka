from django import template
from main.models import MainModel

register = template.Library()

@register.simple_tag()
def list_answers():
    return MainModel.objects.all().order_by('-pk')