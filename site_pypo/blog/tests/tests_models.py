#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-07-21
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from wagtail.tests.utils import WagtailPageTests

from blog.models import BlogIndexPage, BlogPage
from home.models import HomePage


class TestBlogModels(WagtailPageTests):
    """To test the blog app models"""
    def test_can_create_a_blogt_page(self):
        """Can create a page under the BlogIndexPage"""
        self.assertCanCreateAt(BlogIndexPage, BlogPage)

    def test_cant_create_under_blog_page(self):
        """Cannot create a page under BlogPage"""
        self.assertCanNotCreateAt(BlogPage, HomePage)

    def test_can_create_under_home_page(self):
        """Can create an BlogIndexPage under a HomePage"""
        self.assertCanCreateAt(HomePage, BlogIndexPage)

    def test_content_page_parent_pages(self):
        """BlogPage can only be created under an BlogIndexPage"""
        self.assertAllowedParentPageTypes(BlogPage, {BlogIndexPage})
        """BlogIndexPage can only be created under a Home Page"""
        self.assertAllowedParentPageTypes(BlogIndexPage, {HomePage})

    def test_content_blogindexpage_subpages(self):
        """# A BlogIndexPage can only have BlogPage children"""
        self.assertAllowedSubpageTypes(BlogIndexPage, {BlogPage})
