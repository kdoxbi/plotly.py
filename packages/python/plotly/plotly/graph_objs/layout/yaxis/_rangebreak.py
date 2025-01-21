from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Rangebreak(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.yaxis"
    _path_str = "layout.yaxis.rangebreak"
    _valid_props = {
        "bounds",
        "dvalue",
        "enabled",
        "name",
        "pattern",
        "templateitemname",
        "values",
    }

    @property
    def bounds(self):
        return self["bounds"]

    @bounds.setter
    def bounds(self, val):
        self["bounds"] = val

    @property
    def dvalue(self):
        return self["dvalue"]

    @dvalue.setter
    def dvalue(self, val):
        self["dvalue"] = val

    @property
    def enabled(self):
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def pattern(self):
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def values(self):
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        bounds=None,
        dvalue=None,
        enabled=None,
        name=None,
        pattern=None,
        templateitemname=None,
        values=None,
        **kwargs,
    ):
        super(Rangebreak, self).__init__("rangebreaks")

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
The first argument to the plotly.graph_objs.layout.yaxis.Rangebreak
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.yaxis.Rangebreak`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("bounds", None)
        _v = bounds if bounds is not None else _v
        if _v is not None:
            self["bounds"] = _v
        _v = arg.pop("dvalue", None)
        _v = dvalue if dvalue is not None else _v
        if _v is not None:
            self["dvalue"] = _v
        _v = arg.pop("enabled", None)
        _v = enabled if enabled is not None else _v
        if _v is not None:
            self["enabled"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("pattern", None)
        _v = pattern if pattern is not None else _v
        if _v is not None:
            self["pattern"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("values", None)
        _v = values if values is not None else _v
        if _v is not None:
            self["values"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
