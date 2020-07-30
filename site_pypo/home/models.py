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
    
    class Meta:
        verbose_name = "Accueil"


class TermsPage(Page):
    """Model of the terms page"""
    subpage_types = []
    parent_page_types = ['home.HomePage']

    editor = RichTextField(verbose_name='Editeur')
    host = RichTextField(verbose_name='Hébergeur')
    photo_credits = RichTextField(verbose_name='Crédits photos')
    pypo = RichTextField(verbose_name='Exploitant')
    maker = RichTextField(verbose_name='Conception')
    graphism = RichTextField(verbose_name='Graphisme')
    cnil = RichTextField(verbose_name='CNIL')
    rights = RichTextField(verbose_name='Propriété intellectuelle')

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
            FieldPanel('rights'),
        ], heading="Informatique et liberté"),
    ]


class AssociationPage(Page):
    """Model of the association introducing page"""
    subpage_types = []
    parent_page_types = ['home.HomePage']

    body = RichTextField(verbose_name='Historique')

    def main_image(self):
        """Print the introducing image on top of the page"""
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Association"


class AssociationPageGalleryImage(Orderable):
    """Allows to integrate one image into the introducing page"""
    page = ParentalKey(AssociationPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]


class TeamPage(Page):
    """Create the models for the team page"""
    subpage_types = []
    parent_page_types = ['home.HomePage']

    content_panels = Page.content_panels + [
        InlinePanel('members', label="membre de l'équipe")
    ]

    class Meta:
        verbose_name = "Equipe"


class TeamPageMembers(Orderable):
    """To describe every team members"""
    page = ParentalKey(TeamPage, on_delete=models.CASCADE, related_name="members")
    firstname = models.CharField(max_length=50, verbose_name="Prénom")
    lastname = models.CharField(max_length=50, verbose_name="Nom")
    job = models.CharField(max_length=200, verbose_name="Poste")
    phone = models.CharField(max_length=15, verbose_name="Numéro")
    email = models.EmailField(verbose_name="Email")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('firstname'),
        FieldPanel('lastname'),
        FieldPanel('job'),
        FieldPanel('phone'),
        FieldPanel('email'),
        ImageChooserPanel('image'),
    ]
