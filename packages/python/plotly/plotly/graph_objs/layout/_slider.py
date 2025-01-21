from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Slider(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.slider"
    _valid_props = {
        "active",
        "activebgcolor",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "currentvalue",
        "font",
        "len",
        "lenmode",
        "minorticklen",
        "name",
        "pad",
        "stepdefaults",
        "steps",
        "templateitemname",
        "tickcolor",
        "ticklen",
        "tickwidth",
        "transition",
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
    def activebgcolor(self):
        return self["activebgcolor"]

    @activebgcolor.setter
    def activebgcolor(self, val):
        self["activebgcolor"] = val

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
    def currentvalue(self):
        return self["currentvalue"]

    @currentvalue.setter
    def currentvalue(self, val):
        self["currentvalue"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def len(self):
        return self["len"]

    @len.setter
    def len(self, val):
        self["len"] = val

    @property
    def lenmode(self):
        return self["lenmode"]

    @lenmode.setter
    def lenmode(self, val):
        self["lenmode"] = val

    @property
    def minorticklen(self):
        return self["minorticklen"]

    @minorticklen.setter
    def minorticklen(self, val):
        self["minorticklen"] = val

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
    def steps(self):
        return self["steps"]

    @steps.setter
    def steps(self, val):
        self["steps"] = val

    @property
    def stepdefaults(self):
        return self["stepdefaults"]

    @stepdefaults.setter
    def stepdefaults(self, val):
        self["stepdefaults"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def tickcolor(self):
        return self["tickcolor"]

    @tickcolor.setter
    def tickcolor(self, val):
        self["tickcolor"] = val

    @property
    def ticklen(self):
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    @property
    def tickwidth(self):
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    @property
    def transition(self):
        return self["transition"]

    @transition.setter
    def transition(self, val):
        self["transition"] = val

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
        activebgcolor=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        currentvalue=None,
        font=None,
        len=None,
        lenmode=None,
        minorticklen=None,
        name=None,
        pad=None,
        steps=None,
        stepdefaults=None,
        templateitemname=None,
        tickcolor=None,
        ticklen=None,
        tickwidth=None,
        transition=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs,
    ):
        super(Slider, self).__init__("sliders")

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
The first argument to the plotly.graph_objs.layout.Slider
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Slider`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("active", None)
        _v = active if active is not None else _v
        if _v is not None:
            self["active"] = _v
        _v = arg.pop("activebgcolor", None)
        _v = activebgcolor if activebgcolor is not None else _v
        if _v is not None:
            self["activebgcolor"] = _v
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
        _v = arg.pop("currentvalue", None)
        _v = currentvalue if currentvalue is not None else _v
        if _v is not None:
            self["currentvalue"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("len", None)
        _v = len if len is not None else _v
        if _v is not None:
            self["len"] = _v
        _v = arg.pop("lenmode", None)
        _v = lenmode if lenmode is not None else _v
        if _v is not None:
            self["lenmode"] = _v
        _v = arg.pop("minorticklen", None)
        _v = minorticklen if minorticklen is not None else _v
        if _v is not None:
            self["minorticklen"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("pad", None)
        _v = pad if pad is not None else _v
        if _v is not None:
            self["pad"] = _v
        _v = arg.pop("steps", None)
        _v = steps if steps is not None else _v
        if _v is not None:
            self["steps"] = _v
        _v = arg.pop("stepdefaults", None)
        _v = stepdefaults if stepdefaults is not None else _v
        if _v is not None:
            self["stepdefaults"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("tickcolor", None)
        _v = tickcolor if tickcolor is not None else _v
        if _v is not None:
            self["tickcolor"] = _v
        _v = arg.pop("ticklen", None)
        _v = ticklen if ticklen is not None else _v
        if _v is not None:
            self["ticklen"] = _v
        _v = arg.pop("tickwidth", None)
        _v = tickwidth if tickwidth is not None else _v
        if _v is not None:
            self["tickwidth"] = _v
        _v = arg.pop("transition", None)
        _v = transition if transition is not None else _v
        if _v is not None:
            self["transition"] = _v
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
