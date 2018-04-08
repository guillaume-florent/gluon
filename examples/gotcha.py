#!/usr/bin/env python
# coding: utf-8

r"""Persistence example, using pickle"""

import pickle

import wx

from gluon.ui.wx_ import ObjectBackedPanel
from objects import Example

example_instance = Example()
example_instance_2 = Example()

example_instance.float_element = 9.
example_instance.float_range_element_1 = 7.5

print(str(example_instance.value_element_atomic))
print(str(example_instance_2.value_element_atomic))
print(str(example_instance.value_element_atomic_2))
print(str(example_instance_2.value_element_atomic_2))

# print("-"*20)
# print(gluon.persistence.atom_string(example_instance))
# print("-"*20)

print(pickle.dumps(example_instance))

with open("./test.pickle", "w") as f:
    pickle.dump(example_instance, f)

with open("./test.pickle") as f:
    obj = pickle.load(f)

app = wx.PySimpleApp()
frame = wx.Frame(None, -1, title="gluon ui example", size=(600, 400))

sizer = wx.BoxSizer(wx.HORIZONTAL)
panel = ObjectBackedPanel(frame,
                          example_instance,
                          display_protected=True,
                          background_color=(200, 200, 200))
panel_2 = ObjectBackedPanel(frame,
                            example_instance_2,
                            display_protected=True,
                            background_color=(200, 200, 200))
sizer.Add(panel)
sizer.Add(panel_2)
frame.SetSizer(sizer)
frame.Show()
app.SetTopWindow(frame)

app.MainLoop()
