#!/usr/bin/python
# coding: utf-8

r"""gluon's equivalent to Atom's list"""


import atom.list
from gluon.base import Element


class List(Element, atom.list.List):
    r"""List element"""
    def __init__(self, item=None, default=None):
        Element.__init__(self)
        atom.list.List.__init__(self, item, default)


if __name__ == "__main__":
    import atom.api

    class A(atom.api.Atom):
        l = List(default=[1, 2, 3])

    class B(atom.api.Atom):
        l = List(default=[4, 5, 6])

    a = A()
    b = B()

    print(a.l)
    print(b.l)
