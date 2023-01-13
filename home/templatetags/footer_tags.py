from django import template
from home.models import FooterGroup

register = template.Library()


@register.inclusion_tag('home/tags/links.html', takes_context=True)
def links(context):
    return {
        'groups': FooterGroup.objects.all(),
        'request': context['request'],
    }
