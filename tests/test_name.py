#!/usr/bin/env python
# coding: utf-8

r"""name.py module tests"""

import gluon.ui.name


def test_label():
    r"""Test the conversion from variable name to presentable name/label"""
    name = gluon.ui.name.label("this_is_nice")
    assert name == "This is nice"

    name = gluon.ui.name.label("item_#1")
    assert name == "Item #1"

    # The following cases are very unlikely
    # (python variable naming restrictions)
    name = gluon.ui.name.label("101test")
    assert name == "101Test"

    name = gluon.ui.name.label("101_test")
    assert name == "101 test"
