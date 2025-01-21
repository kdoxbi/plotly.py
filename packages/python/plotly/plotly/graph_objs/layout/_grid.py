from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Grid(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.grid"
    _valid_props = {
        "columns",
        "domain",
        "pattern",
        "roworder",
        "rows",
        "subplots",
        "xaxes",
        "xgap",
        "xside",
        "yaxes",
        "ygap",
        "yside",
    }

    @property
    def columns(self):
        return self["columns"]

    @columns.setter
    def columns(self, val):
        self["columns"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def pattern(self):
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

    @property
    def roworder(self):
        return self["roworder"]

    @roworder.setter
    def roworder(self, val):
        self["roworder"] = val

    @property
    def rows(self):
        return self["rows"]

    @rows.setter
    def rows(self, val):
        self["rows"] = val

    @property
    def subplots(self):
        return self["subplots"]

    @subplots.setter
    def subplots(self, val):
        self["subplots"] = val

    @property
    def xaxes(self):
        return self["xaxes"]

    @xaxes.setter
    def xaxes(self, val):
        self["xaxes"] = val

    @property
    def xgap(self):
        return self["xgap"]

    @xgap.setter
    def xgap(self, val):
        self["xgap"] = val

    @property
    def xside(self):
        return self["xside"]

    @xside.setter
    def xside(self, val):
        self["xside"] = val

    @property
    def yaxes(self):
        return self["yaxes"]

    @yaxes.setter
    def yaxes(self, val):
        self["yaxes"] = val

    @property
    def ygap(self):
        return self["ygap"]

    @ygap.setter
    def ygap(self, val):
        self["ygap"] = val

    @property
    def yside(self):
        return self["yside"]

    @yside.setter
    def yside(self, val):
        self["yside"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        columns=None,
        domain=None,
        pattern=None,
        roworder=None,
        rows=None,
        subplots=None,
        xaxes=None,
        xgap=None,
        xside=None,
        yaxes=None,
        ygap=None,
        yside=None,
        **kwargs,
    ):
        super(Grid, self).__init__("grid")

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
The first argument to the plotly.graph_objs.layout.Grid
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Grid`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("columns", None)
        _v = columns if columns is not None else _v
        if _v is not None:
            self["columns"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("pattern", None)
        _v = pattern if pattern is not None else _v
        if _v is not None:
            self["pattern"] = _v
        _v = arg.pop("roworder", None)
        _v = roworder if roworder is not None else _v
        if _v is not None:
            self["roworder"] = _v
        _v = arg.pop("rows", None)
        _v = rows if rows is not None else _v
        if _v is not None:
            self["rows"] = _v
        _v = arg.pop("subplots", None)
        _v = subplots if subplots is not None else _v
        if _v is not None:
            self["subplots"] = _v
        _v = arg.pop("xaxes", None)
        _v = xaxes if xaxes is not None else _v
        if _v is not None:
            self["xaxes"] = _v
        _v = arg.pop("xgap", None)
        _v = xgap if xgap is not None else _v
        if _v is not None:
            self["xgap"] = _v
        _v = arg.pop("xside", None)
        _v = xside if xside is not None else _v
        if _v is not None:
            self["xside"] = _v
        _v = arg.pop("yaxes", None)
        _v = yaxes if yaxes is not None else _v
        if _v is not None:
            self["yaxes"] = _v
        _v = arg.pop("ygap", None)
        _v = ygap if ygap is not None else _v
        if _v is not None:
            self["ygap"] = _v
        _v = arg.pop("yside", None)
        _v = yside if yside is not None else _v
        if _v is not None:
            self["yside"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
