from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Domain(_BaseTraceHierarchyType):

    _parent_path_str = "indicator"
    _path_str = "indicator.domain"
    _valid_props = {"column", "row", "x", "y"}

    @property
    def column(self):
        return self["column"]

    @column.setter
    def column(self, val):
        self["column"] = val

    @property
    def row(self):
        return self["row"]

    @row.setter
    def row(self, val):
        self["row"] = val

    @property
    def x(self):
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def y(self):
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        super(Domain, self).__init__("domain")

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
The first argument to the plotly.graph_objs.indicator.Domain
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Domain`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("column", None)
        _v = column if column is not None else _v
        if _v is not None:
            self["column"] = _v
        _v = arg.pop("row", None)
        _v = row if row is not None else _v
        if _v is not None:
            self["row"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
