#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-21
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase 

from wagtail.tests.utils import WagtailPageTests

from events.models import EventsIndexPage, EventPage
from home.models import HomePage


class TestEventsModels(WagtailPageTests):
    """To test the events pages arborescence"""
    def test_can_create_an_event_page(self):
        """Can create a page under the EventsIndexPage"""
        self.assertCanCreateAt(EventsIndexPage, EventPage)

    def test_cant_create_under_artist_page(self):
        """Cannot create a page under EventPage"""
        self.assertCanNotCreateAt(EventPage, HomePage)

    def test_can_create_under_home_page(self):
        """Can create an EventsIndexPage under a HomePage"""
        self.assertCanCreateAt(HomePage, EventsIndexPage)

    def test_content_page_parent_pages(self):
        """EventPage can only be created under an EventsIndexPage"""
        self.assertAllowedParentPageTypes(EventPage, {EventsIndexPage})
        """EventsIndexPage can only be created under a HomePage"""
        self.assertAllowedParentPageTypes(EventsIndexPage, {HomePage})
