# coding: utf-8

r"""ui generation from an object"""

import wx
# import wx.lib.agw.floatspin
# import wx.lib.scrolledpanel
# import wx.lib.agw.foldpanelbar

from gluon.scalars import Value, Int, Str, Bool, Float, FloatRange
from gluon.enum import Enum
from gluon.tuple import Tuple
from gluon.instance import Instance
from gluon.typed import Typed
from gluon.list import List
from gluon.ui.name import label as label_func
from gluon.ui.wx_widgets import FloatWidget, IntWidget, BoolWidget, StrWidget, \
    ValueWidget, EnumWidget, InstanceWidget

from atom.api import Atom


# class ObjectBackedPanel(wx.ScrolledWindow):
class ObjectBackedPanel(wx.Panel):
    r"""Container for the generated widget(s)"""
    def __init__(self,
                 parent,
                 backing_object,
                 display_protected=False,
                 background_color=None,
                 label_width=-1,
                 read_only=None):
        wx.Panel.__init__(self, parent, -1)
        # wx.ScrolledWindow.__init__(self, parent, -1)

        if background_color is not None:
            self.SetBackgroundColour(background_color)

        if read_only is None:
            read_only = list()

        # sizer = wx.BoxSizer(wx.VERTICAL)

        # Filter out attributes that start with a _
        # (do not display in UI if protected)
        if display_protected is False:
            # manageable_attribute_names =
            #   [attribute_name for attribute_name in manageable_attribute_names
            # if not attribute_name.startswith("_")]
            manageable_attribute_names = [n for n in backing_object.members().keys() if not n.startswith("_")]
        else:
            # manageable_attribute_names =
            #   [attribute_name for attribute_name in manageable_attribute_names
            # if not attribute_name.startswith("__")]
            manageable_attribute_names = backing_object.members().keys()

        # Reorder based on creation_order of Parameter
        manageable_attribute_names = sorted(manageable_attribute_names,
                                            key=lambda attr_name: backing_object.__class__.
                                            __dict__["__atom_members__"][attr_name].creation_order)

        parameters = [backing_object.__getattribute__(attribute_name) for attribute_name in manageable_attribute_names]

        sizer = wx.FlexGridSizer(rows=len(parameters), cols=2, vgap=5, hgap=5)

        # print("Manageable attributes (ordered) :
        #                                 %s" % str(manageable_attribute_names))

        for attribute_name in manageable_attribute_names:
            attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
            # name_ = attribute_element.name_

            name_ = label_func(attribute_element.name)
            label = wx.StaticText(self,
                                  -1,
                                  name_,
                                  style=wx.ALIGN_RIGHT,
                                  size=(label_width, -1))
            # widget = None

            is_read_only = True if attribute_name.startswith("_") or attribute_name in read_only else False

            # if type(attribute_element) == FloatRange:
            if isinstance(attribute_element, FloatRange):
                widget = FloatWidget(self,
                                     -1,
                                     backing_object,
                                     attribute_name,
                                     read_only=is_read_only)
            # elif type(attribute_element) == Float:
            elif isinstance(attribute_element, Float):
                widget = FloatWidget(self,
                                     -1,
                                     backing_object,
                                     attribute_name,
                                     read_only=is_read_only)
            # elif type(attribute_element) == Int:
            elif isinstance(attribute_element, Int):
                widget = IntWidget(self,
                                   -1,
                                   backing_object,
                                   attribute_name,
                                   read_only=is_read_only)
            # elif type(attribute_element) == Bool:
            elif isinstance(attribute_element, Bool):
                widget = BoolWidget(self,
                                    -1,
                                    backing_object,
                                    attribute_name,
                                    read_only=is_read_only)
            # elif type(attribute_element) == Str:
            elif isinstance(attribute_element, Str):
                widget = StrWidget(self,
                                   -1,
                                   backing_object,
                                   attribute_name,
                                   read_only=is_read_only)
            # elif type(attribute_element) == Enum:
            elif isinstance(attribute_element, Enum):
                widget = EnumWidget(self,
                                    -1,
                                    backing_object,
                                    attribute_name,
                                    read_only=is_read_only)
            # elif type(attribute_element) == Tuple:
            elif isinstance(attribute_element, Tuple):
                widget = InstanceWidget(self,
                                        -1,
                                        backing_object,
                                        attribute_name,
                                        read_only=is_read_only)
            # elif type(attribute_element) == List:
            elif isinstance(attribute_element, List):
                widget = InstanceWidget(self,
                                        -1,
                                        backing_object,
                                        attribute_name,
                                        read_only=is_read_only)
            # elif type(attribute_element) == Typed or \
            #      type(attribute_element) == Instance or \
            #      type(attribute_element) == Value:
            elif isinstance(attribute_element, (Typed, Instance, Value,)):
                if isinstance(getattr(backing_object, attribute_name), Atom):
                    if hasattr(attribute_element, "read_only"):
                        ro = attribute_element.read_only
                    else:
                        ro = None
                    widget = ObjectBackedPanel(self,
                                               getattr(backing_object, attribute_name),
                                               display_protected=display_protected,
                                               background_color=background_color,
                                               label_width=label_width,
                                               read_only=ro)
                else:
                    # if type(attribute_element) == Typed or \
                    #    type(attribute_element) == Instance:
                    if isinstance(attribute_element, (Typed, Instance, )):
                        widget = InstanceWidget(self,
                                                -1,
                                                backing_object,
                                                attribute_name,
                                                read_only=is_read_only)
                    else:
                        widget = ValueWidget(self,
                                             -1,
                                             backing_object,
                                             attribute_name,
                                             read_only=is_read_only)

            else:
                print(type(attribute_element))
                raise ValueError("Unknown element type")

            # wx.TOP + border = 10 is a workaround
            # to realign the labels with the textctrl
            sizer.Add(label,
                      1,
                      wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
                      border=5)
            sizer.Add(widget, 1)

        self.SetSizer(sizer)
        # self.SetupScrolling()
        # self.SetScrollbars(20, 20, 50, 50)
        self.Refresh()
