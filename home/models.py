from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page


from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('home.BlogPage', on_delete=models.CASCADE, related_name='tagged_items')

class BlogPage(Page):
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]
    promote_panels= Page.promote_panels + [
        FieldPanel('tags'),
    ]
    content_panels = Page.content_panels + [

        FieldPanel('date'),
        StreamFieldPanel('body', classname="full"),
    ]
    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        main_pages = MainPage.objects.all()
        context['mainpages'] = main_pages
        parent = MainPage.objects.parent_of(self).live().first()

        context['label'] = parent.label
        return context

    parent_page_types = ['home.MainPage']

class MainPage(Page):
    general = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    label = models.TextField()
    content_panels=Page.content_panels + [FieldPanel('label'),  StreamFieldPanel('general')]
    def get_context(self, request):
        context = super(MainPage, self).get_context(request)
        main_pages = MainPage.objects.all()
        blogpages = BlogPage.objects.live().descendant_of(self).order_by('-first_published_at')
        context['blogpages'] = blogpages

        context['mainpages'] = main_pages
        context['label'] = self.label
        return context

class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels=Page.content_panels + [FieldPanel('body', classname="full")]
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        main_pages = MainPage.objects.all()
        context['mainpages'] = main_pages
        return context
