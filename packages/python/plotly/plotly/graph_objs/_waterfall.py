from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Waterfall(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "waterfall"
    _valid_props = {
        "alignmentgroup",
        "base",
        "cliponaxis",
        "connector",
        "constraintext",
        "customdata",
        "customdatasrc",
        "decreasing",
        "dx",
        "dy",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "increasing",
        "insidetextanchor",
        "insidetextfont",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "measure",
        "measuresrc",
        "meta",
        "metasrc",
        "name",
        "offset",
        "offsetgroup",
        "offsetsrc",
        "opacity",
        "orientation",
        "outsidetextfont",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textangle",
        "textfont",
        "textinfo",
        "textposition",
        "textpositionsrc",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "totals",
        "type",
        "uid",
        "uirevision",
        "visible",
        "width",
        "widthsrc",
        "x",
        "x0",
        "xaxis",
        "xhoverformat",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "y",
        "y0",
        "yaxis",
        "yhoverformat",
        "yperiod",
        "yperiod0",
        "yperiodalignment",
        "ysrc",
        "zorder",
    }

    @property
    def alignmentgroup(self):
        return self["alignmentgroup"]

    @alignmentgroup.setter
    def alignmentgroup(self, val):
        self["alignmentgroup"] = val

    @property
    def base(self):
        return self["base"]

    @base.setter
    def base(self, val):
        self["base"] = val

    @property
    def cliponaxis(self):
        return self["cliponaxis"]

    @cliponaxis.setter
    def cliponaxis(self, val):
        self["cliponaxis"] = val

    @property
    def connector(self):
        return self["connector"]

    @connector.setter
    def connector(self, val):
        self["connector"] = val

    @property
    def constraintext(self):
        return self["constraintext"]

    @constraintext.setter
    def constraintext(self, val):
        self["constraintext"] = val

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
    def dx(self):
        return self["dx"]

    @dx.setter
    def dx(self, val):
        self["dx"] = val

    @property
    def dy(self):
        return self["dy"]

    @dy.setter
    def dy(self, val):
        self["dy"] = val

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
    def hovertemplate(self):
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    @property
    def hovertemplatesrc(self):
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

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
    def insidetextanchor(self):
        return self["insidetextanchor"]

    @insidetextanchor.setter
    def insidetextanchor(self, val):
        self["insidetextanchor"] = val

    @property
    def insidetextfont(self):
        return self["insidetextfont"]

    @insidetextfont.setter
    def insidetextfont(self, val):
        self["insidetextfont"] = val

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
    def measure(self):
        return self["measure"]

    @measure.setter
    def measure(self, val):
        self["measure"] = val

    @property
    def measuresrc(self):
        return self["measuresrc"]

    @measuresrc.setter
    def measuresrc(self, val):
        self["measuresrc"] = val

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
    def offset(self):
        return self["offset"]

    @offset.setter
    def offset(self, val):
        self["offset"] = val

    @property
    def offsetgroup(self):
        return self["offsetgroup"]

    @offsetgroup.setter
    def offsetgroup(self, val):
        self["offsetgroup"] = val

    @property
    def offsetsrc(self):
        return self["offsetsrc"]

    @offsetsrc.setter
    def offsetsrc(self, val):
        self["offsetsrc"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def orientation(self):
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def outsidetextfont(self):
        return self["outsidetextfont"]

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self["outsidetextfont"] = val

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
    def textangle(self):
        return self["textangle"]

    @textangle.setter
    def textangle(self, val):
        self["textangle"] = val

    @property
    def textfont(self):
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def textinfo(self):
        return self["textinfo"]

    @textinfo.setter
    def textinfo(self, val):
        self["textinfo"] = val

    @property
    def textposition(self):
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

    @property
    def textpositionsrc(self):
        return self["textpositionsrc"]

    @textpositionsrc.setter
    def textpositionsrc(self, val):
        self["textpositionsrc"] = val

    @property
    def textsrc(self):
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    @property
    def texttemplate(self):
        return self["texttemplate"]

    @texttemplate.setter
    def texttemplate(self, val):
        self["texttemplate"] = val

    @property
    def texttemplatesrc(self):
        return self["texttemplatesrc"]

    @texttemplatesrc.setter
    def texttemplatesrc(self, val):
        self["texttemplatesrc"] = val

    @property
    def totals(self):
        return self["totals"]

    @totals.setter
    def totals(self, val):
        self["totals"] = val

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
    def width(self):
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def widthsrc(self):
        return self["widthsrc"]

    @widthsrc.setter
    def widthsrc(self, val):
        self["widthsrc"] = val

    @property
    def x(self):
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def x0(self):
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    @property
    def xaxis(self):
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

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
    def y(self):
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def y0(self):
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

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
    def yperiod(self):
        return self["yperiod"]

    @yperiod.setter
    def yperiod(self, val):
        self["yperiod"] = val

    @property
    def yperiod0(self):
        return self["yperiod0"]

    @yperiod0.setter
    def yperiod0(self, val):
        self["yperiod0"] = val

    @property
    def yperiodalignment(self):
        return self["yperiodalignment"]

    @yperiodalignment.setter
    def yperiodalignment(self, val):
        self["yperiodalignment"] = val

    @property
    def ysrc(self):
        return self["ysrc"]

    @ysrc.setter
    def ysrc(self, val):
        self["ysrc"] = val

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
        alignmentgroup=None,
        base=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        measure=None,
        measuresrc=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        totals=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        **kwargs,
    ):
        super(Waterfall, self).__init__("waterfall")

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
The first argument to the plotly.graph_objs.Waterfall
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Waterfall`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("alignmentgroup", None)
        _v = alignmentgroup if alignmentgroup is not None else _v
        if _v is not None:
            self["alignmentgroup"] = _v
        _v = arg.pop("base", None)
        _v = base if base is not None else _v
        if _v is not None:
            self["base"] = _v
        _v = arg.pop("cliponaxis", None)
        _v = cliponaxis if cliponaxis is not None else _v
        if _v is not None:
            self["cliponaxis"] = _v
        _v = arg.pop("connector", None)
        _v = connector if connector is not None else _v
        if _v is not None:
            self["connector"] = _v
        _v = arg.pop("constraintext", None)
        _v = constraintext if constraintext is not None else _v
        if _v is not None:
            self["constraintext"] = _v
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
        _v = arg.pop("dx", None)
        _v = dx if dx is not None else _v
        if _v is not None:
            self["dx"] = _v
        _v = arg.pop("dy", None)
        _v = dy if dy is not None else _v
        if _v is not None:
            self["dy"] = _v
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
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("hovertemplatesrc", None)
        _v = hovertemplatesrc if hovertemplatesrc is not None else _v
        if _v is not None:
            self["hovertemplatesrc"] = _v
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
        _v = arg.pop("insidetextanchor", None)
        _v = insidetextanchor if insidetextanchor is not None else _v
        if _v is not None:
            self["insidetextanchor"] = _v
        _v = arg.pop("insidetextfont", None)
        _v = insidetextfont if insidetextfont is not None else _v
        if _v is not None:
            self["insidetextfont"] = _v
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
        _v = arg.pop("measure", None)
        _v = measure if measure is not None else _v
        if _v is not None:
            self["measure"] = _v
        _v = arg.pop("measuresrc", None)
        _v = measuresrc if measuresrc is not None else _v
        if _v is not None:
            self["measuresrc"] = _v
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
        _v = arg.pop("offset", None)
        _v = offset if offset is not None else _v
        if _v is not None:
            self["offset"] = _v
        _v = arg.pop("offsetgroup", None)
        _v = offsetgroup if offsetgroup is not None else _v
        if _v is not None:
            self["offsetgroup"] = _v
        _v = arg.pop("offsetsrc", None)
        _v = offsetsrc if offsetsrc is not None else _v
        if _v is not None:
            self["offsetsrc"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("orientation", None)
        _v = orientation if orientation is not None else _v
        if _v is not None:
            self["orientation"] = _v
        _v = arg.pop("outsidetextfont", None)
        _v = outsidetextfont if outsidetextfont is not None else _v
        if _v is not None:
            self["outsidetextfont"] = _v
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
        _v = arg.pop("textangle", None)
        _v = textangle if textangle is not None else _v
        if _v is not None:
            self["textangle"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
        _v = arg.pop("textinfo", None)
        _v = textinfo if textinfo is not None else _v
        if _v is not None:
            self["textinfo"] = _v
        _v = arg.pop("textposition", None)
        _v = textposition if textposition is not None else _v
        if _v is not None:
            self["textposition"] = _v
        _v = arg.pop("textpositionsrc", None)
        _v = textpositionsrc if textpositionsrc is not None else _v
        if _v is not None:
            self["textpositionsrc"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("texttemplate", None)
        _v = texttemplate if texttemplate is not None else _v
        if _v is not None:
            self["texttemplate"] = _v
        _v = arg.pop("texttemplatesrc", None)
        _v = texttemplatesrc if texttemplatesrc is not None else _v
        if _v is not None:
            self["texttemplatesrc"] = _v
        _v = arg.pop("totals", None)
        _v = totals if totals is not None else _v
        if _v is not None:
            self["totals"] = _v
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
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        _v = arg.pop("widthsrc", None)
        _v = widthsrc if widthsrc is not None else _v
        if _v is not None:
            self["widthsrc"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("x0", None)
        _v = x0 if x0 is not None else _v
        if _v is not None:
            self["x0"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
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
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("y0", None)
        _v = y0 if y0 is not None else _v
        if _v is not None:
            self["y0"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("yperiod", None)
        _v = yperiod if yperiod is not None else _v
        if _v is not None:
            self["yperiod"] = _v
        _v = arg.pop("yperiod0", None)
        _v = yperiod0 if yperiod0 is not None else _v
        if _v is not None:
            self["yperiod0"] = _v
        _v = arg.pop("yperiodalignment", None)
        _v = yperiodalignment if yperiodalignment is not None else _v
        if _v is not None:
            self["yperiodalignment"] = _v
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v
        _v = arg.pop("zorder", None)
        _v = zorder if zorder is not None else _v
        if _v is not None:
            self["zorder"] = _v
        self._props["type"] = "waterfall"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
