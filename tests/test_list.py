#!/usr/bin/env python
# coding: utf-8

r"""Testing list"""

import atom.api
from gluon.list import List


def test_list():
    r"""Test the list"""

    class A(atom.api.Atom):
        l = List(default=[1, 2, 3])

    class B(atom.api.Atom):
        l = List(default=[4, 5, 6])

    a = A()
    b = B()

    assert a.l == [1, 2, 3]
    assert b.l == [4, 5, 6]