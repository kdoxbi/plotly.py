from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Parcats(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "parcats"
    _valid_props = {
        "arrangement",
        "bundlecolors",
        "counts",
        "countssrc",
        "dimensiondefaults",
        "dimensions",
        "domain",
        "hoverinfo",
        "hoveron",
        "hovertemplate",
        "labelfont",
        "legendgrouptitle",
        "legendwidth",
        "line",
        "meta",
        "metasrc",
        "name",
        "sortpaths",
        "stream",
        "tickfont",
        "type",
        "uid",
        "uirevision",
        "visible",
    }

    @property
    def arrangement(self):
        return self["arrangement"]

    @arrangement.setter
    def arrangement(self, val):
        self["arrangement"] = val

    @property
    def bundlecolors(self):
        return self["bundlecolors"]

    @bundlecolors.setter
    def bundlecolors(self, val):
        self["bundlecolors"] = val

    @property
    def counts(self):
        return self["counts"]

    @counts.setter
    def counts(self, val):
        self["counts"] = val

    @property
    def countssrc(self):
        return self["countssrc"]

    @countssrc.setter
    def countssrc(self, val):
        self["countssrc"] = val

    @property
    def dimensions(self):
        return self["dimensions"]

    @dimensions.setter
    def dimensions(self, val):
        self["dimensions"] = val

    @property
    def dimensiondefaults(self):
        return self["dimensiondefaults"]

    @dimensiondefaults.setter
    def dimensiondefaults(self, val):
        self["dimensiondefaults"] = val

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
    def hoveron(self):
        return self["hoveron"]

    @hoveron.setter
    def hoveron(self, val):
        self["hoveron"] = val

    @property
    def hovertemplate(self):
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    @property
    def labelfont(self):
        return self["labelfont"]

    @labelfont.setter
    def labelfont(self, val):
        self["labelfont"] = val

    @property
    def legendgrouptitle(self):
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

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
    def sortpaths(self):
        return self["sortpaths"]

    @sortpaths.setter
    def sortpaths(self, val):
        self["sortpaths"] = val

    @property
    def stream(self):
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def tickfont(self):
        return self["tickfont"]

    @tickfont.setter
    def tickfont(self, val):
        self["tickfont"] = val

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
    def type(self):
        return self._props["type"]

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        arrangement=None,
        bundlecolors=None,
        counts=None,
        countssrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        hoverinfo=None,
        hoveron=None,
        hovertemplate=None,
        labelfont=None,
        legendgrouptitle=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        sortpaths=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        **kwargs,
    ):
        super(Parcats, self).__init__("parcats")

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
The first argument to the plotly.graph_objs.Parcats
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Parcats`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("arrangement", None)
        _v = arrangement if arrangement is not None else _v
        if _v is not None:
            self["arrangement"] = _v
        _v = arg.pop("bundlecolors", None)
        _v = bundlecolors if bundlecolors is not None else _v
        if _v is not None:
            self["bundlecolors"] = _v
        _v = arg.pop("counts", None)
        _v = counts if counts is not None else _v
        if _v is not None:
            self["counts"] = _v
        _v = arg.pop("countssrc", None)
        _v = countssrc if countssrc is not None else _v
        if _v is not None:
            self["countssrc"] = _v
        _v = arg.pop("dimensions", None)
        _v = dimensions if dimensions is not None else _v
        if _v is not None:
            self["dimensions"] = _v
        _v = arg.pop("dimensiondefaults", None)
        _v = dimensiondefaults if dimensiondefaults is not None else _v
        if _v is not None:
            self["dimensiondefaults"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoveron", None)
        _v = hoveron if hoveron is not None else _v
        if _v is not None:
            self["hoveron"] = _v
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("labelfont", None)
        _v = labelfont if labelfont is not None else _v
        if _v is not None:
            self["labelfont"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
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
        _v = arg.pop("sortpaths", None)
        _v = sortpaths if sortpaths is not None else _v
        if _v is not None:
            self["sortpaths"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("tickfont", None)
        _v = tickfont if tickfont is not None else _v
        if _v is not None:
            self["tickfont"] = _v
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
        self._props["type"] = "parcats"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
