# coding: utf-8

r"""wx widgets that can be added to an auto generated container/panel"""

import wx
from wx.lib.agw.floatspin import FloatSpin, FS_RIGHT, EVT_FLOATSPIN
# import wx.lib.scrolledpanel
# import wx.lib.agw.foldpanelbar

from gluon.scalars import Str, Bool, Int, Float, FloatRange
from gluon.enum import Enum

from atom.api import Atom


class EnumWidget(wx.ComboBox):
    r"""Generic widget for an enum

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : an Atom object
    attribute_name : str
    read_only : bool

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        self.attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(self.attribute_element, Enum)
        if not isinstance(self.attribute_element, Enum):
            raise AssertionError("attribute_element should be an Enum")
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        wx.ComboBox.__init__(self,
                             parent,
                             id_,
                             choices=self.attribute_element.items,
                             style=wx.CB_READONLY)

        self.SetValue(getattr(backing_object, attribute_name))

        self.Bind(wx.EVT_COMBOBOX, self.on_evt_combobox, self)

        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)

        if read_only is True:
            self.Enable(False)

    def on_evt_combobox(self, event):
        r"""The choice was changed

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            print(event.GetEventObject().GetValue())
            setattr(self.backing_object,
                    self.attribute_name,
                    event.GetEventObject().GetValue())
            print(getattr(self.backing_object, self.attribute_name))

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("EnumWidget : backed_object_attr_value_changed")
        print("EnumWidget : backed_object_attr_value_change : %s" % str(change))
        print("EnumWidget : %s" % str(self))

        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            # self.SetValue(change["value"])
            self.SetValue(getattr(change["object"], change["name"]))
        print(getattr(change["object"], change["name"]))


class InstanceWidget(wx.TextCtrl):
    r"""Generic widget for anything

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : an Atom object
    attribute_name : str
    read_only : bool

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        # attribute_element = \
        #  backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(attribute_element, Value)
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        wx.TextCtrl.__init__(self, parent, id_, size=(500, -1))

        self.SetValue(str(getattr(backing_object, attribute_name)))

        # self.Bind(wx.EVT_TEXT, self.on_evt_text, self)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)

        if read_only is True:
            self.Enable(False)

    # def on_evt_text(self, event):
    #     r"""The text was changed
    #
    #     Parameters
    #     ----------
    #     event : wx event
    #
    #     """
    #     # PyDeadObject error avoidance
    #     # (python is a proxy to C++ that should not be called if not there)
    #     if self:
    #         setattr(self.backing_object,
    #                 self.attribute_name,
    #                 event.GetEventObject().GetValue())
    #         print(getattr(self.backing_object, self.attribute_name))

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("InstanceWidget : backed_object_attr_value_changed")
        print("InstanceWidget : backed_object_attr_value_change : %s" % str(change))
        print("InstanceWidget : %s" % str(self))
        # assert isinstance(change["value"], object)
        # if not isinstance(change["value"], object):
        #     raise AssertionError('change["value"] should be an object')
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            self.SetValue(str(change["value"]))
            # self.SetValue(str(getattr(change["object"], change["name"])))
        print(getattr(change["object"], change["name"]))


class ValueWidget(wx.TextCtrl):
    r"""Generic widget for anything

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : an Atom object
    attribute_name : str
    read_only : bool

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        # attribute_element = \
        #  backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(attribute_element, Value)
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        wx.TextCtrl.__init__(self, parent, id_, size=(500, -1))

        self.SetValue(str(getattr(backing_object, attribute_name)))

        self.Bind(wx.EVT_TEXT, self.on_evt_text, self)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)

        if read_only is True:
            self.Enable(False)

    def on_evt_text(self, event):
        r"""The text was changed

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            setattr(self.backing_object,
                    self.attribute_name,
                    event.GetEventObject().GetValue())
            print(getattr(self.backing_object, self.attribute_name))

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("ValueWidget : backed_object_attr_value_changed")
        print("ValueWidget : backed_object_attr_value_change : %s" %
              str(change))
        print("ValueWidget : %s" % str(self))
        # assert isinstance(change["value"], object)
        # if not isinstance(change["value"], object):
        #     raise AssertionError('change["value"] should be an object')
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            self.SetValue(str(change["value"]))
            # self.SetValue(str(getattr(change["object"], change["name"])))
        print(getattr(change["object"], change["name"]))


class StrWidget(wx.TextCtrl):
    r"""String widget

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : an Atom object
    attribute_name : str
    read_only : bool

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(attribute_element, Str)
        if not isinstance(attribute_element, Str):
            raise AssertionError("attribute_element should be an Str")
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        wx.TextCtrl.__init__(self, parent, -1)

        self.SetValue(getattr(backing_object, attribute_name))

        self.Bind(wx.EVT_TEXT, self.on_evt_text, self)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)

        if read_only is True:
            self.Enable(False)

    def on_evt_text(self, event):
        r"""The text changed

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            setattr(self.backing_object,
                    self.attribute_name,
                    event.GetEventObject().GetValue())
            print(getattr(self.backing_object, self.attribute_name))

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("StrWidget : backed_object_attr_value_changed")
        print("StrWidget : backed_object_attr_value_change : %s" % str(change))
        print("StrWidget : %s" % str(self))
        # assert isinstance(change["value"], str)
        if not isinstance(change["value"], str):
            raise AssertionError('change["value"] should be an str')
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            # self.SetValue(change["value"])
            self.SetValue(getattr(change["object"], change["name"]))
        print(getattr(change["object"], change["name"]))


class BoolWidget(wx.CheckBox):
    r"""Bool widget

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : an Atom object
    attribute_name : str
    read_only : bool

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(attribute_element, Bool)
        if not isinstance(attribute_element, Bool):
            raise AssertionError("attribute_element should be a Bool")
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        wx.CheckBox.__init__(self, parent, id_)

        if getattr(backing_object, attribute_name) is True:
            self.SetValue(True)
        elif getattr(backing_object, attribute_name) is False:
            self.SetValue(False)
        else:
            raise ValueError

        self.Bind(wx.EVT_CHECKBOX, self.on_evt_checkbox, self)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)

        if read_only is True:
            self.Enable(False)

    def on_evt_checkbox(self, event):
        r"""The checkbox was checked or unchecked

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            setattr(self.backing_object,
                    self.attribute_name,
                    event.GetEventObject().GetValue())
            print(getattr(self.backing_object, self.attribute_name))

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("BoolWidget : backed_object_attr_value_changed")
        print("BoolWidget : backed_object_attr_value_change : %s" % str(change))
        print("BoolWidget : %s" % str(self))
        # assert type(change["value"]) is bool

        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            # self.SetValue(change["value"])
            self.SetValue(getattr(change["object"], change["name"]))
        print(getattr(change["object"], change["name"]))


class IntWidget(FloatSpin):
    r"""Int widget

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : subclass of atom.api.Atom
        the atom object being dealt with
    attribute_name : the name of the managed variable in the backing
        object definition.
        if backing object is defined as
        class BackingObject(Atom): var_1 = FloatRange(),
        the attribute name is var_1
    read_only : bool

    Widget how to
    -------------
    see the FloatWidget how to

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        # assert isinstance(backing_object, Atom)
        if not isinstance(backing_object, Atom):
            raise AssertionError("backing_object should be an Atom")
        attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert isinstance(attribute_element, Int)
        if not isinstance(attribute_element, Int):
            raise AssertionError("attribute_element should be an Int")
        self.backing_object = backing_object
        self.attribute_name = attribute_name

        FloatSpin.__init__(self,
                           parent,
                           id_,
                           increment=1,
                           value=getattr(backing_object, attribute_name),
                           agwStyle=FS_RIGHT)

        self.SetDigits(0)
        # self.Bind(wx.EVT_TEXT, self.on_evt_floatspin, self)
        self.Bind(EVT_FLOATSPIN,
                  self.on_evt_floatspin, self)
        self._textctrl.Bind(wx.EVT_TEXT, self.on_evt_text, self._textctrl)

        if read_only is True:
            self.Enable(False)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)
        # backing_object.observe("update",
        #                        self.backed_object_attr_value_changed)

        self.sent = False
        self.last_value_sent = None

    def on_evt_floatspin(self, event):
        r"""Handler for the manipulation of the arrows

        Parameters
        ----------
        event : wx event

        """
        print("on_evt_floatspin called")
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            val = int(event.GetEventObject().GetValue())
            print("Sending Val " + str(val))
            setattr(self.backing_object, self.attribute_name, val)
            self.Refresh()
            self.last_value_sent = val
            print(getattr(self.backing_object, self.attribute_name))

    def on_evt_text(self, event):
        r"""Handler of EVT_TEXT in the text ctrl of the FloatSpin

        Parameters
        ----------
        event : wx event

        """
        print("on_evt_text called")
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            if self.sent is False:
                try:
                    f = int(event.GetEventObject().GetValue())
                    if f != self.last_value_sent:
                        # self._textctrl.SetBackgroundColour("orange")
                        pass
                    else:
                        self._textctrl.SetBackgroundColour(wx.NullColour)
                    self.Refresh()

                except ValueError:
                    # self._textctrl.SetBackgroundColour("red")
                    self.Refresh()
            else:
                self._textctrl.SetBackgroundColour(wx.NullColour)
                self.Refresh()
                self.sent = False

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        # assert type(caller._value) is float
        print("IntWidget : backed_object_attr_value_changed")
        print("IntWidget : backed_object_attr_value_change : %s" % str(change))
        print("IntWidget : %s" % str(self))
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            # self.SetValue(change["value"])
            self.SetValue(getattr(change["object"], change["name"]))
        print(getattr(change["object"], change["name"]))


class FloatWidget(FloatSpin):
    r"""Float widget

    Parameters
    ----------
    parent : wx panel
    id_ : int
    backing_object : subclass of atom.api.Atom
        the atom object being dealt with
    attribute_name : the name of the managed variable in the backing
        object definition
        if backing object is defined as 
        class BackingObject(Atom): var_1 = FloatRange(),
        the attribute name is var_1
    read_only : bool

    Widget how to
    -------------
    `FloatSpin` catches 3 different types of events:
    1) Spin events: events generated by spinning up/down the spinbutton;
    2) Char events: playing with up/down arrows of the keyboard 
    increase/decrease the value of :class:`FloatSpin`;
    3) Mouse wheel event:
    using the wheel will change the value of :class:`FloatSpin`.
    In addition, there are some other functionalities:
    - It remembers the initial value as a default value,
    call meth:~FloatSpin.SetToDefaultValue`, or
    press ``Esc`` to return to it;
    - ``Shift`` + arrow = 2 * increment (or ``Shift`` + mouse wheel);
    - ``Ctrl`` + arrow = 10 * increment (or ``Ctrl`` + mouse wheel);
    - ``Alt`` + arrow = 100 * increment (or ``Alt`` + mouse wheel);
    - Combinations of ``Shift``, ``Ctrl``, ``Alt``
    increment the :class:`FloatSpin` value by the product of the factors;
    - ``PgUp`` & ``PgDn`` = 10 * increment * the product of the
    ``Shift``, ``Ctrl``, ``Alt`` factors;
    - ``Space`` sets the control's value to it's last valid state.

    """
    def __init__(self,
                 parent,
                 id_,
                 backing_object=None,
                 attribute_name=None,
                 read_only=False):
        # assert isinstance(backing_object, Atom)
        if not isinstance(backing_object, Atom):
            raise AssertionError("backing object should be an Atom")
        attribute_element = backing_object.__class__.__dict__["__atom_members__"][attribute_name]
        # assert (isinstance(attribute_element, FloatRange) or
        #         isinstance(attribute_element, Float))
        if not isinstance(attribute_element, (FloatRange, Float,)):
            raise AssertionError("attribute_element should be a "
                                 "Float or a FloatRange")
        self.backing_object = backing_object
        self.attribute_name = attribute_name
        # Increment is dynamically handled in the control,
        # 0.01 is only a starting value
        if hasattr(attribute_element, "low"):
            minimum = attribute_element.low
        else:
            minimum = None
        if hasattr(attribute_element, "high"):
            maximum = attribute_element.high
        else:
            maximum = None
        FloatSpin.__init__(self,
                           parent,
                           id_,
                           min_val=minimum,
                           max_val=maximum,
                           increment=self.get_increment(self.get_digits(getattr(backing_object, attribute_name))),
                           value=getattr(backing_object, attribute_name),
                           agwStyle=FS_RIGHT)
        # self.SetFormat("%f")
        self.SetDigits(self.get_digits(getattr(backing_object, attribute_name)))
        # self.Bind(wx.EVT_TEXT, self.on_evt_floatspin, self)
        self.Bind(EVT_FLOATSPIN, self.on_evt_floatspin, self)
        self._textctrl.Bind(wx.EVT_TEXT, self.on_evt_text, self._textctrl)

        if read_only is True:
            self.Enable(False)

        # attribute_element.add_static_observer(self.backed_object_attr_value_changed)
        backing_object.observe(attribute_name,
                               self.backed_object_attr_value_changed)
        # backing_object.observe("update",
        #                        self.backed_object_attr_value_changed)

        self.sent = False
        self.last_value_sent = None

    #     # Not necessary, just to show the mechanism
    #     self.backing_object.set_notifications_enabled(False)
    #     self.backing_object.observe("update", self.toto)
    #     self.backing_object.set_notifications_enabled(True)
    #     self.backing_object.observe("update", self.toto)
    #
    # #
    # # # Not necessary, just to show the mechanism
    # def toto(self, change):
    #     print("also got a notification from the backing object")

    @staticmethod
    def get_digits(number):
        r"""Number of displayed digits of number

        Parameters
        ----------
        number : float"""
        return max(1, len(str(number).split(".")[1]))

    @staticmethod
    def get_increment(digits):
        r"""Increment corresponding to a given number of digits

        Parameters
        ----------
        digits : int

        """
        return 1. / (10**digits)

    def on_evt_floatspin(self, event):
        r"""Handler for the manipulation of the arrows

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            self.sent = False
            if -1e-10 < event.GetEventObject().GetValue() < 1e-10:
                val = 0.
            else:
                val = event.GetEventObject().GetValue()
            digits = self.get_digits(val)

            self.SetDigits(digits)
            self.SetIncrement(self.get_increment(digits))
            # if digits != 0:
            print("Sending Val " + str(val))
            setattr(self.backing_object, self.attribute_name, val)
            self.Refresh()
            print(getattr(self.backing_object, self.attribute_name))

    def on_evt_text(self, event):
        r"""Handler of EVT_TEXT in the text ctrl of the FloatSpin

        Parameters
        ----------
        event : wx event

        """
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            if self.sent is False:
                try:
                    f = float(event.GetEventObject().GetValue())
                    if f != self.last_value_sent:
                        # self._textctrl.SetBackgroundColour("orange")
                        pass
                    else:
                        self._textctrl.SetBackgroundColour(wx.NullColour)
                    self.Refresh()

                except ValueError:
                    # self._textctrl.SetBackgroundColour("red")
                    self.Refresh()
            else:
                self._textctrl.SetBackgroundColour(wx.NullColour)
                self.Refresh()
                self.sent = False

    def backed_object_attr_value_changed(self, change):
        r"""Observer method implementation

        Parameters
        ----------
        change : dict

        """
        print("FloatWidget : backed_object_attr_value_changed")
        print("FloatWidget : backed_object_attr_value_change : %s" %
              str(change))
        # PyDeadObject error avoidance
        # (python is a proxy to C++ that should not be called if not there)
        if self:
            # self.SetValue(change["value"])
            self.SetValue(getattr(change["object"], change["name"]))
        print(getattr(change["object"], change["name"]))

        # print("FloatWidget : backed_object_attr_value_changed")
        # print("FloatWidget : backed_object_attr_value_change : %s" %
        #       str(change))
        # # PyDeadObject error avoidance
        # # (python is a proxy to C++ that should not be called if not there)
        # if self:
        #     try:
        #         if change["name"] == self.attribute_name:
        #             self.SetValue(change["value"])
        #     except KeyError:
        #         print("FloatWidget says : It was not for me")
