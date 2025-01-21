from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Updatemenu(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.updatemenu"
    _valid_props = {
        "active",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "buttondefaults",
        "buttons",
        "direction",
        "font",
        "name",
        "pad",
        "showactive",
        "templateitemname",
        "type",
        "visible",
        "x",
        "xanchor",
        "y",
        "yanchor",
    }

    @property
    def active(self):
        return self["active"]

    @active.setter
    def active(self, val):
        self["active"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def borderwidth(self):
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    @property
    def buttons(self):
        return self["buttons"]

    @buttons.setter
    def buttons(self, val):
        self["buttons"] = val

    @property
    def buttondefaults(self):
        return self["buttondefaults"]

    @buttondefaults.setter
    def buttondefaults(self, val):
        self["buttondefaults"] = val

    @property
    def direction(self):
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def pad(self):
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    @property
    def showactive(self):
        return self["showactive"]

    @showactive.setter
    def showactive(self, val):
        self["showactive"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def x(self):
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def xanchor(self):
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    @property
    def y(self):
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def yanchor(self):
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        active=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        buttons=None,
        buttondefaults=None,
        direction=None,
        font=None,
        name=None,
        pad=None,
        showactive=None,
        templateitemname=None,
        type=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs,
    ):
        super(Updatemenu, self).__init__("updatemenus")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Updatemenu
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Updatemenu`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("active", None)
        _v = active if active is not None else _v
        if _v is not None:
            self["active"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("borderwidth", None)
        _v = borderwidth if borderwidth is not None else _v
        if _v is not None:
            self["borderwidth"] = _v
        _v = arg.pop("buttons", None)
        _v = buttons if buttons is not None else _v
        if _v is not None:
            self["buttons"] = _v
        _v = arg.pop("buttondefaults", None)
        _v = buttondefaults if buttondefaults is not None else _v
        if _v is not None:
            self["buttondefaults"] = _v
        _v = arg.pop("direction", None)
        _v = direction if direction is not None else _v
        if _v is not None:
            self["direction"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("pad", None)
        _v = pad if pad is not None else _v
        if _v is not None:
            self["pad"] = _v
        _v = arg.pop("showactive", None)
        _v = showactive if showactive is not None else _v
        if _v is not None:
            self["showactive"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xanchor", None)
        _v = xanchor if xanchor is not None else _v
        if _v is not None:
            self["xanchor"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("yanchor", None)
        _v = yanchor if yanchor is not None else _v
        if _v is not None:
            self["yanchor"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
