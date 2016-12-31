#!/usr/bin/python
# coding: utf-8

r"""gluon's equivalent to Atom's Dict"""

import atom.dict
from gluon.base import Element


class Dict(Element, atom.dict.Dict):
    r"""Dict element"""
    def __init__(self, key=None, value=None, default=None):
        Element.__init__(self)
        atom.dict.Dict.__init__(self, key, value, default)


if __name__ == "__main__":
    import atom.api

    class A(atom.api.Atom):
        d = Dict(default={'a': 1, 'b': 2})

    class B(atom.api.Atom):
        d = Dict(default={'c': 3, 'd': 4})

    a = A()
    b = B()

    print(a.d["a"])
    print(b.d["c"])

