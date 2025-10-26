from django import template

register = template.Library()

@register.filter(name='fupper')
def full_upper(value):
    result = value.upper()
    return result

@register.filter(name='Datef')
def date_format(value):
    result = value.strftime('%d-%m-%Y')
    return result