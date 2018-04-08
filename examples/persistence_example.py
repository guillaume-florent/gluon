#!/usr/bin/env python
# coding: utf-8

r"""Persistence example, using pickle"""

import pickle

import wx
from gluon.ui.wx_ import ObjectBackedPanel
from objects import Example

example_instance = Example()
example_instance.float_element = 9.
example_instance.float_range_element_1 = 7.5

print(pickle.dumps(example_instance))

with open("./test.pickle", "wb") as f:
    pickle.dump(example_instance, f)

with open("./test.pickle", "rb") as f:
    obj = pickle.load(f)

app = wx.App()
frame = wx.Frame(None, -1, title="gluon ui example", size=(300, 400))
panel = ObjectBackedPanel(frame,
                          obj,
                          display_protected=True,
                          background_color=(200, 200, 200))
frame.Show()
app.SetTopWindow(frame)

app.MainLoop()
