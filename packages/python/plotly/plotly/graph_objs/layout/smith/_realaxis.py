from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Realaxis(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.smith"
    _path_str = "layout.smith.realaxis"
    _valid_props = {
        "color",
        "gridcolor",
        "griddash",
        "gridwidth",
        "hoverformat",
        "labelalias",
        "layer",
        "linecolor",
        "linewidth",
        "showgrid",
        "showline",
        "showticklabels",
        "showtickprefix",
        "showticksuffix",
        "side",
        "tickangle",
        "tickcolor",
        "tickfont",
        "tickformat",
        "ticklen",
        "tickprefix",
        "ticks",
        "ticksuffix",
        "tickvals",
        "tickvalssrc",
        "tickwidth",
        "visible",
    }

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def gridcolor(self):
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    @property
    def griddash(self):
        return self["griddash"]

    @griddash.setter
    def griddash(self, val):
        self["griddash"] = val

    @property
    def gridwidth(self):
        return self["gridwidth"]

    @gridwidth.setter
    def gridwidth(self, val):
        self["gridwidth"] = val

    @property
    def hoverformat(self):
        return self["hoverformat"]

    @hoverformat.setter
    def hoverformat(self, val):
        self["hoverformat"] = val

    @property
    def labelalias(self):
        return self["labelalias"]

    @labelalias.setter
    def labelalias(self, val):
        self["labelalias"] = val

    @property
    def layer(self):
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    @property
    def linecolor(self):
        return self["linecolor"]

    @linecolor.setter
    def linecolor(self, val):
        self["linecolor"] = val

    @property
    def linewidth(self):
        return self["linewidth"]

    @linewidth.setter
    def linewidth(self, val):
        self["linewidth"] = val

    @property
    def showgrid(self):
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val):
        self["showgrid"] = val

    @property
    def showline(self):
        return self["showline"]

    @showline.setter
    def showline(self, val):
        self["showline"] = val

    @property
    def showticklabels(self):
        return self["showticklabels"]

    @showticklabels.setter
    def showticklabels(self, val):
        self["showticklabels"] = val

    @property
    def showtickprefix(self):
        return self["showtickprefix"]

    @showtickprefix.setter
    def showtickprefix(self, val):
        self["showtickprefix"] = val

    @property
    def showticksuffix(self):
        return self["showticksuffix"]

    @showticksuffix.setter
    def showticksuffix(self, val):
        self["showticksuffix"] = val

    @property
    def side(self):
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    @property
    def tickangle(self):
        return self["tickangle"]

    @tickangle.setter
    def tickangle(self, val):
        self["tickangle"] = val

    @property
    def tickcolor(self):
        return self["tickcolor"]

    @tickcolor.setter
    def tickcolor(self, val):
        self["tickcolor"] = val

    @property
    def tickfont(self):
        return self["tickfont"]

    @tickfont.setter
    def tickfont(self, val):
        self["tickfont"] = val

    @property
    def tickformat(self):
        return self["tickformat"]

    @tickformat.setter
    def tickformat(self, val):
        self["tickformat"] = val

    @property
    def ticklen(self):
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    @property
    def tickprefix(self):
        return self["tickprefix"]

    @tickprefix.setter
    def tickprefix(self, val):
        self["tickprefix"] = val

    @property
    def ticks(self):
        return self["ticks"]

    @ticks.setter
    def ticks(self, val):
        self["ticks"] = val

    @property
    def ticksuffix(self):
        return self["ticksuffix"]

    @ticksuffix.setter
    def ticksuffix(self, val):
        self["ticksuffix"] = val

    @property
    def tickvals(self):
        return self["tickvals"]

    @tickvals.setter
    def tickvals(self, val):
        self["tickvals"] = val

    @property
    def tickvalssrc(self):
        return self["tickvalssrc"]

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self["tickvalssrc"] = val

    @property
    def tickwidth(self):
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        color=None,
        gridcolor=None,
        griddash=None,
        gridwidth=None,
        hoverformat=None,
        labelalias=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        side=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        ticklen=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        visible=None,
        **kwargs,
    ):
        super(Realaxis, self).__init__("realaxis")

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
The first argument to the plotly.graph_objs.layout.smith.Realaxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.smith.Realaxis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("gridcolor", None)
        _v = gridcolor if gridcolor is not None else _v
        if _v is not None:
            self["gridcolor"] = _v
        _v = arg.pop("griddash", None)
        _v = griddash if griddash is not None else _v
        if _v is not None:
            self["griddash"] = _v
        _v = arg.pop("gridwidth", None)
        _v = gridwidth if gridwidth is not None else _v
        if _v is not None:
            self["gridwidth"] = _v
        _v = arg.pop("hoverformat", None)
        _v = hoverformat if hoverformat is not None else _v
        if _v is not None:
            self["hoverformat"] = _v
        _v = arg.pop("labelalias", None)
        _v = labelalias if labelalias is not None else _v
        if _v is not None:
            self["labelalias"] = _v
        _v = arg.pop("layer", None)
        _v = layer if layer is not None else _v
        if _v is not None:
            self["layer"] = _v
        _v = arg.pop("linecolor", None)
        _v = linecolor if linecolor is not None else _v
        if _v is not None:
            self["linecolor"] = _v
        _v = arg.pop("linewidth", None)
        _v = linewidth if linewidth is not None else _v
        if _v is not None:
            self["linewidth"] = _v
        _v = arg.pop("showgrid", None)
        _v = showgrid if showgrid is not None else _v
        if _v is not None:
            self["showgrid"] = _v
        _v = arg.pop("showline", None)
        _v = showline if showline is not None else _v
        if _v is not None:
            self["showline"] = _v
        _v = arg.pop("showticklabels", None)
        _v = showticklabels if showticklabels is not None else _v
        if _v is not None:
            self["showticklabels"] = _v
        _v = arg.pop("showtickprefix", None)
        _v = showtickprefix if showtickprefix is not None else _v
        if _v is not None:
            self["showtickprefix"] = _v
        _v = arg.pop("showticksuffix", None)
        _v = showticksuffix if showticksuffix is not None else _v
        if _v is not None:
            self["showticksuffix"] = _v
        _v = arg.pop("side", None)
        _v = side if side is not None else _v
        if _v is not None:
            self["side"] = _v
        _v = arg.pop("tickangle", None)
        _v = tickangle if tickangle is not None else _v
        if _v is not None:
            self["tickangle"] = _v
        _v = arg.pop("tickcolor", None)
        _v = tickcolor if tickcolor is not None else _v
        if _v is not None:
            self["tickcolor"] = _v
        _v = arg.pop("tickfont", None)
        _v = tickfont if tickfont is not None else _v
        if _v is not None:
            self["tickfont"] = _v
        _v = arg.pop("tickformat", None)
        _v = tickformat if tickformat is not None else _v
        if _v is not None:
            self["tickformat"] = _v
        _v = arg.pop("ticklen", None)
        _v = ticklen if ticklen is not None else _v
        if _v is not None:
            self["ticklen"] = _v
        _v = arg.pop("tickprefix", None)
        _v = tickprefix if tickprefix is not None else _v
        if _v is not None:
            self["tickprefix"] = _v
        _v = arg.pop("ticks", None)
        _v = ticks if ticks is not None else _v
        if _v is not None:
            self["ticks"] = _v
        _v = arg.pop("ticksuffix", None)
        _v = ticksuffix if ticksuffix is not None else _v
        if _v is not None:
            self["ticksuffix"] = _v
        _v = arg.pop("tickvals", None)
        _v = tickvals if tickvals is not None else _v
        if _v is not None:
            self["tickvals"] = _v
        _v = arg.pop("tickvalssrc", None)
        _v = tickvalssrc if tickvalssrc is not None else _v
        if _v is not None:
            self["tickvalssrc"] = _v
        _v = arg.pop("tickwidth", None)
        _v = tickwidth if tickwidth is not None else _v
        if _v is not None:
            self["tickwidth"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
