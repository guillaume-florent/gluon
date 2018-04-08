#!/usr/bin/env python
# coding: utf-8

r"""Testing typed"""

import atom.api
from gluon.typed import Typed


def test_typed():
    r"""Test typed"""

    class DummyParent(object):
        pass

    class Dummy(DummyParent):
        pass

    class A(atom.api.Atom):
        ins = Typed(kind=DummyParent, args=())

    a = A()
    assert isinstance(a.ins, DummyParent)
    assert not isinstance(a.ins, Dummy)
    # print(a.ins)
    a.ins = Dummy()
    assert isinstance(a.ins, DummyParent)
    assert isinstance(a.ins, Dummy)
    # print(a.ins)
