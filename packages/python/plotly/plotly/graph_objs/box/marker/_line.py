from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    _parent_path_str = "box.marker"
    _path_str = "box.marker.line"
    _valid_props = {"color", "outliercolor", "outlierwidth", "width"}

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def outliercolor(self):
        return self["outliercolor"]

    @outliercolor.setter
    def outliercolor(self, val):
        self["outliercolor"] = val

    @property
    def outlierwidth(self):
        return self["outlierwidth"]

    @outlierwidth.setter
    def outlierwidth(self, val):
        self["outlierwidth"] = val

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
        color=None,
        outliercolor=None,
        outlierwidth=None,
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
The first argument to the plotly.graph_objs.box.marker.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.box.marker.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("outliercolor", None)
        _v = outliercolor if outliercolor is not None else _v
        if _v is not None:
            self["outliercolor"] = _v
        _v = arg.pop("outlierwidth", None)
        _v = outlierwidth if outlierwidth is not None else _v
        if _v is not None:
            self["outlierwidth"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
