from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Baxis(_BaseTraceHierarchyType):

    _parent_path_str = "carpet"
    _path_str = "carpet.baxis"
    _valid_props = {
        "arraydtick",
        "arraytick0",
        "autorange",
        "autotypenumbers",
        "categoryarray",
        "categoryarraysrc",
        "categoryorder",
        "cheatertype",
        "color",
        "dtick",
        "endline",
        "endlinecolor",
        "endlinewidth",
        "exponentformat",
        "fixedrange",
        "gridcolor",
        "griddash",
        "gridwidth",
        "labelalias",
        "labelpadding",
        "labelprefix",
        "labelsuffix",
        "linecolor",
        "linewidth",
        "minexponent",
        "minorgridcolor",
        "minorgridcount",
        "minorgriddash",
        "minorgridwidth",
        "nticks",
        "range",
        "rangemode",
        "separatethousands",
        "showexponent",
        "showgrid",
        "showline",
        "showticklabels",
        "showtickprefix",
        "showticksuffix",
        "smoothing",
        "startline",
        "startlinecolor",
        "startlinewidth",
        "tick0",
        "tickangle",
        "tickfont",
        "tickformat",
        "tickformatstopdefaults",
        "tickformatstops",
        "tickmode",
        "tickprefix",
        "ticksuffix",
        "ticktext",
        "ticktextsrc",
        "tickvals",
        "tickvalssrc",
        "title",
        "type",
    }

    @property
    def arraydtick(self):
        return self["arraydtick"]

    @arraydtick.setter
    def arraydtick(self, val):
        self["arraydtick"] = val

    @property
    def arraytick0(self):
        return self["arraytick0"]

    @arraytick0.setter
    def arraytick0(self, val):
        self["arraytick0"] = val

    @property
    def autorange(self):
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

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
    def cheatertype(self):
        return self["cheatertype"]

    @cheatertype.setter
    def cheatertype(self, val):
        self["cheatertype"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def dtick(self):
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    @property
    def endline(self):
        return self["endline"]

    @endline.setter
    def endline(self, val):
        self["endline"] = val

    @property
    def endlinecolor(self):
        return self["endlinecolor"]

    @endlinecolor.setter
    def endlinecolor(self, val):
        self["endlinecolor"] = val

    @property
    def endlinewidth(self):
        return self["endlinewidth"]

    @endlinewidth.setter
    def endlinewidth(self, val):
        self["endlinewidth"] = val

    @property
    def exponentformat(self):
        return self["exponentformat"]

    @exponentformat.setter
    def exponentformat(self, val):
        self["exponentformat"] = val

    @property
    def fixedrange(self):
        return self["fixedrange"]

    @fixedrange.setter
    def fixedrange(self, val):
        self["fixedrange"] = val

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
    def labelalias(self):
        return self["labelalias"]

    @labelalias.setter
    def labelalias(self, val):
        self["labelalias"] = val

    @property
    def labelpadding(self):
        return self["labelpadding"]

    @labelpadding.setter
    def labelpadding(self, val):
        self["labelpadding"] = val

    @property
    def labelprefix(self):
        return self["labelprefix"]

    @labelprefix.setter
    def labelprefix(self, val):
        self["labelprefix"] = val

    @property
    def labelsuffix(self):
        return self["labelsuffix"]

    @labelsuffix.setter
    def labelsuffix(self, val):
        self["labelsuffix"] = val

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
    def minorgridcolor(self):
        return self["minorgridcolor"]

    @minorgridcolor.setter
    def minorgridcolor(self, val):
        self["minorgridcolor"] = val

    @property
    def minorgridcount(self):
        return self["minorgridcount"]

    @minorgridcount.setter
    def minorgridcount(self, val):
        self["minorgridcount"] = val

    @property
    def minorgriddash(self):
        return self["minorgriddash"]

    @minorgriddash.setter
    def minorgriddash(self, val):
        self["minorgriddash"] = val

    @property
    def minorgridwidth(self):
        return self["minorgridwidth"]

    @minorgridwidth.setter
    def minorgridwidth(self, val):
        self["minorgridwidth"] = val

    @property
    def nticks(self):
        return self["nticks"]

    @nticks.setter
    def nticks(self, val):
        self["nticks"] = val

    @property
    def range(self):
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    @property
    def rangemode(self):
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

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
    def smoothing(self):
        return self["smoothing"]

    @smoothing.setter
    def smoothing(self, val):
        self["smoothing"] = val

    @property
    def startline(self):
        return self["startline"]

    @startline.setter
    def startline(self, val):
        self["startline"] = val

    @property
    def startlinecolor(self):
        return self["startlinecolor"]

    @startlinecolor.setter
    def startlinecolor(self, val):
        self["startlinecolor"] = val

    @property
    def startlinewidth(self):
        return self["startlinewidth"]

    @startlinewidth.setter
    def startlinewidth(self, val):
        self["startlinewidth"] = val

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
    def title(self):
        return self["title"]

    @title.setter
    def title(self, val):
        self["title"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        arraydtick=None,
        arraytick0=None,
        autorange=None,
        autotypenumbers=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        cheatertype=None,
        color=None,
        dtick=None,
        endline=None,
        endlinecolor=None,
        endlinewidth=None,
        exponentformat=None,
        fixedrange=None,
        gridcolor=None,
        griddash=None,
        gridwidth=None,
        labelalias=None,
        labelpadding=None,
        labelprefix=None,
        labelsuffix=None,
        linecolor=None,
        linewidth=None,
        minexponent=None,
        minorgridcolor=None,
        minorgridcount=None,
        minorgriddash=None,
        minorgridwidth=None,
        nticks=None,
        range=None,
        rangemode=None,
        separatethousands=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        smoothing=None,
        startline=None,
        startlinecolor=None,
        startlinewidth=None,
        tick0=None,
        tickangle=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        tickmode=None,
        tickprefix=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        title=None,
        type=None,
        **kwargs,
    ):
        super(Baxis, self).__init__("baxis")

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
The first argument to the plotly.graph_objs.carpet.Baxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.carpet.Baxis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("arraydtick", None)
        _v = arraydtick if arraydtick is not None else _v
        if _v is not None:
            self["arraydtick"] = _v
        _v = arg.pop("arraytick0", None)
        _v = arraytick0 if arraytick0 is not None else _v
        if _v is not None:
            self["arraytick0"] = _v
        _v = arg.pop("autorange", None)
        _v = autorange if autorange is not None else _v
        if _v is not None:
            self["autorange"] = _v
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
        _v = arg.pop("cheatertype", None)
        _v = cheatertype if cheatertype is not None else _v
        if _v is not None:
            self["cheatertype"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("dtick", None)
        _v = dtick if dtick is not None else _v
        if _v is not None:
            self["dtick"] = _v
        _v = arg.pop("endline", None)
        _v = endline if endline is not None else _v
        if _v is not None:
            self["endline"] = _v
        _v = arg.pop("endlinecolor", None)
        _v = endlinecolor if endlinecolor is not None else _v
        if _v is not None:
            self["endlinecolor"] = _v
        _v = arg.pop("endlinewidth", None)
        _v = endlinewidth if endlinewidth is not None else _v
        if _v is not None:
            self["endlinewidth"] = _v
        _v = arg.pop("exponentformat", None)
        _v = exponentformat if exponentformat is not None else _v
        if _v is not None:
            self["exponentformat"] = _v
        _v = arg.pop("fixedrange", None)
        _v = fixedrange if fixedrange is not None else _v
        if _v is not None:
            self["fixedrange"] = _v
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
        _v = arg.pop("labelalias", None)
        _v = labelalias if labelalias is not None else _v
        if _v is not None:
            self["labelalias"] = _v
        _v = arg.pop("labelpadding", None)
        _v = labelpadding if labelpadding is not None else _v
        if _v is not None:
            self["labelpadding"] = _v
        _v = arg.pop("labelprefix", None)
        _v = labelprefix if labelprefix is not None else _v
        if _v is not None:
            self["labelprefix"] = _v
        _v = arg.pop("labelsuffix", None)
        _v = labelsuffix if labelsuffix is not None else _v
        if _v is not None:
            self["labelsuffix"] = _v
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
        _v = arg.pop("minorgridcolor", None)
        _v = minorgridcolor if minorgridcolor is not None else _v
        if _v is not None:
            self["minorgridcolor"] = _v
        _v = arg.pop("minorgridcount", None)
        _v = minorgridcount if minorgridcount is not None else _v
        if _v is not None:
            self["minorgridcount"] = _v
        _v = arg.pop("minorgriddash", None)
        _v = minorgriddash if minorgriddash is not None else _v
        if _v is not None:
            self["minorgriddash"] = _v
        _v = arg.pop("minorgridwidth", None)
        _v = minorgridwidth if minorgridwidth is not None else _v
        if _v is not None:
            self["minorgridwidth"] = _v
        _v = arg.pop("nticks", None)
        _v = nticks if nticks is not None else _v
        if _v is not None:
            self["nticks"] = _v
        _v = arg.pop("range", None)
        _v = range if range is not None else _v
        if _v is not None:
            self["range"] = _v
        _v = arg.pop("rangemode", None)
        _v = rangemode if rangemode is not None else _v
        if _v is not None:
            self["rangemode"] = _v
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
        _v = arg.pop("smoothing", None)
        _v = smoothing if smoothing is not None else _v
        if _v is not None:
            self["smoothing"] = _v
        _v = arg.pop("startline", None)
        _v = startline if startline is not None else _v
        if _v is not None:
            self["startline"] = _v
        _v = arg.pop("startlinecolor", None)
        _v = startlinecolor if startlinecolor is not None else _v
        if _v is not None:
            self["startlinecolor"] = _v
        _v = arg.pop("startlinewidth", None)
        _v = startlinewidth if startlinewidth is not None else _v
        if _v is not None:
            self["startlinewidth"] = _v
        _v = arg.pop("tick0", None)
        _v = tick0 if tick0 is not None else _v
        if _v is not None:
            self["tick0"] = _v
        _v = arg.pop("tickangle", None)
        _v = tickangle if tickangle is not None else _v
        if _v is not None:
            self["tickangle"] = _v
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
        _v = arg.pop("tickmode", None)
        _v = tickmode if tickmode is not None else _v
        if _v is not None:
            self["tickmode"] = _v
        _v = arg.pop("tickprefix", None)
        _v = tickprefix if tickprefix is not None else _v
        if _v is not None:
            self["tickprefix"] = _v
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
        _v = arg.pop("title", None)
        _v = title if title is not None else _v
        if _v is not None:
            self["title"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
