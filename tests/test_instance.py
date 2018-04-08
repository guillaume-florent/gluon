#!/usr/bin/env python
# coding: utf-8

r"""Testing instance"""

import pytest

import atom.api
from gluon.instance import Instance


def test_instance():
    r"""Test the instance"""

    class DummyParent(object):
        pass

    class Dummy(DummyParent):
        pass

    class A(atom.api.Atom):
        ins = Instance(kind=DummyParent, args=())

    class B(atom.api.Atom):
        ins = Instance(kind=Dummy)

    a = A()
    assert isinstance(a.ins, DummyParent)
    assert not isinstance(a.ins, Dummy)
    # print(a.ins)
    a.ins = Dummy()
    assert isinstance(a.ins, DummyParent)
    assert isinstance(a.ins, Dummy)
    # print(a.ins)
    b = B()
    # print(b.ins)
    assert b.ins is None
    with pytest.raises(TypeError):
        b.ins = DummyParent()  # -> raise TypeError exception
