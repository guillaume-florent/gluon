#!/usr/bin/python
# coding: utf-8

r"""Elements are Atom Members with the capacity to store metadata
when relevant and to remember their creation order

"""

import atom.scalars
from gluon.base import Element


class Value(Element, atom.scalars.Value):
    r"""Value element"""
    def __init__(self, default=None, factory=None):
        Element.__init__(self)
        atom.scalars.Value.__init__(self, default, factory)


class Bool(Element, atom.scalars.Bool):
    r"""Bool element"""
    def __init__(self, default=False, factory=None):
        Element.__init__(self)
        atom.scalars.Bool.__init__(self, default, factory)


class Int(Element, atom.scalars.Int):
    r"""Int electron"""
    def __init__(self, default=0, factory=None, strict=True):
        Element.__init__(self)
        atom.scalars.Int.__init__(self, default, factory, strict)


class FloatRange(Element, atom.scalars.FloatRange):
    r"""FloatRange element"""
    def __init__(self, low=None, high=None, value=None):
        self.low = low
        self.high = high
        Element.__init__(self)
        atom.scalars.FloatRange.__init__(self, low, high, value)


class Range(Element, atom.scalars.Range):
    r"""Range element"""
    def __init__(self, low=None, high=None, value=None):
        self.low = low
        self.high = high
        Element.__init__(self)
        atom.scalars.Range.__init__(self, low, high, value)


class Float(Element, atom.scalars.Float):
    r"""Float element"""
    def __init__(self, default=0.0, factory=None, strict=False):
        Element.__init__(self)
        atom.scalars.Float.__init__(self, default, factory, strict)


class Str(Element, atom.scalars.Str):
    r"""Str element"""
    def __init__(self, default='', factory=None, strict=False):
        Element.__init__(self)
        atom.scalars.Str.__init__(self, default, factory, strict)


class Unicode(Element, atom.scalars.Unicode):
    r"""Unicode element"""
    def __init__(self, default=u'', factory=None, strict=False):
        Element.__init__(self)
        atom.scalars.Unicode.__init__(self, default, factory, strict)
