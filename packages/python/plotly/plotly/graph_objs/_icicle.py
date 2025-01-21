from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Icicle(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "icicle"
    _valid_props = {
        "branchvalues",
        "count",
        "customdata",
        "customdatasrc",
        "domain",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "insidetextfont",
        "labels",
        "labelssrc",
        "leaf",
        "legend",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "level",
        "marker",
        "maxdepth",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "outsidetextfont",
        "parents",
        "parentssrc",
        "pathbar",
        "root",
        "sort",
        "stream",
        "text",
        "textfont",
        "textinfo",
        "textposition",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "tiling",
        "type",
        "uid",
        "uirevision",
        "values",
        "valuessrc",
        "visible",
    }

    @property
    def branchvalues(self):
        return self["branchvalues"]

    @branchvalues.setter
    def branchvalues(self, val):
        self["branchvalues"] = val

    @property
    def count(self):
        return self["count"]

    @count.setter
    def count(self, val):
        self["count"] = val

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
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

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
    def insidetextfont(self):
        return self["insidetextfont"]

    @insidetextfont.setter
    def insidetextfont(self, val):
        self["insidetextfont"] = val

    @property
    def labels(self):
        return self["labels"]

    @labels.setter
    def labels(self, val):
        self["labels"] = val

    @property
    def labelssrc(self):
        return self["labelssrc"]

    @labelssrc.setter
    def labelssrc(self, val):
        self["labelssrc"] = val

    @property
    def leaf(self):
        return self["leaf"]

    @leaf.setter
    def leaf(self, val):
        self["leaf"] = val

    @property
    def legend(self):
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

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
    def level(self):
        return self["level"]

    @level.setter
    def level(self, val):
        self["level"] = val

    @property
    def marker(self):
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def maxdepth(self):
        return self["maxdepth"]

    @maxdepth.setter
    def maxdepth(self, val):
        self["maxdepth"] = val

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
    def outsidetextfont(self):
        return self["outsidetextfont"]

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self["outsidetextfont"] = val

    @property
    def parents(self):
        return self["parents"]

    @parents.setter
    def parents(self, val):
        self["parents"] = val

    @property
    def parentssrc(self):
        return self["parentssrc"]

    @parentssrc.setter
    def parentssrc(self, val):
        self["parentssrc"] = val

    @property
    def pathbar(self):
        return self["pathbar"]

    @pathbar.setter
    def pathbar(self, val):
        self["pathbar"] = val

    @property
    def root(self):
        return self["root"]

    @root.setter
    def root(self, val):
        self["root"] = val

    @property
    def sort(self):
        return self["sort"]

    @sort.setter
    def sort(self, val):
        self["sort"] = val

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
    def tiling(self):
        return self["tiling"]

    @tiling.setter
    def tiling(self, val):
        self["tiling"] = val

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
    def values(self):
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    @property
    def valuessrc(self):
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

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
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        labels=None,
        labelssrc=None,
        leaf=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        pathbar=None,
        root=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tiling=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        **kwargs,
    ):
        super(Icicle, self).__init__("icicle")

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
The first argument to the plotly.graph_objs.Icicle
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Icicle`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("branchvalues", None)
        _v = branchvalues if branchvalues is not None else _v
        if _v is not None:
            self["branchvalues"] = _v
        _v = arg.pop("count", None)
        _v = count if count is not None else _v
        if _v is not None:
            self["count"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
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
        _v = arg.pop("insidetextfont", None)
        _v = insidetextfont if insidetextfont is not None else _v
        if _v is not None:
            self["insidetextfont"] = _v
        _v = arg.pop("labels", None)
        _v = labels if labels is not None else _v
        if _v is not None:
            self["labels"] = _v
        _v = arg.pop("labelssrc", None)
        _v = labelssrc if labelssrc is not None else _v
        if _v is not None:
            self["labelssrc"] = _v
        _v = arg.pop("leaf", None)
        _v = leaf if leaf is not None else _v
        if _v is not None:
            self["leaf"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
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
        _v = arg.pop("level", None)
        _v = level if level is not None else _v
        if _v is not None:
            self["level"] = _v
        _v = arg.pop("marker", None)
        _v = marker if marker is not None else _v
        if _v is not None:
            self["marker"] = _v
        _v = arg.pop("maxdepth", None)
        _v = maxdepth if maxdepth is not None else _v
        if _v is not None:
            self["maxdepth"] = _v
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
        _v = arg.pop("outsidetextfont", None)
        _v = outsidetextfont if outsidetextfont is not None else _v
        if _v is not None:
            self["outsidetextfont"] = _v
        _v = arg.pop("parents", None)
        _v = parents if parents is not None else _v
        if _v is not None:
            self["parents"] = _v
        _v = arg.pop("parentssrc", None)
        _v = parentssrc if parentssrc is not None else _v
        if _v is not None:
            self["parentssrc"] = _v
        _v = arg.pop("pathbar", None)
        _v = pathbar if pathbar is not None else _v
        if _v is not None:
            self["pathbar"] = _v
        _v = arg.pop("root", None)
        _v = root if root is not None else _v
        if _v is not None:
            self["root"] = _v
        _v = arg.pop("sort", None)
        _v = sort if sort is not None else _v
        if _v is not None:
            self["sort"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
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
        _v = arg.pop("tiling", None)
        _v = tiling if tiling is not None else _v
        if _v is not None:
            self["tiling"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("values", None)
        _v = values if values is not None else _v
        if _v is not None:
            self["values"] = _v
        _v = arg.pop("valuessrc", None)
        _v = valuessrc if valuessrc is not None else _v
        if _v is not None:
            self["valuessrc"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._props["type"] = "icicle"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
