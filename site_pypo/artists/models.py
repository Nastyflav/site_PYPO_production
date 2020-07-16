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


class ArtistsCatalogPage(Page):
    """Model of the artistes catalog"""
    intro = RichTextField(blank=True)

    def get_context(self, request):
        """Update context to include only published artists, randomly ordered"""
        context = super().get_context(request)
        artists_pages = self.get_children().live().order_by('?')
        context['artists_pages'] = artistes_pages
        return context


class ArtistPage(Page):
    """All the fields to complete when editing an artist page"""
    name = models.DateField("Post date")
    style = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def main_image(self):
        """Print the artist image on top of the page"""
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('style'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('style'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class ArtistPageGalleryImage(Orderable):
    """Allows to integrate one image into an artiste page"""
    page = ParentalKey(ArtistPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]