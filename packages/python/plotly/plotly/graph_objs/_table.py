from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Table(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "table"
    _valid_props = {
        "cells",
        "columnorder",
        "columnordersrc",
        "columnwidth",
        "columnwidthsrc",
        "customdata",
        "customdatasrc",
        "domain",
        "header",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "ids",
        "idssrc",
        "legend",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "meta",
        "metasrc",
        "name",
        "stream",
        "type",
        "uid",
        "uirevision",
        "visible",
    }

    @property
    def cells(self):
        return self["cells"]

    @cells.setter
    def cells(self, val):
        self["cells"] = val

    @property
    def columnorder(self):
        return self["columnorder"]

    @columnorder.setter
    def columnorder(self, val):
        self["columnorder"] = val

    @property
    def columnordersrc(self):
        return self["columnordersrc"]

    @columnordersrc.setter
    def columnordersrc(self, val):
        self["columnordersrc"] = val

    @property
    def columnwidth(self):
        return self["columnwidth"]

    @columnwidth.setter
    def columnwidth(self, val):
        self["columnwidth"] = val

    @property
    def columnwidthsrc(self):
        return self["columnwidthsrc"]

    @columnwidthsrc.setter
    def columnwidthsrc(self, val):
        self["columnwidthsrc"] = val

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
    def header(self):
        return self["header"]

    @header.setter
    def header(self, val):
        self["header"] = val

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
    def stream(self):
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

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
        cells=None,
        columnorder=None,
        columnordersrc=None,
        columnwidth=None,
        columnwidthsrc=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        header=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        **kwargs,
    ):
        super(Table, self).__init__("table")

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
The first argument to the plotly.graph_objs.Table
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Table`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("cells", None)
        _v = cells if cells is not None else _v
        if _v is not None:
            self["cells"] = _v
        _v = arg.pop("columnorder", None)
        _v = columnorder if columnorder is not None else _v
        if _v is not None:
            self["columnorder"] = _v
        _v = arg.pop("columnordersrc", None)
        _v = columnordersrc if columnordersrc is not None else _v
        if _v is not None:
            self["columnordersrc"] = _v
        _v = arg.pop("columnwidth", None)
        _v = columnwidth if columnwidth is not None else _v
        if _v is not None:
            self["columnwidth"] = _v
        _v = arg.pop("columnwidthsrc", None)
        _v = columnwidthsrc if columnwidthsrc is not None else _v
        if _v is not None:
            self["columnwidthsrc"] = _v
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
        _v = arg.pop("header", None)
        _v = header if header is not None else _v
        if _v is not None:
            self["header"] = _v
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
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
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
        self._props["type"] = "table"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
