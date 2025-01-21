from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Histogram(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "histogram"
    _valid_props = {
        "alignmentgroup",
        "autobinx",
        "autobiny",
        "bingroup",
        "cliponaxis",
        "constraintext",
        "cumulative",
        "customdata",
        "customdatasrc",
        "error_x",
        "error_y",
        "histfunc",
        "histnorm",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "insidetextanchor",
        "insidetextfont",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "marker",
        "meta",
        "metasrc",
        "name",
        "nbinsx",
        "nbinsy",
        "offsetgroup",
        "opacity",
        "orientation",
        "outsidetextfont",
        "selected",
        "selectedpoints",
        "showlegend",
        "stream",
        "text",
        "textangle",
        "textfont",
        "textposition",
        "textsrc",
        "texttemplate",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
        "x",
        "xaxis",
        "xbins",
        "xcalendar",
        "xhoverformat",
        "xsrc",
        "y",
        "yaxis",
        "ybins",
        "ycalendar",
        "yhoverformat",
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
    def autobinx(self):
        return self["autobinx"]

    @autobinx.setter
    def autobinx(self, val):
        self["autobinx"] = val

    @property
    def autobiny(self):
        return self["autobiny"]

    @autobiny.setter
    def autobiny(self, val):
        self["autobiny"] = val

    @property
    def bingroup(self):
        return self["bingroup"]

    @bingroup.setter
    def bingroup(self, val):
        self["bingroup"] = val

    @property
    def cliponaxis(self):
        return self["cliponaxis"]

    @cliponaxis.setter
    def cliponaxis(self, val):
        self["cliponaxis"] = val

    @property
    def constraintext(self):
        return self["constraintext"]

    @constraintext.setter
    def constraintext(self, val):
        self["constraintext"] = val

    @property
    def cumulative(self):
        return self["cumulative"]

    @cumulative.setter
    def cumulative(self, val):
        self["cumulative"] = val

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
    def error_x(self):
        return self["error_x"]

    @error_x.setter
    def error_x(self, val):
        self["error_x"] = val

    @property
    def error_y(self):
        return self["error_y"]

    @error_y.setter
    def error_y(self, val):
        self["error_y"] = val

    @property
    def histfunc(self):
        return self["histfunc"]

    @histfunc.setter
    def histfunc(self, val):
        self["histfunc"] = val

    @property
    def histnorm(self):
        return self["histnorm"]

    @histnorm.setter
    def histnorm(self, val):
        self["histnorm"] = val

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
    def marker(self):
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

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
    def nbinsx(self):
        return self["nbinsx"]

    @nbinsx.setter
    def nbinsx(self, val):
        self["nbinsx"] = val

    @property
    def nbinsy(self):
        return self["nbinsy"]

    @nbinsy.setter
    def nbinsy(self, val):
        self["nbinsy"] = val

    @property
    def offsetgroup(self):
        return self["offsetgroup"]

    @offsetgroup.setter
    def offsetgroup(self, val):
        self["offsetgroup"] = val

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
    def selected(self):
        return self["selected"]

    @selected.setter
    def selected(self, val):
        self["selected"] = val

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
    def textposition(self):
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

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
    def unselected(self):
        return self["unselected"]

    @unselected.setter
    def unselected(self, val):
        self["unselected"] = val

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
    def xbins(self):
        return self["xbins"]

    @xbins.setter
    def xbins(self, val):
        self["xbins"] = val

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
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def ybins(self):
        return self["ybins"]

    @ybins.setter
    def ybins(self, val):
        self["ybins"] = val

    @property
    def ycalendar(self):
        return self["ycalendar"]

    @ycalendar.setter
    def ycalendar(self, val):
        self["ycalendar"] = val

    @property
    def yhoverformat(self):
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

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
        autobinx=None,
        autobiny=None,
        bingroup=None,
        cliponaxis=None,
        constraintext=None,
        cumulative=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        xaxis=None,
        xbins=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybins=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        zorder=None,
        **kwargs,
    ):
        super(Histogram, self).__init__("histogram")

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
The first argument to the plotly.graph_objs.Histogram
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Histogram`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("alignmentgroup", None)
        _v = alignmentgroup if alignmentgroup is not None else _v
        if _v is not None:
            self["alignmentgroup"] = _v
        _v = arg.pop("autobinx", None)
        _v = autobinx if autobinx is not None else _v
        if _v is not None:
            self["autobinx"] = _v
        _v = arg.pop("autobiny", None)
        _v = autobiny if autobiny is not None else _v
        if _v is not None:
            self["autobiny"] = _v
        _v = arg.pop("bingroup", None)
        _v = bingroup if bingroup is not None else _v
        if _v is not None:
            self["bingroup"] = _v
        _v = arg.pop("cliponaxis", None)
        _v = cliponaxis if cliponaxis is not None else _v
        if _v is not None:
            self["cliponaxis"] = _v
        _v = arg.pop("constraintext", None)
        _v = constraintext if constraintext is not None else _v
        if _v is not None:
            self["constraintext"] = _v
        _v = arg.pop("cumulative", None)
        _v = cumulative if cumulative is not None else _v
        if _v is not None:
            self["cumulative"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("error_x", None)
        _v = error_x if error_x is not None else _v
        if _v is not None:
            self["error_x"] = _v
        _v = arg.pop("error_y", None)
        _v = error_y if error_y is not None else _v
        if _v is not None:
            self["error_y"] = _v
        _v = arg.pop("histfunc", None)
        _v = histfunc if histfunc is not None else _v
        if _v is not None:
            self["histfunc"] = _v
        _v = arg.pop("histnorm", None)
        _v = histnorm if histnorm is not None else _v
        if _v is not None:
            self["histnorm"] = _v
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
        _v = arg.pop("marker", None)
        _v = marker if marker is not None else _v
        if _v is not None:
            self["marker"] = _v
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
        _v = arg.pop("nbinsx", None)
        _v = nbinsx if nbinsx is not None else _v
        if _v is not None:
            self["nbinsx"] = _v
        _v = arg.pop("nbinsy", None)
        _v = nbinsy if nbinsy is not None else _v
        if _v is not None:
            self["nbinsy"] = _v
        _v = arg.pop("offsetgroup", None)
        _v = offsetgroup if offsetgroup is not None else _v
        if _v is not None:
            self["offsetgroup"] = _v
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
        _v = arg.pop("selected", None)
        _v = selected if selected is not None else _v
        if _v is not None:
            self["selected"] = _v
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
        _v = arg.pop("textposition", None)
        _v = textposition if textposition is not None else _v
        if _v is not None:
            self["textposition"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("texttemplate", None)
        _v = texttemplate if texttemplate is not None else _v
        if _v is not None:
            self["texttemplate"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("unselected", None)
        _v = unselected if unselected is not None else _v
        if _v is not None:
            self["unselected"] = _v
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
        _v = arg.pop("xbins", None)
        _v = xbins if xbins is not None else _v
        if _v is not None:
            self["xbins"] = _v
        _v = arg.pop("xcalendar", None)
        _v = xcalendar if xcalendar is not None else _v
        if _v is not None:
            self["xcalendar"] = _v
        _v = arg.pop("xhoverformat", None)
        _v = xhoverformat if xhoverformat is not None else _v
        if _v is not None:
            self["xhoverformat"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("ybins", None)
        _v = ybins if ybins is not None else _v
        if _v is not None:
            self["ybins"] = _v
        _v = arg.pop("ycalendar", None)
        _v = ycalendar if ycalendar is not None else _v
        if _v is not None:
            self["ycalendar"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v
        _v = arg.pop("zorder", None)
        _v = zorder if zorder is not None else _v
        if _v is not None:
            self["zorder"] = _v
        self._props["type"] = "histogram"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
