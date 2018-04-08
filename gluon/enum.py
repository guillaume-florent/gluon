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
