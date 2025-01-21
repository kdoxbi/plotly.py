from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Line(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.mapbox.layer"
    _path_str = "layout.mapbox.layer.line"
    _valid_props = {"dash", "dashsrc", "width"}

    @property
    def dash(self):
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    @property
    def dashsrc(self):
        return self["dashsrc"]

    @dashsrc.setter
    def dashsrc(self, val):
        self["dashsrc"] = val

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

    def __init__(self, arg=None, dash=None, dashsrc=None, width=None, **kwargs):
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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.mapbox.layer.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("dash", None)
        _v = dash if dash is not None else _v
        if _v is not None:
            self["dash"] = _v
        _v = arg.pop("dashsrc", None)
        _v = dashsrc if dashsrc is not None else _v
        if _v is not None:
            self["dashsrc"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
