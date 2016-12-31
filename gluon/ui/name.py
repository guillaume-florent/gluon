#!/usr/bin/python
# coding: utf-8

r"""name.py"""


def label(attribute_name):
    r"""Convert an attribute/variable name to its ui displayable equivalent

    Capitalise the first letter
    Transform underscores to spaces

    Parameters
    ----------
    attribute_name : str
        The attribute/variable name

    """
    if attribute_name.startswith('_'):
        return attribute_name

    chunks = attribute_name.split("_")
    if chunks[0] is not None:
        chunks[0] = chunks[0].title()
    return " ".join(chunks)
