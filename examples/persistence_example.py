#!/usr/bin/python
# coding: utf-8

r"""Persistence example, using pickle"""

import pickle

import wx
import gluon.ui.wx_
from objects import Example

example_instance = Example()
example_instance.float_element = 9.
example_instance.float_range_element_1 = 7.5

print(pickle.dumps(example_instance))
with open("./test.pickle", "w") as f:
    pickle.dump(example_instance, f)

with open("./test.pickle") as f:
    obj = pickle.load(f)

app = wx.PySimpleApp()
frame = wx.Frame(None, -1, title="gluon ui example", size=(300, 400))
panel = gluon.ui.wx_.ObjectBackedPanel(frame, obj, display_protected=True, background_color=(200, 200, 200))
frame.Show()
app.SetTopWindow(frame)

app.MainLoop()
