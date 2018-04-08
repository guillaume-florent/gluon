# coding: utf-8

r"""gluon's equivalent to Atom's Dict"""

import atom.dict
from gluon.base import Element


class Dict(Element, atom.dict.Dict):
    r"""Dict element"""
    def __init__(self, key=None, value=None, default=None):
        Element.__init__(self)
        atom.dict.Dict.__init__(self, key, value, default)
