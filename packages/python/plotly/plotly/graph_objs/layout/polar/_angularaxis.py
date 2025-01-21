from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class AngularAxis(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.polar"
    _path_str = "layout.polar.angularaxis"
    _valid_props = {
        "autotypenumbers",
        "categoryarray",
        "categoryarraysrc",
        "categoryorder",
        "color",
        "direction",
        "dtick",
        "exponentformat",
        "gridcolor",
        "griddash",
        "gridwidth",
        "hoverformat",
        "labelalias",
        "layer",
        "linecolor",
        "linewidth",
        "minexponent",
        "nticks",
        "period",
        "rotation",
        "separatethousands",
        "showexponent",
        "showgrid",
        "showline",
        "showticklabels",
        "showtickprefix",
        "showticksuffix",
        "thetaunit",
        "tick0",
        "tickangle",
        "tickcolor",
        "tickfont",
        "tickformat",
        "tickformatstopdefaults",
        "tickformatstops",
        "ticklabelstep",
        "ticklen",
        "tickmode",
        "tickprefix",
        "ticks",
        "ticksuffix",
        "ticktext",
        "ticktextsrc",
        "tickvals",
        "tickvalssrc",
        "tickwidth",
        "type",
        "uirevision",
        "visible",
    }

    @property
    def autotypenumbers(self):
        return self["autotypenumbers"]

    @autotypenumbers.setter
    def autotypenumbers(self, val):
        self["autotypenumbers"] = val

    @property
    def categoryarray(self):
        return self["categoryarray"]

    @categoryarray.setter
    def categoryarray(self, val):
        self["categoryarray"] = val

    @property
    def categoryarraysrc(self):
        return self["categoryarraysrc"]

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self["categoryarraysrc"] = val

    @property
    def categoryorder(self):
        return self["categoryorder"]

    @categoryorder.setter
    def categoryorder(self, val):
        self["categoryorder"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def direction(self):
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    @property
    def dtick(self):
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    @property
    def exponentformat(self):
        return self["exponentformat"]

    @exponentformat.setter
    def exponentformat(self, val):
        self["exponentformat"] = val

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
    def minexponent(self):
        return self["minexponent"]

    @minexponent.setter
    def minexponent(self, val):
        self["minexponent"] = val

    @property
    def nticks(self):
        return self["nticks"]

    @nticks.setter
    def nticks(self, val):
        self["nticks"] = val

    @property
    def period(self):
        return self["period"]

    @period.setter
    def period(self, val):
        self["period"] = val

    @property
    def rotation(self):
        return self["rotation"]

    @rotation.setter
    def rotation(self, val):
        self["rotation"] = val

    @property
    def separatethousands(self):
        return self["separatethousands"]

    @separatethousands.setter
    def separatethousands(self, val):
        self["separatethousands"] = val

    @property
    def showexponent(self):
        return self["showexponent"]

    @showexponent.setter
    def showexponent(self, val):
        self["showexponent"] = val

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
    def thetaunit(self):
        return self["thetaunit"]

    @thetaunit.setter
    def thetaunit(self, val):
        self["thetaunit"] = val

    @property
    def tick0(self):
        return self["tick0"]

    @tick0.setter
    def tick0(self, val):
        self["tick0"] = val

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
    def tickformatstops(self):
        return self["tickformatstops"]

    @tickformatstops.setter
    def tickformatstops(self, val):
        self["tickformatstops"] = val

    @property
    def tickformatstopdefaults(self):
        return self["tickformatstopdefaults"]

    @tickformatstopdefaults.setter
    def tickformatstopdefaults(self, val):
        self["tickformatstopdefaults"] = val

    @property
    def ticklabelstep(self):
        return self["ticklabelstep"]

    @ticklabelstep.setter
    def ticklabelstep(self, val):
        self["ticklabelstep"] = val

    @property
    def ticklen(self):
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    @property
    def tickmode(self):
        return self["tickmode"]

    @tickmode.setter
    def tickmode(self, val):
        self["tickmode"] = val

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
    def ticktext(self):
        return self["ticktext"]

    @ticktext.setter
    def ticktext(self, val):
        self["ticktext"] = val

    @property
    def ticktextsrc(self):
        return self["ticktextsrc"]

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self["ticktextsrc"] = val

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
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

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
        autotypenumbers=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        direction=None,
        dtick=None,
        exponentformat=None,
        gridcolor=None,
        griddash=None,
        gridwidth=None,
        hoverformat=None,
        labelalias=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        minexponent=None,
        nticks=None,
        period=None,
        rotation=None,
        separatethousands=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        thetaunit=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        ticklabelstep=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        type=None,
        uirevision=None,
        visible=None,
        **kwargs,
    ):
        super(AngularAxis, self).__init__("angularaxis")

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
The first argument to the plotly.graph_objs.layout.polar.AngularAxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.polar.AngularAxis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("autotypenumbers", None)
        _v = autotypenumbers if autotypenumbers is not None else _v
        if _v is not None:
            self["autotypenumbers"] = _v
        _v = arg.pop("categoryarray", None)
        _v = categoryarray if categoryarray is not None else _v
        if _v is not None:
            self["categoryarray"] = _v
        _v = arg.pop("categoryarraysrc", None)
        _v = categoryarraysrc if categoryarraysrc is not None else _v
        if _v is not None:
            self["categoryarraysrc"] = _v
        _v = arg.pop("categoryorder", None)
        _v = categoryorder if categoryorder is not None else _v
        if _v is not None:
            self["categoryorder"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("direction", None)
        _v = direction if direction is not None else _v
        if _v is not None:
            self["direction"] = _v
        _v = arg.pop("dtick", None)
        _v = dtick if dtick is not None else _v
        if _v is not None:
            self["dtick"] = _v
        _v = arg.pop("exponentformat", None)
        _v = exponentformat if exponentformat is not None else _v
        if _v is not None:
            self["exponentformat"] = _v
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
        _v = arg.pop("minexponent", None)
        _v = minexponent if minexponent is not None else _v
        if _v is not None:
            self["minexponent"] = _v
        _v = arg.pop("nticks", None)
        _v = nticks if nticks is not None else _v
        if _v is not None:
            self["nticks"] = _v
        _v = arg.pop("period", None)
        _v = period if period is not None else _v
        if _v is not None:
            self["period"] = _v
        _v = arg.pop("rotation", None)
        _v = rotation if rotation is not None else _v
        if _v is not None:
            self["rotation"] = _v
        _v = arg.pop("separatethousands", None)
        _v = separatethousands if separatethousands is not None else _v
        if _v is not None:
            self["separatethousands"] = _v
        _v = arg.pop("showexponent", None)
        _v = showexponent if showexponent is not None else _v
        if _v is not None:
            self["showexponent"] = _v
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
        _v = arg.pop("thetaunit", None)
        _v = thetaunit if thetaunit is not None else _v
        if _v is not None:
            self["thetaunit"] = _v
        _v = arg.pop("tick0", None)
        _v = tick0 if tick0 is not None else _v
        if _v is not None:
            self["tick0"] = _v
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
        _v = arg.pop("tickformatstops", None)
        _v = tickformatstops if tickformatstops is not None else _v
        if _v is not None:
            self["tickformatstops"] = _v
        _v = arg.pop("tickformatstopdefaults", None)
        _v = tickformatstopdefaults if tickformatstopdefaults is not None else _v
        if _v is not None:
            self["tickformatstopdefaults"] = _v
        _v = arg.pop("ticklabelstep", None)
        _v = ticklabelstep if ticklabelstep is not None else _v
        if _v is not None:
            self["ticklabelstep"] = _v
        _v = arg.pop("ticklen", None)
        _v = ticklen if ticklen is not None else _v
        if _v is not None:
            self["ticklen"] = _v
        _v = arg.pop("tickmode", None)
        _v = tickmode if tickmode is not None else _v
        if _v is not None:
            self["tickmode"] = _v
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
        _v = arg.pop("ticktext", None)
        _v = ticktext if ticktext is not None else _v
        if _v is not None:
            self["ticktext"] = _v
        _v = arg.pop("ticktextsrc", None)
        _v = ticktextsrc if ticktextsrc is not None else _v
        if _v is not None:
            self["ticktextsrc"] = _v
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
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
