#!/usr/bin/python
# coding: utf-8

r"""gluon's equivalent to Atom's enum"""

import atom.enum
from gluon.base import Element


class Enum(Element, atom.enum.Enum):
    r"""Enum element"""
    def __init__(self, *items):
        Element.__init__(self)
        atom.enum.Enum.__init__(self, *items)


if __name__ == "__main__":
    # ae = atom.enum.Enum(1, 2, 3)

    e = Enum(1, 2, 3)
    e.set_index(1)
    print(e.index)
    print(e.items[e.index])
    for item in e.items:
        print(item)
