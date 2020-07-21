#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-21
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield

from home.models import HomePage, TermsPage, AssociationPage


class TestHomeModels(WagtailPageTests):
    """To test the blog app models"""
    def test_can_create_a_terms_page(self):
        """Can create a page under the HomePage"""
        self.assertCanCreateAt(HomePage, TermsPage)

    def test_cant_create_under_terms_page(self):
        """Cannot create a page under BlogPage"""
        self.assertCanNotCreateAt(TermsPage, HomePage)

    def test_cant_create_under_asso_page(self):
        """Cannot create a page under BlogPage"""
        self.assertCanNotCreateAt(AssociationPage, HomePage)

    def test_content_page_parent_pages(self):
        """TermsPage can only be created under a HomePage"""
        self.assertAllowedParentPageTypes(TermsPage, {HomePage})
        """AssoPage can only be created under a HomePage"""
        self.assertAllowedParentPageTypes(AssociationPage, {HomePage})
