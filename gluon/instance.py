#!/usr/bin/python
# coding: utf-8

r"""gluon's equivalent to Atom's Instance"""

import atom.instance
from gluon.base import Element


class Instance(Element, atom.instance.Instance):
    r"""Dict element"""
    def __init__(self, kind, args=None, kwargs=None, factory=None):
        Element.__init__(self)
        atom.instance.Instance.__init__(self, kind, args, kwargs, factory)

if __name__ == "__main__":
    import atom.api

    class DummyParent(object):
        pass

    class Dummy(DummyParent):
        pass

    class A(atom.api.Atom):
        ins = Instance(kind=DummyParent, args=())

    class B(atom.api.Atom):
        ins = Instance(kind=Dummy)


    a = A()
    print(a.ins)
    a.ins = Dummy()
    print(a.ins)
    b = B()
    print(b.ins)
    b.ins = DummyParent()  # -> raise TypeError exception
