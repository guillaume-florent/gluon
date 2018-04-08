#!/usr/bin/env python
# coding: utf-8

r"""Testing enum"""

from gluon.enum import Enum


def test_enum():
    r"""Test the enum"""
    e = Enum(1, 2, 3)
    e.set_index(1)
    assert e.index == 1
    assert e.items[e.index] == 2
    for i, item in enumerate(e.items):
        assert item == i + 1
