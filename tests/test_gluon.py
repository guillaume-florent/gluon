#!/usr/bin/env python
# coding: utf-8

r"""
"""

from __future__ import absolute_import

from .objects import Example


def test_two_instances():

    a = Example()
    b = Example()

    assert a.float_element == b.float_element

    a.float_element = 10.

    assert a.float_element != b.float_element

    a.float_element = b.float_element

    assert a.float_element == b.float_element

    a.float_element = 10.

    assert a.float_element != b.float_element

