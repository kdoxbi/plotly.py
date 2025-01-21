from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Axis(_BaseTraceHierarchyType):

    _parent_path_str = "splom.dimension"
    _path_str = "splom.dimension.axis"
    _valid_props = {"matches", "type"}

    @property
    def matches(self):
        return self["matches"]

    @matches.setter
    def matches(self, val):
        self["matches"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, matches=None, type=None, **kwargs):
        super(Axis, self).__init__("axis")

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
The first argument to the plotly.graph_objs.splom.dimension.Axis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.splom.dimension.Axis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("matches", None)
        _v = matches if matches is not None else _v
        if _v is not None:
            self["matches"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
