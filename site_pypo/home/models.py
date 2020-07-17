#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-15
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


class HomePage(Page):
    pass


class TermsPage(Page):
    """Model of the terms page"""
    editor = RichTextField(verbose_name='Editeur')
    host = RichTextField(verbose_name='Hébergeur')
    photo_credits = RichTextField(verbose_name='Crédits photos')
    pypo = RichTextField(verbose_name='Exploitant')
    maker = RichTextField(verbose_name='Conception')
    graphism = RichTextField(verbose_name='Graphisme')
    cnil = RichTextField(verbose_name='CNIL')
    _copyright = RichTextField(verbose_name='Propriété intellectuelle')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('editor'),
            FieldPanel('host'),
            FieldPanel('photo_credits'),
            FieldPanel('pypo'),
            FieldPanel('maker'),
            FieldPanel('graphism'),
        ], heading="Informations générales"),
        MultiFieldPanel([
            FieldPanel('cnil'),
            FieldPanel('_copyright'),
        ], heading="Informatique et liberté"),
    ]

