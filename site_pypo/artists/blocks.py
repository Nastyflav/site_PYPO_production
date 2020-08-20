#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-08-03
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.core.blocks import StructBlock, ChoiceBlock
from wagtail.embeds.blocks import EmbedBlock


class InlineVideoBlock(StructBlock):
    """Video block settings"""
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
        choices=[('small', 'Petit'), ('medium', 'Médium'), ('large', 'Grand')],
        default='medium',
        label='Taille'
    )

    class Meta:
        icon = 'media'
        label = "Vidéo intégrée"
