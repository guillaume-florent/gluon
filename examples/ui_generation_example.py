#!/usr/bin/env python
# coding: utf-8

r"""UI auto generation example using the gluon framework"""

from __future__ import absolute_import

import wx
from gluon.ui.wx_ import ObjectBackedPanel
from objects import Example

example_instance = Example()

app = wx.PySimpleApp()
frame = wx.Frame(None, -1, title="gluon ui example", size=(300, 500))
panel = ObjectBackedPanel(frame,
                          example_instance,
                          display_protected=True,
                          background_color=(200, 200, 200))
frame.Show()
app.SetTopWindow(frame)
example_instance.float_element = 9.
example_instance.float_range_element_1 = 7.5

app.MainLoop()
