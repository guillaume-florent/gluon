gluon
=====

Python UI auto generation framework based on Atom

The UI is generated from the elements defined on an object.
An instance of the object is passed to the UI container constructor.
The generated UI has built-in bidirectional sync with its backing object

The order of creation of the elements is transferred to the generated UI container.

When available, the metadata (e.g. low and high of FloatRange) is used to define the corresponding widget.

Use
---

from atom.api import Atom, observe
from gluon.scalars import Float, FloatRange

same member names as with Atom but import gluon.scalars instead of atom.scalars

objects are still Atom(s). The observing framework is unmodified
