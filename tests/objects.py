#!/usr/bin/python
# coding: utf-8

r"""objects used in the examples, to avoid duplication in each example"""

import atom.api
import gluon.scalars
import gluon.ui.wx_


class Dummy(object):
    r"""The dummiest possible class"""
    pass


class DummyButAtomic(atom.api.Atom):
    r"""A dummy class that inherits Atom and has a 3 members"""
    a = gluon.scalars.Float(default=11.)
    b = gluon.scalars.Float(default=22.)
    c = gluon.scalars.Float(default=33.)


class Example(atom.api.Atom):
    r"""The Example class that is used to generated the UI

    It inherits Atom to create the members and for the built-in observer pattern

    """
    float_element = gluon.scalars.Float(default=-22.)
    float_range_element_1 = gluon.scalars.FloatRange(low=2., high=10., value=8.)
    float_range_element_2 = gluon.scalars.FloatRange(low=2., high=13., value=3.)

    bool_element = gluon.scalars.Bool(default=False)

    str_element = gluon.scalars.Str(default="hi there")

    value_element = gluon.scalars.Value(default=Dummy())

    value_element_atomic = gluon.scalars.Value(default=DummyButAtomic())

    _value_element_protected = gluon.scalars.Value(default=Dummy())

    # This should never happen a Member's intent is not to be private
    # __private = gluon.scalars.Value(name="private value", default=Dummy())

    int_element = gluon.scalars.Int(default=3)
    # c = gluon.scalars.Float(name="c is a free float", default=-22.)

    var_normal = 44.
    _var_protected = 44.
    __var_private = 44.

    @atom.api.observe("float_element", "float_range_element_1")
    def someone_changed_it(self, change):
        r"""Callback for some members modifications"""
        print("someone changed float_element or float_range_element_1")
        self.notify("update", change)
