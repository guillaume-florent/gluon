gluon
=====

.. image:: https://api.codacy.com/project/badge/Grade/7c3f965fed4742dbb9dc80b7cc55b7a9
    :target: https://www.codacy.com/app/guillaume-florent/gluon?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guillaume-florent/gluon&amp;utm_campaign=Badge_Grade


Python UI auto generation framework based on `atom <https://github.com/nucleic/atom>`_

The UI is generated from the elements defined on an object.
An instance of the object is passed to the UI container constructor.
The generated UI has built-in bidirectional sync with its backing object

The order of creation of the elements is transferred to the generated UI container.

When available, the metadata (e.g. low and high of FloatRange) is used to define the corresponding widget.

Use
---

.. code-block:: python

   from atom.api import Atom, observe
   from gluon.scalars import Float, FloatRange

same member names as with Atom but import gluon.scalars instead of atom.scalars

objects are still Atom(s). The observing framework is unmodified
