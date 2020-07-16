#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-16
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class EventsIndexPage(Page):
    """Model of the events catalog"""
    intro = RichTextField(blank=True)

    def get_context(self, request):
        """Update context to include only published events, ordered by reverse-chron"""
        context = super().get_context(request)
        events_pages = self.get_children().live().order_by('-first_published_at')
        context['events_pages'] = events_pages
        return context
