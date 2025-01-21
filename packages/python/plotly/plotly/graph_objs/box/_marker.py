from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    _parent_path_str = "box"
    _path_str = "box.marker"
    _valid_props = {
        "angle",
        "color",
        "line",
        "opacity",
        "outliercolor",
        "size",
        "symbol",
    }

    @property
    def angle(self):
        return self["angle"]

    @angle.setter
    def angle(self, val):
        self["angle"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def outliercolor(self):
        return self["outliercolor"]

    @outliercolor.setter
    def outliercolor(self, val):
        self["outliercolor"] = val

    @property
    def size(self):
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    @property
    def symbol(self):
        return self["symbol"]

    @symbol.setter
    def symbol(self, val):
        self["symbol"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        angle=None,
        color=None,
        line=None,
        opacity=None,
        outliercolor=None,
        size=None,
        symbol=None,
        **kwargs,
    ):
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.box.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.box.Marker`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("angle", None)
        _v = angle if angle is not None else _v
        if _v is not None:
            self["angle"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("outliercolor", None)
        _v = outliercolor if outliercolor is not None else _v
        if _v is not None:
            self["outliercolor"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("symbol", None)
        _v = symbol if symbol is not None else _v
        if _v is not None:
            self["symbol"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
