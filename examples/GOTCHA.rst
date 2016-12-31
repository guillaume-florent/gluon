The wrong way
-------------

defining

value_element_atomic = gluon.scalars.Value(default=DummyButAtomic())
value_element_atomic_2 = gluon.scalars.Value(default=DummyButAtomic())

will cause the 2 attributes to live independently in the same Atom but to be synchronized with the same attributes
in other Atoms

i.e.
instance_1.value_element_atomic -> <objects.DummyButAtomic object at 0x036E4EE0>
instance_2.value_element_atomic -> <objects.DummyButAtomic object at 0x036E4EE0>
instance_1.value_element_atomic_2 -> <objects.DummyButAtomic object at 0x036E4F08>
instance_2.value_element_atomic_2 -> <objects.DummyButAtomic object at 0x036E4F08>

The right way
-------------

value_element_atomic = gluon.scalars.Value(default=None)
value_element_atomic_2 = gluon.scalars.Value(default=None)

def __init__(self):
    self.value_element_atomic = DummyButAtomic()
    self.value_element_atomic_2 = DummyButAtomic()