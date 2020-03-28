from django import template
from articles.models import Scripts

register = template.Library()



@register.simple_tag
def header_scripts():
    return Scripts.objects.get(shortcode='header')

@register.simple_tag
def footer_scripts():
    return Scripts.objects.get(shortcode='footer')

