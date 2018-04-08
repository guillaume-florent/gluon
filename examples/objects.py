# coding: utf-8

r"""objects used in the examples, to avoid duplication in each example"""

from atom.api import Atom, observe
from gluon.scalars import Float, FloatRange, Bool, Str, Value, Int
from gluon.typed import Typed
# import gluon.instance
from gluon.enum import Enum
# import gluon.ui.wx_


class Dummy(object):
    r"""The dummiest possible class"""
    pass


class DummyButAtomic(Atom):
    r"""A dummy class that inherits Atom and has a 3 members"""
    a = Float(default=11.)
    b = Float(default=22.)
    c = Float(default=33.)


class Example(Atom):
    r"""The Example class that is used to generated the UI

    It inherits Atom to create the members and for the built-in observer pattern

    """
    float_element = Float(default=-22.)
    float_range_element_1 = FloatRange(low=2., high=10., value=8.)
    float_range_element_2 = FloatRange(low=2., high=13., value=3.)

    bool_element = Bool(default=False)

    str_element = Str(default="hi there")

    value_element = Value(default=Dummy())

    # value_element_atomic = Value(default=DummyButAtomic())
    # value_element_atomic_2 = Value(default=DummyButAtomic())
    typed_element_atomic = Typed(DummyButAtomic,
                                 args=(),
                                 kwargs={"a": 1, "b": 2, "c": 3},
                                 read_only=["c"])
    typed_element_atomic_2 = Typed(DummyButAtomic,
                                   args=(),
                                   kwargs={"a": 4, "b": 5, "c": 6})

    _value_element_protected = Value(default=Dummy())

    # This should never happen a Member's intent is not to be private
    # __private = Value(name="private value", default=Dummy())

    int_element = Int(default=3)
    # c = Float(name="c is a free float", default=-22.)

    enum_element = Enum("a", "b", "c")

    var_normal = 44.
    _var_protected = 44.
    __var_private = 44.

    def __init__(self):
        pass
        # self.value_element_atomic = DummyButAtomic()
        # self.value_element_atomic_2 = DummyButAtomic()

    @observe("float_element", "float_range_element_1")
    def someone_changed_it(self, change):
        r"""Callback for some members modifications"""
        print("someone changed float_element or float_range_element_1")
        self.notify("update", change)
