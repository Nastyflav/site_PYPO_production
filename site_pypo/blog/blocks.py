#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-08-04
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.core.blocks import StructBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import StreamBlock


class VideoEmbedBlock(StructBlock):
   video = EmbedBlock(
       required=True,
       help_text="Insérer un lien comme par ex. https://youtu.be/yRmZ6WUfoOc"
   )

   class Meta:
       icon = 'media'
       label = "Vidéo intégrée"
       template = "blog/blocks/block_video_embed.html"


class BaseArticleStreamBlock(StreamBlock):
   video = VideoEmbedBlock()