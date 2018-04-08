# coding: utf-8

r"""gluon's equivalent to Atom's Instance"""

import atom.instance
from gluon.base import Element


class Instance(Element, atom.instance.Instance):
    r"""Dict element"""
    def __init__(self, kind, args=None, kwargs=None, factory=None):
        Element.__init__(self)
        atom.instance.Instance.__init__(self, kind, args, kwargs, factory)
