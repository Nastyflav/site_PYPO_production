#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-08-18
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.tests.utils import WagtailPageTests

from contact.models import ContactPage 
from home.models import HomePage


class TestContactPage(WagtailPageTests):
    """To test the contact app models and arborescence"""
    def test_cant_create_under_contact_page(self):
        """Cannot create a page under ContactPage"""
        self.assertCanNotCreateAt(ContactPage, HomePage)

    def test_can_create_under_home_page(self):
        """Can create an ContactPage under a HomePage"""
        self.assertCanCreateAt(HomePage, ContactPage)

    def test_content_page_parent_pages(self):
        """ContactPage can only be created under an HomePage"""
        self.assertAllowedParentPageTypes(ContactPage, {HomePage})