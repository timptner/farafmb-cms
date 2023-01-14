from django import template
from wagtail.models import Page

register = template.Library()


@register.simple_tag()
def list_pages():
    return Page.objects.live().in_menu()
