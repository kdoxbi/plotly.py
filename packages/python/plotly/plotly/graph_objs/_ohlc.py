from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Ohlc(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "ohlc"
    _valid_props = {
        "close",
        "closesrc",
        "customdata",
        "customdatasrc",
        "decreasing",
        "high",
        "highsrc",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "increasing",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "low",
        "lowsrc",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "open",
        "opensrc",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textsrc",
        "tickwidth",
        "type",
        "uid",
        "uirevision",
        "visible",
        "x",
        "xaxis",
        "xcalendar",
        "xhoverformat",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "yaxis",
        "yhoverformat",
        "zorder",
    }

    @property
    def close(self):
        return self["close"]

    @close.setter
    def close(self, val):
        self["close"] = val

    @property
    def closesrc(self):
        return self["closesrc"]

    @closesrc.setter
    def closesrc(self, val):
        self["closesrc"] = val

    @property
    def customdata(self):
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    @property
    def customdatasrc(self):
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    @property
    def decreasing(self):
        return self["decreasing"]

    @decreasing.setter
    def decreasing(self, val):
        self["decreasing"] = val

    @property
    def high(self):
        return self["high"]

    @high.setter
    def high(self, val):
        self["high"] = val

    @property
    def highsrc(self):
        return self["highsrc"]

    @highsrc.setter
    def highsrc(self, val):
        self["highsrc"] = val

    @property
    def hoverinfo(self):
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    @property
    def hoverinfosrc(self):
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    @property
    def hoverlabel(self):
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hovertext(self):
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    @property
    def hovertextsrc(self):
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

    @property
    def ids(self):
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    @property
    def idssrc(self):
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    @property
    def increasing(self):
        return self["increasing"]

    @increasing.setter
    def increasing(self, val):
        self["increasing"] = val

    @property
    def legend(self):
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    @property
    def legendgroup(self):
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    @property
    def legendgrouptitle(self):
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    @property
    def legendrank(self):
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    @property
    def legendwidth(self):
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def low(self):
        return self["low"]

    @low.setter
    def low(self, val):
        self["low"] = val

    @property
    def lowsrc(self):
        return self["lowsrc"]

    @lowsrc.setter
    def lowsrc(self, val):
        self["lowsrc"] = val

    @property
    def meta(self):
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    @property
    def metasrc(self):
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def open(self):
        return self["open"]

    @open.setter
    def open(self, val):
        self["open"] = val

    @property
    def opensrc(self):
        return self["opensrc"]

    @opensrc.setter
    def opensrc(self, val):
        self["opensrc"] = val

    @property
    def selectedpoints(self):
        return self["selectedpoints"]

    @selectedpoints.setter
    def selectedpoints(self, val):
        self["selectedpoints"] = val

    @property
    def showlegend(self):
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    @property
    def stream(self):
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textsrc(self):
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    @property
    def tickwidth(self):
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    @property
    def uid(self):
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

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
    def x(self):
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def xaxis(self):
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    @property
    def xcalendar(self):
        return self["xcalendar"]

    @xcalendar.setter
    def xcalendar(self, val):
        self["xcalendar"] = val

    @property
    def xhoverformat(self):
        return self["xhoverformat"]

    @xhoverformat.setter
    def xhoverformat(self, val):
        self["xhoverformat"] = val

    @property
    def xperiod(self):
        return self["xperiod"]

    @xperiod.setter
    def xperiod(self, val):
        self["xperiod"] = val

    @property
    def xperiod0(self):
        return self["xperiod0"]

    @xperiod0.setter
    def xperiod0(self, val):
        self["xperiod0"] = val

    @property
    def xperiodalignment(self):
        return self["xperiodalignment"]

    @xperiodalignment.setter
    def xperiodalignment(self, val):
        self["xperiodalignment"] = val

    @property
    def xsrc(self):
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    @property
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def yhoverformat(self):
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

    @property
    def zorder(self):
        return self["zorder"]

    @zorder.setter
    def zorder(self, val):
        self["zorder"] = val

    @property
    def type(self):
        return self._props["type"]

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        yhoverformat=None,
        zorder=None,
        **kwargs,
    ):
        super(Ohlc, self).__init__("ohlc")

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
The first argument to the plotly.graph_objs.Ohlc
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Ohlc`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("close", None)
        _v = close if close is not None else _v
        if _v is not None:
            self["close"] = _v
        _v = arg.pop("closesrc", None)
        _v = closesrc if closesrc is not None else _v
        if _v is not None:
            self["closesrc"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("decreasing", None)
        _v = decreasing if decreasing is not None else _v
        if _v is not None:
            self["decreasing"] = _v
        _v = arg.pop("high", None)
        _v = high if high is not None else _v
        if _v is not None:
            self["high"] = _v
        _v = arg.pop("highsrc", None)
        _v = highsrc if highsrc is not None else _v
        if _v is not None:
            self["highsrc"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverinfosrc", None)
        _v = hoverinfosrc if hoverinfosrc is not None else _v
        if _v is not None:
            self["hoverinfosrc"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("hovertextsrc", None)
        _v = hovertextsrc if hovertextsrc is not None else _v
        if _v is not None:
            self["hovertextsrc"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("increasing", None)
        _v = increasing if increasing is not None else _v
        if _v is not None:
            self["increasing"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
        _v = arg.pop("legendrank", None)
        _v = legendrank if legendrank is not None else _v
        if _v is not None:
            self["legendrank"] = _v
        _v = arg.pop("legendwidth", None)
        _v = legendwidth if legendwidth is not None else _v
        if _v is not None:
            self["legendwidth"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("low", None)
        _v = low if low is not None else _v
        if _v is not None:
            self["low"] = _v
        _v = arg.pop("lowsrc", None)
        _v = lowsrc if lowsrc is not None else _v
        if _v is not None:
            self["lowsrc"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("open", None)
        _v = open if open is not None else _v
        if _v is not None:
            self["open"] = _v
        _v = arg.pop("opensrc", None)
        _v = opensrc if opensrc is not None else _v
        if _v is not None:
            self["opensrc"] = _v
        _v = arg.pop("selectedpoints", None)
        _v = selectedpoints if selectedpoints is not None else _v
        if _v is not None:
            self["selectedpoints"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("tickwidth", None)
        _v = tickwidth if tickwidth is not None else _v
        if _v is not None:
            self["tickwidth"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("xcalendar", None)
        _v = xcalendar if xcalendar is not None else _v
        if _v is not None:
            self["xcalendar"] = _v
        _v = arg.pop("xhoverformat", None)
        _v = xhoverformat if xhoverformat is not None else _v
        if _v is not None:
            self["xhoverformat"] = _v
        _v = arg.pop("xperiod", None)
        _v = xperiod if xperiod is not None else _v
        if _v is not None:
            self["xperiod"] = _v
        _v = arg.pop("xperiod0", None)
        _v = xperiod0 if xperiod0 is not None else _v
        if _v is not None:
            self["xperiod0"] = _v
        _v = arg.pop("xperiodalignment", None)
        _v = xperiodalignment if xperiodalignment is not None else _v
        if _v is not None:
            self["xperiodalignment"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("zorder", None)
        _v = zorder if zorder is not None else _v
        if _v is not None:
            self["zorder"] = _v
        self._props["type"] = "ohlc"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
