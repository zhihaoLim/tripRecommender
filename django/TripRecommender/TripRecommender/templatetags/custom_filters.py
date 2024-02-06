from django import template

register = template.Library()

@register.filter(name='add_png')
def add_png(value):
    return f"{value}.png"