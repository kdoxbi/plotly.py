from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Decreasing(_BaseTraceHierarchyType):

    _parent_path_str = "ohlc"
    _path_str = "ohlc.decreasing"
    _valid_props = {"line"}

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, line=None, **kwargs):
        super(Decreasing, self).__init__("decreasing")

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
The first argument to the plotly.graph_objs.ohlc.Decreasing
constructor must be a dict or
an instance of :class:`plotly.graph_objs.ohlc.Decreasing`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
