# coding: utf-8

r"""Base element has the capacity to store a name and remember
the order in which it has been created"""


class Element(object):
    r"""Base class for all elements

    The creation order is attached to each element.
    This is used to enforce the same display order as the creation order.
    Useful elements(i.e. subclasses of Element) will also inherit their
    Atom alter ego

    """
    creation_order = 0

    def __init__(self):
        self.creation_order = Element.creation_order
        Element.creation_order += 1
