from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Selection(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.selection"
    _valid_props = {
        "line",
        "name",
        "opacity",
        "path",
        "templateitemname",
        "type",
        "x0",
        "x1",
        "xref",
        "y0",
        "y1",
        "yref",
    }

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

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
    def path(self):
        return self["path"]

    @path.setter
    def path(self, val):
        self["path"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def x0(self):
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    @property
    def x1(self):
        return self["x1"]

    @x1.setter
    def x1(self, val):
        self["x1"] = val

    @property
    def xref(self):
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    @property
    def y0(self):
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    @property
    def y1(self):
        return self["y1"]

    @y1.setter
    def y1(self, val):
        self["y1"] = val

    @property
    def yref(self):
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        templateitemname=None,
        type=None,
        x0=None,
        x1=None,
        xref=None,
        y0=None,
        y1=None,
        yref=None,
        **kwargs,
    ):
        super(Selection, self).__init__("selections")

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
The first argument to the plotly.graph_objs.layout.Selection
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Selection`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("path", None)
        _v = path if path is not None else _v
        if _v is not None:
            self["path"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("x0", None)
        _v = x0 if x0 is not None else _v
        if _v is not None:
            self["x0"] = _v
        _v = arg.pop("x1", None)
        _v = x1 if x1 is not None else _v
        if _v is not None:
            self["x1"] = _v
        _v = arg.pop("xref", None)
        _v = xref if xref is not None else _v
        if _v is not None:
            self["xref"] = _v
        _v = arg.pop("y0", None)
        _v = y0 if y0 is not None else _v
        if _v is not None:
            self["y0"] = _v
        _v = arg.pop("y1", None)
        _v = y1 if y1 is not None else _v
        if _v is not None:
            self["y1"] = _v
        _v = arg.pop("yref", None)
        _v = yref if yref is not None else _v
        if _v is not None:
            self["yref"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
