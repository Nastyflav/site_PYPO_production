#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-17
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield

from artists.models import ArtistPage, ArtistsCatalogPage, ArtistPageGalleryImage


class TestArtistsModels(WagtailPageTests):
    """To test the artists app models"""
    def test_can_create_a_page(self):
        """Can create a page under the Artist Catalog Page"""
        self.assertCanCreateAt(ArtistsCatalogPage, ArtistPage)
