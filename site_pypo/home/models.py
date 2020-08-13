#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
                                         FieldPanel,
                                         InlinePanel,
                                         MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel

from artists.models import ArtistPage


class HomePage(Page):
    "Model of the home page"
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Bannière'
    )
    playlist_text = RichTextField(blank=True, verbose_name='Texte playlist')
    agenda_text = RichTextField(blank=True, verbose_name='Texte agenda')

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner'),
        MultiFieldPanel([
            InlinePanel('audio', label="Lien Spotify"),
            FieldPanel('playlist_text'),
        ], heading="Playlist"),
        FieldPanel('agenda_text'),
    ]

    @property
    def artists_infos(self):
        return ArtistPage.objects.live()

    class Meta:
        verbose_name = "Accueil"


class HomePagePlayer(Orderable):
    """To add an audio player into the homepage"""
    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="audio")
    link = models.URLField(
        max_length=300,
        null=True,
        verbose_name='Code embed',
        help_text="Ne garder que le lien du code\
                   embed, par ex. https://open.spotify.com/embed/album/***")

    panels = [
        FieldPanel('link'),
    ]


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
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Bannière'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Association"


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
    page = ParentalKey(
        TeamPage, on_delete=models.CASCADE, related_name="members")
    firstname = models.CharField(max_length=50, verbose_name="Prénom")
    lastname = models.CharField(max_length=50, verbose_name="Nom")
    job = models.CharField(max_length=200, verbose_name="Poste")
    phone = models.CharField(max_length=15, verbose_name="Numéro")
    email = models.EmailField(verbose_name="Email")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, verbose_name='Photo'
    )

    panels = [
        FieldPanel('firstname'),
        FieldPanel('lastname'),
        FieldPanel('job'),
        FieldPanel('phone'),
        FieldPanel('email'),
        ImageChooserPanel('image'),
    ]
