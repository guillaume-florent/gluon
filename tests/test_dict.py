#!/usr/bin/env python
# coding: utf-8

r"""Testing dict"""

import atom.api

from gluon.dict import Dict


def test_dict():
    r"""Test the dict"""
    class A(atom.api.Atom):
        d = Dict(default={'a': 1, 'b': 2})

    class B(atom.api.Atom):
        d = Dict(default={'c': 3, 'd': 4})

    a = A()
    b = B()

    assert a.d["a"] == 1
    assert b.d["c"] == 3
