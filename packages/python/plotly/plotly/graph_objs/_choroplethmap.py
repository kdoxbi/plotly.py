from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Choroplethmap(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "choroplethmap"
    _valid_props = {
        "autocolorscale",
        "below",
        "coloraxis",
        "colorbar",
        "colorscale",
        "customdata",
        "customdatasrc",
        "featureidkey",
        "geojson",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "locations",
        "locationssrc",
        "marker",
        "meta",
        "metasrc",
        "name",
        "reversescale",
        "selected",
        "selectedpoints",
        "showlegend",
        "showscale",
        "stream",
        "subplot",
        "text",
        "textsrc",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
        "z",
        "zauto",
        "zmax",
        "zmid",
        "zmin",
        "zsrc",
    }

    @property
    def autocolorscale(self):
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    @property
    def below(self):
        return self["below"]

    @below.setter
    def below(self, val):
        self["below"] = val

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
    def featureidkey(self):
        return self["featureidkey"]

    @featureidkey.setter
    def featureidkey(self, val):
        self["featureidkey"] = val

    @property
    def geojson(self):
        return self["geojson"]

    @geojson.setter
    def geojson(self, val):
        self["geojson"] = val

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
    def locations(self):
        return self["locations"]

    @locations.setter
    def locations(self, val):
        self["locations"] = val

    @property
    def locationssrc(self):
        return self["locationssrc"]

    @locationssrc.setter
    def locationssrc(self, val):
        self["locationssrc"] = val

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
    def reversescale(self):
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

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
    def subplot(self):
        return self["subplot"]

    @subplot.setter
    def subplot(self, val):
        self["subplot"] = val

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
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        **kwargs,
    ):
        super(Choroplethmap, self).__init__("choroplethmap")

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
The first argument to the plotly.graph_objs.Choroplethmap
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Choroplethmap`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("below", None)
        _v = below if below is not None else _v
        if _v is not None:
            self["below"] = _v
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
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("featureidkey", None)
        _v = featureidkey if featureidkey is not None else _v
        if _v is not None:
            self["featureidkey"] = _v
        _v = arg.pop("geojson", None)
        _v = geojson if geojson is not None else _v
        if _v is not None:
            self["geojson"] = _v
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
        _v = arg.pop("locations", None)
        _v = locations if locations is not None else _v
        if _v is not None:
            self["locations"] = _v
        _v = arg.pop("locationssrc", None)
        _v = locationssrc if locationssrc is not None else _v
        if _v is not None:
            self["locationssrc"] = _v
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
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
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
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("subplot", None)
        _v = subplot if subplot is not None else _v
        if _v is not None:
            self["subplot"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
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
        _v = arg.pop("zsrc", None)
        _v = zsrc if zsrc is not None else _v
        if _v is not None:
            self["zsrc"] = _v
        self._props["type"] = "choroplethmap"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
