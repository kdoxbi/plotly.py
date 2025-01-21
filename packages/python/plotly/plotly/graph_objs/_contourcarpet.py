from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Contourcarpet(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "contourcarpet"
    _valid_props = {
        "a",
        "a0",
        "asrc",
        "atype",
        "autocolorscale",
        "autocontour",
        "b",
        "b0",
        "bsrc",
        "btype",
        "carpet",
        "coloraxis",
        "colorbar",
        "colorscale",
        "contours",
        "customdata",
        "customdatasrc",
        "da",
        "db",
        "fillcolor",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "meta",
        "metasrc",
        "name",
        "ncontours",
        "opacity",
        "reversescale",
        "showlegend",
        "showscale",
        "stream",
        "text",
        "textsrc",
        "transpose",
        "type",
        "uid",
        "uirevision",
        "visible",
        "xaxis",
        "yaxis",
        "z",
        "zauto",
        "zmax",
        "zmid",
        "zmin",
        "zorder",
        "zsrc",
    }

    @property
    def a(self):
        return self["a"]

    @a.setter
    def a(self, val):
        self["a"] = val

    @property
    def a0(self):
        return self["a0"]

    @a0.setter
    def a0(self, val):
        self["a0"] = val

    @property
    def asrc(self):
        return self["asrc"]

    @asrc.setter
    def asrc(self, val):
        self["asrc"] = val

    @property
    def atype(self):
        return self["atype"]

    @atype.setter
    def atype(self, val):
        self["atype"] = val

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
    def b(self):
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

    @property
    def b0(self):
        return self["b0"]

    @b0.setter
    def b0(self, val):
        self["b0"] = val

    @property
    def bsrc(self):
        return self["bsrc"]

    @bsrc.setter
    def bsrc(self, val):
        self["bsrc"] = val

    @property
    def btype(self):
        return self["btype"]

    @btype.setter
    def btype(self, val):
        self["btype"] = val

    @property
    def carpet(self):
        return self["carpet"]

    @carpet.setter
    def carpet(self, val):
        self["carpet"] = val

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
    def da(self):
        return self["da"]

    @da.setter
    def da(self, val):
        self["da"] = val

    @property
    def db(self):
        return self["db"]

    @db.setter
    def db(self, val):
        self["db"] = val

    @property
    def fillcolor(self):
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

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
    def transpose(self):
        return self["transpose"]

    @transpose.setter
    def transpose(self, val):
        self["transpose"] = val

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
    def xaxis(self):
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    @property
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

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
    def zorder(self):
        return self["zorder"]

    @zorder.setter
    def zorder(self, val):
        self["zorder"] = val

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
        a=None,
        a0=None,
        asrc=None,
        atype=None,
        autocolorscale=None,
        autocontour=None,
        b=None,
        b0=None,
        bsrc=None,
        btype=None,
        carpet=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        fillcolor=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zorder=None,
        zsrc=None,
        **kwargs,
    ):
        super(Contourcarpet, self).__init__("contourcarpet")

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
The first argument to the plotly.graph_objs.Contourcarpet
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Contourcarpet`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("a", None)
        _v = a if a is not None else _v
        if _v is not None:
            self["a"] = _v
        _v = arg.pop("a0", None)
        _v = a0 if a0 is not None else _v
        if _v is not None:
            self["a0"] = _v
        _v = arg.pop("asrc", None)
        _v = asrc if asrc is not None else _v
        if _v is not None:
            self["asrc"] = _v
        _v = arg.pop("atype", None)
        _v = atype if atype is not None else _v
        if _v is not None:
            self["atype"] = _v
        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("autocontour", None)
        _v = autocontour if autocontour is not None else _v
        if _v is not None:
            self["autocontour"] = _v
        _v = arg.pop("b", None)
        _v = b if b is not None else _v
        if _v is not None:
            self["b"] = _v
        _v = arg.pop("b0", None)
        _v = b0 if b0 is not None else _v
        if _v is not None:
            self["b0"] = _v
        _v = arg.pop("bsrc", None)
        _v = bsrc if bsrc is not None else _v
        if _v is not None:
            self["bsrc"] = _v
        _v = arg.pop("btype", None)
        _v = btype if btype is not None else _v
        if _v is not None:
            self["btype"] = _v
        _v = arg.pop("carpet", None)
        _v = carpet if carpet is not None else _v
        if _v is not None:
            self["carpet"] = _v
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
        _v = arg.pop("da", None)
        _v = da if da is not None else _v
        if _v is not None:
            self["da"] = _v
        _v = arg.pop("db", None)
        _v = db if db is not None else _v
        if _v is not None:
            self["db"] = _v
        _v = arg.pop("fillcolor", None)
        _v = fillcolor if fillcolor is not None else _v
        if _v is not None:
            self["fillcolor"] = _v
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
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("transpose", None)
        _v = transpose if transpose is not None else _v
        if _v is not None:
            self["transpose"] = _v
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
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("z", None)
        _v = z if z is not None else _v
        if _v is not None:
            self["z"] = _v
        _v = arg.pop("zauto", None)
        _v = zauto if zauto is not None else _v
        if _v is not None:
            self["zauto"] = _v
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
        _v = arg.pop("zorder", None)
        _v = zorder if zorder is not None else _v
        if _v is not None:
            self["zorder"] = _v
        _v = arg.pop("zsrc", None)
        _v = zsrc if zsrc is not None else _v
        if _v is not None:
            self["zsrc"] = _v
        self._props["type"] = "contourcarpet"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
