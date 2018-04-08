# coding: utf-8

r"""gluon's equivalent to Atom's Instance"""

import atom.typed
from gluon.base import Element


class Typed(Element, atom.typed.Typed):
    r"""Typed element"""
    def __init__(self, kind, args=None, kwargs=None, factory=None, read_only=None):
        Element.__init__(self)
        atom.typed.Typed.__init__(self, kind, args, kwargs, factory)
        # if kwargs is not None:
        #     try:
        #         self.read_only = kwargs["read_only"]
        #     except KeyError:
        #         self.read_only = []
        self.read_only = read_only
