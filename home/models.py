from django.db import models

from wagtail.models import Page
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    content = RichTextField(blank=True)
    web_content = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("web_content", classname="full"),
        FieldPanel("content", classname="full"),
    ]
    api_fields = [
        APIField("content"),
    ]

    pass