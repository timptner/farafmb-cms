from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


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
