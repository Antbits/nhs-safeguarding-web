from django.db import models

# Create your models here.
from django.db import models
from wagtail.search import index
from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from wagtail.search.models import Query



class ContentIndexPage(Page):
    parent_page_types = ["home.HomePage"]
    search_auto_update = False 
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    api_fields = [
        APIField("content"),
    ]
    pass
class ContentSubIndexPage(Page):
    parent_page_types = ["home.HomePage","content.ContentIndexPage"]
    search_auto_update = False
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    api_fields = [
        APIField("content"),
    ]
    pass


class ContentPage(Page):
    parent_page_types = ["content.ContentIndexPage","content.ContentSubIndexPage"]
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['anchor-identifier','h1', 'h2', 'h3', 'h4', 'h5', 'h6','blockquote','warninglist','anchorlist','greyblockquotelist','blockquotelist','datestamp','scrolltop','apponly','webonly','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField('title',20),
        index.SearchField('content',1)
    ]
    api_fields = [
        APIField("content"),
    ]
class ContactPage(Page):
    parent_page_types = ["content.ContentIndexPage","content.ContentSubIndexPage"]
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['anchor-identifier','h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField('title',20),
        index.SearchField('content',1)
    ]
   
class ContactIndexPage(Page):
    search_auto_update = False 
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    
    pass
class ContactHomePage(Page):
    search_auto_update = False
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    api_fields = [
        APIField("content"),
    ]
    pass
class InfoPage(Page):
    parent_page_types = ["home.HomePage","content.ContentIndexPage","content.ContentSubIndexPage"]
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['anchor-identifier','h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField('title',20),
        index.SearchField('content',1)
    ]
    api_fields = [
        APIField("content"),
    ]
class SearchPage(Page):
    search_auto_update = False 
    parent_page_types = ["home.HomePage","content.ContentIndexPage","content.ContentSubIndexPage"]
class FooterPage(Page):
    search_auto_update = False 
    parent_page_types = ["home.HomePage","content.ContentIndexPage","content.ContentSubIndexPage"]
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6','datestamp','download','bold', 'italic','ol','ul','hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough'])),
        ('image', ImageChooserBlock()),
        ('raw_html',RawHTMLBlock())
    ])
    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    api_fields = [
        APIField("content"),
    ]