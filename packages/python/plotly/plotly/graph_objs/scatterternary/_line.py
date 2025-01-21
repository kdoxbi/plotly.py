from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    _parent_path_str = "scatterternary"
    _path_str = "scatterternary.line"
    _valid_props = {
        "backoff",
        "backoffsrc",
        "color",
        "dash",
        "shape",
        "smoothing",
        "width",
    }

    @property
    def backoff(self):
        return self["backoff"]

    @backoff.setter
    def backoff(self, val):
        self["backoff"] = val

    @property
    def backoffsrc(self):
        return self["backoffsrc"]

    @backoffsrc.setter
    def backoffsrc(self, val):
        self["backoffsrc"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def dash(self):
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    @property
    def shape(self):
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def smoothing(self):
        return self["smoothing"]

    @smoothing.setter
    def smoothing(self, val):
        self["smoothing"] = val

    @property
    def width(self):
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        backoff=None,
        backoffsrc=None,
        color=None,
        dash=None,
        shape=None,
        smoothing=None,
        width=None,
        **kwargs,
    ):
        super(Line, self).__init__("line")

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
The first argument to the plotly.graph_objs.scatterternary.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterternary.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("backoff", None)
        _v = backoff if backoff is not None else _v
        if _v is not None:
            self["backoff"] = _v
        _v = arg.pop("backoffsrc", None)
        _v = backoffsrc if backoffsrc is not None else _v
        if _v is not None:
            self["backoffsrc"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("dash", None)
        _v = dash if dash is not None else _v
        if _v is not None:
            self["dash"] = _v
        _v = arg.pop("shape", None)
        _v = shape if shape is not None else _v
        if _v is not None:
            self["shape"] = _v
        _v = arg.pop("smoothing", None)
        _v = smoothing if smoothing is not None else _v
        if _v is not None:
            self["smoothing"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
