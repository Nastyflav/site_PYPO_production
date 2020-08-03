#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-17
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase

from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield

from artists.models import ArtistPage, ArtistsCatalogPage, ArtistPageGalleryImage
from home.models import HomePage


class TestArtistsPages(WagtailPageTests):
    """To test the artists app models"""
    def test_can_create_an_artist_page(self):
        """Can create a page under the Artist Catalog Page"""
        self.assertCanCreateAt(ArtistsCatalogPage, ArtistPage)

    def test_cant_create_under_artist_page(self):
        """Cannot create a page under Artist Page"""
        self.assertCanNotCreateAt(ArtistPage, HomePage)

    def test_can_create_under_home_page(self):
        """Can create an ArtistCatalogPage under a HomePage"""
        self.assertCanCreateAt(HomePage, ArtistsCatalogPage)

    def test_content_page_parent_pages(self):
        """ArtistPage can only be created under an ArtistCatalogPage"""
        self.assertAllowedParentPageTypes(ArtistPage, {ArtistsCatalogPage})
        """ArtistCatalogPage can only be created under a Home Page"""
        self.assertAllowedParentPageTypes(ArtistsCatalogPage, {HomePage})
