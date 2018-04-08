# coding: utf-8

r"""gluon's equivalent to Atom's list"""


import atom.list
from gluon.base import Element


class List(Element, atom.list.List):
    r"""List element"""
    def __init__(self, item=None, default=None):
        Element.__init__(self)
        atom.list.List.__init__(self, item, default)
