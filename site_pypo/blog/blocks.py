#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-08-17
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.core.blocks import (
                                 StructBlock,
                                 ChoiceBlock,
                                 RichTextBlock,
                                 CharBlock)
from wagtail.embeds.blocks import EmbedBlock


class InlineVideoBlock(StructBlock):
    """Video block settings"""
    title = CharBlock(required=True, label='Type de recommandation')
    richtext_content = RichTextBlock(required=True)
    video = EmbedBlock(
        label='Vidéo',
        help_text="Insérer une url comme par ex. https://youtu.be/yRmZ6WUfoOc"
    )
    position = ChoiceBlock(
        required=False,
        choices=[
            ('right', 'Droite'), ('left', 'Gauche'), ('center', 'Centre')],
        default='left',
        label='Position'
    )
    size = ChoiceBlock(
        required=False,
        choices=[
            ('small', 'Petit'), ('medium', 'Médium'), ('large', 'Grand')],
        default='medium',
        label='Taille'
    )

    class Meta:
        icon = 'media'
        label = "Recommandation vidéo"


class InlineTextBlock(StructBlock):
    """Text block settings"""
    title = CharBlock(required=True, label='Type de recommandation')
    richtext_content = RichTextBlock(required=True, label='Description vidéo')
    position = ChoiceBlock(
        required=False,
        choices=[
            ('right', 'Droite'), ('left', 'Gauche'), ('center', 'Centre')],
        default='left',
        label='Position'
    )
    size = ChoiceBlock(
        required=False,
        choices=[
            ('small', 'Petit'), ('medium', 'Médium'), ('large', 'Grand')],
        default='medium',
        label='Taille'
    )

    class Meta:
        icon = 'edit'
        label = "Recommandations texte"
