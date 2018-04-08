# coding: utf-8

r"""gluon's equivalent to Atom's tuple"""


import atom.tuple
from gluon.base import Element


class Tuple(Element, atom.tuple.Tuple):
    r"""Tuple element"""
    def __init__(self, item=None, default=()):
        Element.__init__(self)
        atom.tuple.Tuple.__init__(self, item, default)

