#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-08-22
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django import template
register = template.Library()


@register.filter
def sort_by(queryset, order):
    """Sort every queryset by order, defined in templates"""
    return queryset.order_by(order)