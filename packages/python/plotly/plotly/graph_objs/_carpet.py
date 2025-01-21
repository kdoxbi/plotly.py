from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Carpet(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "carpet"
    _valid_props = {
        "a",
        "a0",
        "aaxis",
        "asrc",
        "b",
        "b0",
        "baxis",
        "bsrc",
        "carpet",
        "cheaterslope",
        "color",
        "customdata",
        "customdatasrc",
        "da",
        "db",
        "font",
        "ids",
        "idssrc",
        "legend",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "stream",
        "type",
        "uid",
        "uirevision",
        "visible",
        "x",
        "xaxis",
        "xsrc",
        "y",
        "yaxis",
        "ysrc",
        "zorder",
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
    def aaxis(self):
        return self["aaxis"]

    @aaxis.setter
    def aaxis(self, val):
        self["aaxis"] = val

    @property
    def asrc(self):
        return self["asrc"]

    @asrc.setter
    def asrc(self, val):
        self["asrc"] = val

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
    def baxis(self):
        return self["baxis"]

    @baxis.setter
    def baxis(self, val):
        self["baxis"] = val

    @property
    def bsrc(self):
        return self["bsrc"]

    @bsrc.setter
    def bsrc(self, val):
        self["bsrc"] = val

    @property
    def carpet(self):
        return self["carpet"]

    @carpet.setter
    def carpet(self, val):
        self["carpet"] = val

    @property
    def cheaterslope(self):
        return self["cheaterslope"]

    @cheaterslope.setter
    def cheaterslope(self, val):
        self["cheaterslope"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

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
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

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
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

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
        a=None,
        a0=None,
        aaxis=None,
        asrc=None,
        b=None,
        b0=None,
        baxis=None,
        bsrc=None,
        carpet=None,
        cheaterslope=None,
        color=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        font=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ysrc=None,
        zorder=None,
        **kwargs,
    ):
        super(Carpet, self).__init__("carpet")

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
The first argument to the plotly.graph_objs.Carpet
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Carpet`"""
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
        _v = arg.pop("aaxis", None)
        _v = aaxis if aaxis is not None else _v
        if _v is not None:
            self["aaxis"] = _v
        _v = arg.pop("asrc", None)
        _v = asrc if asrc is not None else _v
        if _v is not None:
            self["asrc"] = _v
        _v = arg.pop("b", None)
        _v = b if b is not None else _v
        if _v is not None:
            self["b"] = _v
        _v = arg.pop("b0", None)
        _v = b0 if b0 is not None else _v
        if _v is not None:
            self["b0"] = _v
        _v = arg.pop("baxis", None)
        _v = baxis if baxis is not None else _v
        if _v is not None:
            self["baxis"] = _v
        _v = arg.pop("bsrc", None)
        _v = bsrc if bsrc is not None else _v
        if _v is not None:
            self["bsrc"] = _v
        _v = arg.pop("carpet", None)
        _v = carpet if carpet is not None else _v
        if _v is not None:
            self["carpet"] = _v
        _v = arg.pop("cheaterslope", None)
        _v = cheaterslope if cheaterslope is not None else _v
        if _v is not None:
            self["cheaterslope"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
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
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
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
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
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
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
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
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v
        _v = arg.pop("zorder", None)
        _v = zorder if zorder is not None else _v
        if _v is not None:
            self["zorder"] = _v
        self._props["type"] = "carpet"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
