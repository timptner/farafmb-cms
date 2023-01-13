from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    body = RichTextField(
        features=[
            'h3', 'h4', 'h5', 'h6',
            'bold', 'italic',
            'ol', 'ul',
            'hr',
            'link',
        ],
        blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('image'),
    ]


@register_snippet
class FooterGroup(models.Model):
    title = models.CharField(max_length=250)

    panels = [
        FieldPanel('title'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class FooterLink(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    group = models.ForeignKey(FooterGroup, on_delete=models.CASCADE)

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
        FieldPanel('group'),
    ]

    def __str__(self):
        return self.title
