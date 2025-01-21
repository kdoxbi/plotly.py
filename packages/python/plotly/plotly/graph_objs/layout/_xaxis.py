from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class XAxis(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.xaxis"
    _valid_props = {
        "anchor",
        "automargin",
        "autorange",
        "autorangeoptions",
        "autotickangles",
        "autotypenumbers",
        "calendar",
        "categoryarray",
        "categoryarraysrc",
        "categoryorder",
        "color",
        "constrain",
        "constraintoward",
        "dividercolor",
        "dividerwidth",
        "domain",
        "dtick",
        "exponentformat",
        "fixedrange",
        "gridcolor",
        "griddash",
        "gridwidth",
        "hoverformat",
        "insiderange",
        "labelalias",
        "layer",
        "linecolor",
        "linewidth",
        "matches",
        "maxallowed",
        "minallowed",
        "minexponent",
        "minor",
        "mirror",
        "nticks",
        "overlaying",
        "position",
        "range",
        "rangebreakdefaults",
        "rangebreaks",
        "rangemode",
        "rangeselector",
        "rangeslider",
        "scaleanchor",
        "scaleratio",
        "separatethousands",
        "showdividers",
        "showexponent",
        "showgrid",
        "showline",
        "showspikes",
        "showticklabels",
        "showtickprefix",
        "showticksuffix",
        "side",
        "spikecolor",
        "spikedash",
        "spikemode",
        "spikesnap",
        "spikethickness",
        "tick0",
        "tickangle",
        "tickcolor",
        "tickfont",
        "tickformat",
        "tickformatstopdefaults",
        "tickformatstops",
        "ticklabelindex",
        "ticklabelindexsrc",
        "ticklabelmode",
        "ticklabeloverflow",
        "ticklabelposition",
        "ticklabelshift",
        "ticklabelstandoff",
        "ticklabelstep",
        "ticklen",
        "tickmode",
        "tickprefix",
        "ticks",
        "tickson",
        "ticksuffix",
        "ticktext",
        "ticktextsrc",
        "tickvals",
        "tickvalssrc",
        "tickwidth",
        "title",
        "type",
        "uirevision",
        "visible",
        "zeroline",
        "zerolinecolor",
        "zerolinewidth",
    }

    @property
    def anchor(self):
        return self["anchor"]

    @anchor.setter
    def anchor(self, val):
        self["anchor"] = val

    @property
    def automargin(self):
        return self["automargin"]

    @automargin.setter
    def automargin(self, val):
        self["automargin"] = val

    @property
    def autorange(self):
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

    @property
    def autorangeoptions(self):
        return self["autorangeoptions"]

    @autorangeoptions.setter
    def autorangeoptions(self, val):
        self["autorangeoptions"] = val

    @property
    def autotickangles(self):
        return self["autotickangles"]

    @autotickangles.setter
    def autotickangles(self, val):
        self["autotickangles"] = val

    @property
    def autotypenumbers(self):
        return self["autotypenumbers"]

    @autotypenumbers.setter
    def autotypenumbers(self, val):
        self["autotypenumbers"] = val

    @property
    def calendar(self):
        return self["calendar"]

    @calendar.setter
    def calendar(self, val):
        self["calendar"] = val

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
    def constrain(self):
        return self["constrain"]

    @constrain.setter
    def constrain(self, val):
        self["constrain"] = val

    @property
    def constraintoward(self):
        return self["constraintoward"]

    @constraintoward.setter
    def constraintoward(self, val):
        self["constraintoward"] = val

    @property
    def dividercolor(self):
        return self["dividercolor"]

    @dividercolor.setter
    def dividercolor(self, val):
        self["dividercolor"] = val

    @property
    def dividerwidth(self):
        return self["dividerwidth"]

    @dividerwidth.setter
    def dividerwidth(self, val):
        self["dividerwidth"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

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
    def hoverformat(self):
        return self["hoverformat"]

    @hoverformat.setter
    def hoverformat(self, val):
        self["hoverformat"] = val

    @property
    def insiderange(self):
        return self["insiderange"]

    @insiderange.setter
    def insiderange(self, val):
        self["insiderange"] = val

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
    def matches(self):
        return self["matches"]

    @matches.setter
    def matches(self, val):
        self["matches"] = val

    @property
    def maxallowed(self):
        return self["maxallowed"]

    @maxallowed.setter
    def maxallowed(self, val):
        self["maxallowed"] = val

    @property
    def minallowed(self):
        return self["minallowed"]

    @minallowed.setter
    def minallowed(self, val):
        self["minallowed"] = val

    @property
    def minexponent(self):
        return self["minexponent"]

    @minexponent.setter
    def minexponent(self, val):
        self["minexponent"] = val

    @property
    def minor(self):
        return self["minor"]

    @minor.setter
    def minor(self, val):
        self["minor"] = val

    @property
    def mirror(self):
        return self["mirror"]

    @mirror.setter
    def mirror(self, val):
        self["mirror"] = val

    @property
    def nticks(self):
        return self["nticks"]

    @nticks.setter
    def nticks(self, val):
        self["nticks"] = val

    @property
    def overlaying(self):
        return self["overlaying"]

    @overlaying.setter
    def overlaying(self, val):
        self["overlaying"] = val

    @property
    def position(self):
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

    @property
    def range(self):
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    @property
    def rangebreaks(self):
        return self["rangebreaks"]

    @rangebreaks.setter
    def rangebreaks(self, val):
        self["rangebreaks"] = val

    @property
    def rangebreakdefaults(self):
        return self["rangebreakdefaults"]

    @rangebreakdefaults.setter
    def rangebreakdefaults(self, val):
        self["rangebreakdefaults"] = val

    @property
    def rangemode(self):
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

    @property
    def rangeselector(self):
        return self["rangeselector"]

    @rangeselector.setter
    def rangeselector(self, val):
        self["rangeselector"] = val

    @property
    def rangeslider(self):
        return self["rangeslider"]

    @rangeslider.setter
    def rangeslider(self, val):
        self["rangeslider"] = val

    @property
    def scaleanchor(self):
        return self["scaleanchor"]

    @scaleanchor.setter
    def scaleanchor(self, val):
        self["scaleanchor"] = val

    @property
    def scaleratio(self):
        return self["scaleratio"]

    @scaleratio.setter
    def scaleratio(self, val):
        self["scaleratio"] = val

    @property
    def separatethousands(self):
        return self["separatethousands"]

    @separatethousands.setter
    def separatethousands(self, val):
        self["separatethousands"] = val

    @property
    def showdividers(self):
        return self["showdividers"]

    @showdividers.setter
    def showdividers(self, val):
        self["showdividers"] = val

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
    def showspikes(self):
        return self["showspikes"]

    @showspikes.setter
    def showspikes(self, val):
        self["showspikes"] = val

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
    def spikecolor(self):
        return self["spikecolor"]

    @spikecolor.setter
    def spikecolor(self, val):
        self["spikecolor"] = val

    @property
    def spikedash(self):
        return self["spikedash"]

    @spikedash.setter
    def spikedash(self, val):
        self["spikedash"] = val

    @property
    def spikemode(self):
        return self["spikemode"]

    @spikemode.setter
    def spikemode(self, val):
        self["spikemode"] = val

    @property
    def spikesnap(self):
        return self["spikesnap"]

    @spikesnap.setter
    def spikesnap(self, val):
        self["spikesnap"] = val

    @property
    def spikethickness(self):
        return self["spikethickness"]

    @spikethickness.setter
    def spikethickness(self, val):
        self["spikethickness"] = val

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
    def ticklabelindex(self):
        return self["ticklabelindex"]

    @ticklabelindex.setter
    def ticklabelindex(self, val):
        self["ticklabelindex"] = val

    @property
    def ticklabelindexsrc(self):
        return self["ticklabelindexsrc"]

    @ticklabelindexsrc.setter
    def ticklabelindexsrc(self, val):
        self["ticklabelindexsrc"] = val

    @property
    def ticklabelmode(self):
        return self["ticklabelmode"]

    @ticklabelmode.setter
    def ticklabelmode(self, val):
        self["ticklabelmode"] = val

    @property
    def ticklabeloverflow(self):
        return self["ticklabeloverflow"]

    @ticklabeloverflow.setter
    def ticklabeloverflow(self, val):
        self["ticklabeloverflow"] = val

    @property
    def ticklabelposition(self):
        return self["ticklabelposition"]

    @ticklabelposition.setter
    def ticklabelposition(self, val):
        self["ticklabelposition"] = val

    @property
    def ticklabelshift(self):
        return self["ticklabelshift"]

    @ticklabelshift.setter
    def ticklabelshift(self, val):
        self["ticklabelshift"] = val

    @property
    def ticklabelstandoff(self):
        return self["ticklabelstandoff"]

    @ticklabelstandoff.setter
    def ticklabelstandoff(self, val):
        self["ticklabelstandoff"] = val

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
    def tickson(self):
        return self["tickson"]

    @tickson.setter
    def tickson(self, val):
        self["tickson"] = val

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
    def zeroline(self):
        return self["zeroline"]

    @zeroline.setter
    def zeroline(self, val):
        self["zeroline"] = val

    @property
    def zerolinecolor(self):
        return self["zerolinecolor"]

    @zerolinecolor.setter
    def zerolinecolor(self, val):
        self["zerolinecolor"] = val

    @property
    def zerolinewidth(self):
        return self["zerolinewidth"]

    @zerolinewidth.setter
    def zerolinewidth(self, val):
        self["zerolinewidth"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        anchor=None,
        automargin=None,
        autorange=None,
        autorangeoptions=None,
        autotickangles=None,
        autotypenumbers=None,
        calendar=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        constrain=None,
        constraintoward=None,
        dividercolor=None,
        dividerwidth=None,
        domain=None,
        dtick=None,
        exponentformat=None,
        fixedrange=None,
        gridcolor=None,
        griddash=None,
        gridwidth=None,
        hoverformat=None,
        insiderange=None,
        labelalias=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        matches=None,
        maxallowed=None,
        minallowed=None,
        minexponent=None,
        minor=None,
        mirror=None,
        nticks=None,
        overlaying=None,
        position=None,
        range=None,
        rangebreaks=None,
        rangebreakdefaults=None,
        rangemode=None,
        rangeselector=None,
        rangeslider=None,
        scaleanchor=None,
        scaleratio=None,
        separatethousands=None,
        showdividers=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showspikes=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        side=None,
        spikecolor=None,
        spikedash=None,
        spikemode=None,
        spikesnap=None,
        spikethickness=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        ticklabelindex=None,
        ticklabelindexsrc=None,
        ticklabelmode=None,
        ticklabeloverflow=None,
        ticklabelposition=None,
        ticklabelshift=None,
        ticklabelstandoff=None,
        ticklabelstep=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        tickson=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        title=None,
        type=None,
        uirevision=None,
        visible=None,
        zeroline=None,
        zerolinecolor=None,
        zerolinewidth=None,
        **kwargs,
    ):
        super(XAxis, self).__init__("xaxis")

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
The first argument to the plotly.graph_objs.layout.XAxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.XAxis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("anchor", None)
        _v = anchor if anchor is not None else _v
        if _v is not None:
            self["anchor"] = _v
        _v = arg.pop("automargin", None)
        _v = automargin if automargin is not None else _v
        if _v is not None:
            self["automargin"] = _v
        _v = arg.pop("autorange", None)
        _v = autorange if autorange is not None else _v
        if _v is not None:
            self["autorange"] = _v
        _v = arg.pop("autorangeoptions", None)
        _v = autorangeoptions if autorangeoptions is not None else _v
        if _v is not None:
            self["autorangeoptions"] = _v
        _v = arg.pop("autotickangles", None)
        _v = autotickangles if autotickangles is not None else _v
        if _v is not None:
            self["autotickangles"] = _v
        _v = arg.pop("autotypenumbers", None)
        _v = autotypenumbers if autotypenumbers is not None else _v
        if _v is not None:
            self["autotypenumbers"] = _v
        _v = arg.pop("calendar", None)
        _v = calendar if calendar is not None else _v
        if _v is not None:
            self["calendar"] = _v
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
        _v = arg.pop("constrain", None)
        _v = constrain if constrain is not None else _v
        if _v is not None:
            self["constrain"] = _v
        _v = arg.pop("constraintoward", None)
        _v = constraintoward if constraintoward is not None else _v
        if _v is not None:
            self["constraintoward"] = _v
        _v = arg.pop("dividercolor", None)
        _v = dividercolor if dividercolor is not None else _v
        if _v is not None:
            self["dividercolor"] = _v
        _v = arg.pop("dividerwidth", None)
        _v = dividerwidth if dividerwidth is not None else _v
        if _v is not None:
            self["dividerwidth"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("dtick", None)
        _v = dtick if dtick is not None else _v
        if _v is not None:
            self["dtick"] = _v
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
        _v = arg.pop("hoverformat", None)
        _v = hoverformat if hoverformat is not None else _v
        if _v is not None:
            self["hoverformat"] = _v
        _v = arg.pop("insiderange", None)
        _v = insiderange if insiderange is not None else _v
        if _v is not None:
            self["insiderange"] = _v
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
        _v = arg.pop("matches", None)
        _v = matches if matches is not None else _v
        if _v is not None:
            self["matches"] = _v
        _v = arg.pop("maxallowed", None)
        _v = maxallowed if maxallowed is not None else _v
        if _v is not None:
            self["maxallowed"] = _v
        _v = arg.pop("minallowed", None)
        _v = minallowed if minallowed is not None else _v
        if _v is not None:
            self["minallowed"] = _v
        _v = arg.pop("minexponent", None)
        _v = minexponent if minexponent is not None else _v
        if _v is not None:
            self["minexponent"] = _v
        _v = arg.pop("minor", None)
        _v = minor if minor is not None else _v
        if _v is not None:
            self["minor"] = _v
        _v = arg.pop("mirror", None)
        _v = mirror if mirror is not None else _v
        if _v is not None:
            self["mirror"] = _v
        _v = arg.pop("nticks", None)
        _v = nticks if nticks is not None else _v
        if _v is not None:
            self["nticks"] = _v
        _v = arg.pop("overlaying", None)
        _v = overlaying if overlaying is not None else _v
        if _v is not None:
            self["overlaying"] = _v
        _v = arg.pop("position", None)
        _v = position if position is not None else _v
        if _v is not None:
            self["position"] = _v
        _v = arg.pop("range", None)
        _v = range if range is not None else _v
        if _v is not None:
            self["range"] = _v
        _v = arg.pop("rangebreaks", None)
        _v = rangebreaks if rangebreaks is not None else _v
        if _v is not None:
            self["rangebreaks"] = _v
        _v = arg.pop("rangebreakdefaults", None)
        _v = rangebreakdefaults if rangebreakdefaults is not None else _v
        if _v is not None:
            self["rangebreakdefaults"] = _v
        _v = arg.pop("rangemode", None)
        _v = rangemode if rangemode is not None else _v
        if _v is not None:
            self["rangemode"] = _v
        _v = arg.pop("rangeselector", None)
        _v = rangeselector if rangeselector is not None else _v
        if _v is not None:
            self["rangeselector"] = _v
        _v = arg.pop("rangeslider", None)
        _v = rangeslider if rangeslider is not None else _v
        if _v is not None:
            self["rangeslider"] = _v
        _v = arg.pop("scaleanchor", None)
        _v = scaleanchor if scaleanchor is not None else _v
        if _v is not None:
            self["scaleanchor"] = _v
        _v = arg.pop("scaleratio", None)
        _v = scaleratio if scaleratio is not None else _v
        if _v is not None:
            self["scaleratio"] = _v
        _v = arg.pop("separatethousands", None)
        _v = separatethousands if separatethousands is not None else _v
        if _v is not None:
            self["separatethousands"] = _v
        _v = arg.pop("showdividers", None)
        _v = showdividers if showdividers is not None else _v
        if _v is not None:
            self["showdividers"] = _v
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
        _v = arg.pop("showspikes", None)
        _v = showspikes if showspikes is not None else _v
        if _v is not None:
            self["showspikes"] = _v
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
        _v = arg.pop("spikecolor", None)
        _v = spikecolor if spikecolor is not None else _v
        if _v is not None:
            self["spikecolor"] = _v
        _v = arg.pop("spikedash", None)
        _v = spikedash if spikedash is not None else _v
        if _v is not None:
            self["spikedash"] = _v
        _v = arg.pop("spikemode", None)
        _v = spikemode if spikemode is not None else _v
        if _v is not None:
            self["spikemode"] = _v
        _v = arg.pop("spikesnap", None)
        _v = spikesnap if spikesnap is not None else _v
        if _v is not None:
            self["spikesnap"] = _v
        _v = arg.pop("spikethickness", None)
        _v = spikethickness if spikethickness is not None else _v
        if _v is not None:
            self["spikethickness"] = _v
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
        _v = arg.pop("ticklabelindex", None)
        _v = ticklabelindex if ticklabelindex is not None else _v
        if _v is not None:
            self["ticklabelindex"] = _v
        _v = arg.pop("ticklabelindexsrc", None)
        _v = ticklabelindexsrc if ticklabelindexsrc is not None else _v
        if _v is not None:
            self["ticklabelindexsrc"] = _v
        _v = arg.pop("ticklabelmode", None)
        _v = ticklabelmode if ticklabelmode is not None else _v
        if _v is not None:
            self["ticklabelmode"] = _v
        _v = arg.pop("ticklabeloverflow", None)
        _v = ticklabeloverflow if ticklabeloverflow is not None else _v
        if _v is not None:
            self["ticklabeloverflow"] = _v
        _v = arg.pop("ticklabelposition", None)
        _v = ticklabelposition if ticklabelposition is not None else _v
        if _v is not None:
            self["ticklabelposition"] = _v
        _v = arg.pop("ticklabelshift", None)
        _v = ticklabelshift if ticklabelshift is not None else _v
        if _v is not None:
            self["ticklabelshift"] = _v
        _v = arg.pop("ticklabelstandoff", None)
        _v = ticklabelstandoff if ticklabelstandoff is not None else _v
        if _v is not None:
            self["ticklabelstandoff"] = _v
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
        _v = arg.pop("tickson", None)
        _v = tickson if tickson is not None else _v
        if _v is not None:
            self["tickson"] = _v
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
        _v = arg.pop("title", None)
        _v = title if title is not None else _v
        if _v is not None:
            self["title"] = _v
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
        _v = arg.pop("zeroline", None)
        _v = zeroline if zeroline is not None else _v
        if _v is not None:
            self["zeroline"] = _v
        _v = arg.pop("zerolinecolor", None)
        _v = zerolinecolor if zerolinecolor is not None else _v
        if _v is not None:
            self["zerolinecolor"] = _v
        _v = arg.pop("zerolinewidth", None)
        _v = zerolinewidth if zerolinewidth is not None else _v
        if _v is not None:
            self["zerolinewidth"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
