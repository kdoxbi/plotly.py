from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Histogram2dContour(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "histogram2dcontour"
    _valid_props = {
        "autobinx",
        "autobiny",
        "autocolorscale",
        "autocontour",
        "bingroup",
        "coloraxis",
        "colorbar",
        "colorscale",
        "contours",
        "customdata",
        "customdatasrc",
        "histfunc",
        "histnorm",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "marker",
        "meta",
        "metasrc",
        "name",
        "nbinsx",
        "nbinsy",
        "ncontours",
        "opacity",
        "reversescale",
        "showlegend",
        "showscale",
        "stream",
        "textfont",
        "texttemplate",
        "type",
        "uid",
        "uirevision",
        "visible",
        "x",
        "xaxis",
        "xbingroup",
        "xbins",
        "xcalendar",
        "xhoverformat",
        "xsrc",
        "y",
        "yaxis",
        "ybingroup",
        "ybins",
        "ycalendar",
        "yhoverformat",
        "ysrc",
        "z",
        "zauto",
        "zhoverformat",
        "zmax",
        "zmid",
        "zmin",
        "zsrc",
    }

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
    def autocolorscale(self):
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    @property
    def autocontour(self):
        return self["autocontour"]

    @autocontour.setter
    def autocontour(self, val):
        self["autocontour"] = val

    @property
    def bingroup(self):
        return self["bingroup"]

    @bingroup.setter
    def bingroup(self, val):
        self["bingroup"] = val

    @property
    def coloraxis(self):
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    @property
    def colorbar(self):
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    @property
    def colorscale(self):
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    @property
    def contours(self):
        return self["contours"]

    @contours.setter
    def contours(self, val):
        self["contours"] = val

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
    def ncontours(self):
        return self["ncontours"]

    @ncontours.setter
    def ncontours(self, val):
        self["ncontours"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def reversescale(self):
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    @property
    def showlegend(self):
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    @property
    def showscale(self):
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    @property
    def stream(self):
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def textfont(self):
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

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
    def xbingroup(self):
        return self["xbingroup"]

    @xbingroup.setter
    def xbingroup(self, val):
        self["xbingroup"] = val

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
    def ybingroup(self):
        return self["ybingroup"]

    @ybingroup.setter
    def ybingroup(self, val):
        self["ybingroup"] = val

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
    def z(self):
        return self["z"]

    @z.setter
    def z(self, val):
        self["z"] = val

    @property
    def zauto(self):
        return self["zauto"]

    @zauto.setter
    def zauto(self, val):
        self["zauto"] = val

    @property
    def zhoverformat(self):
        return self["zhoverformat"]

    @zhoverformat.setter
    def zhoverformat(self, val):
        self["zhoverformat"] = val

    @property
    def zmax(self):
        return self["zmax"]

    @zmax.setter
    def zmax(self, val):
        self["zmax"] = val

    @property
    def zmid(self):
        return self["zmid"]

    @zmid.setter
    def zmid(self, val):
        self["zmid"] = val

    @property
    def zmin(self):
        return self["zmin"]

    @zmin.setter
    def zmin(self, val):
        self["zmin"] = val

    @property
    def zsrc(self):
        return self["zsrc"]

    @zsrc.setter
    def zsrc(self, val):
        self["zsrc"] = val

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
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        autocontour=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        textfont=None,
        texttemplate=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        **kwargs,
    ):
        super(Histogram2dContour, self).__init__("histogram2dcontour")

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
The first argument to the plotly.graph_objs.Histogram2dContour
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Histogram2dContour`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("autobinx", None)
        _v = autobinx if autobinx is not None else _v
        if _v is not None:
            self["autobinx"] = _v
        _v = arg.pop("autobiny", None)
        _v = autobiny if autobiny is not None else _v
        if _v is not None:
            self["autobiny"] = _v
        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("autocontour", None)
        _v = autocontour if autocontour is not None else _v
        if _v is not None:
            self["autocontour"] = _v
        _v = arg.pop("bingroup", None)
        _v = bingroup if bingroup is not None else _v
        if _v is not None:
            self["bingroup"] = _v
        _v = arg.pop("coloraxis", None)
        _v = coloraxis if coloraxis is not None else _v
        if _v is not None:
            self["coloraxis"] = _v
        _v = arg.pop("colorbar", None)
        _v = colorbar if colorbar is not None else _v
        if _v is not None:
            self["colorbar"] = _v
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("contours", None)
        _v = contours if contours is not None else _v
        if _v is not None:
            self["contours"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
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
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
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
        _v = arg.pop("ncontours", None)
        _v = ncontours if ncontours is not None else _v
        if _v is not None:
            self["ncontours"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
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
        _v = arg.pop("xbingroup", None)
        _v = xbingroup if xbingroup is not None else _v
        if _v is not None:
            self["xbingroup"] = _v
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
        _v = arg.pop("ybingroup", None)
        _v = ybingroup if ybingroup is not None else _v
        if _v is not None:
            self["ybingroup"] = _v
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
        _v = arg.pop("z", None)
        _v = z if z is not None else _v
        if _v is not None:
            self["z"] = _v
        _v = arg.pop("zauto", None)
        _v = zauto if zauto is not None else _v
        if _v is not None:
            self["zauto"] = _v
        _v = arg.pop("zhoverformat", None)
        _v = zhoverformat if zhoverformat is not None else _v
        if _v is not None:
            self["zhoverformat"] = _v
        _v = arg.pop("zmax", None)
        _v = zmax if zmax is not None else _v
        if _v is not None:
            self["zmax"] = _v
        _v = arg.pop("zmid", None)
        _v = zmid if zmid is not None else _v
        if _v is not None:
            self["zmid"] = _v
        _v = arg.pop("zmin", None)
        _v = zmin if zmin is not None else _v
        if _v is not None:
            self["zmin"] = _v
        _v = arg.pop("zsrc", None)
        _v = zsrc if zsrc is not None else _v
        if _v is not None:
            self["zsrc"] = _v
        self._props["type"] = "histogram2dcontour"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
