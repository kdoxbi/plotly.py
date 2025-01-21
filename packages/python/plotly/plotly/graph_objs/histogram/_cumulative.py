from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cumulative(_BaseTraceHierarchyType):

    _parent_path_str = "histogram"
    _path_str = "histogram.cumulative"
    _valid_props = {"currentbin", "direction", "enabled"}

    @property
    def currentbin(self):
        return self["currentbin"]

    @currentbin.setter
    def currentbin(self, val):
        self["currentbin"] = val

    @property
    def direction(self):
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    @property
    def enabled(self):
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, currentbin=None, direction=None, enabled=None, **kwargs
    ):
        super(Cumulative, self).__init__("cumulative")

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
The first argument to the plotly.graph_objs.histogram.Cumulative
constructor must be a dict or
an instance of :class:`plotly.graph_objs.histogram.Cumulative`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("currentbin", None)
        _v = currentbin if currentbin is not None else _v
        if _v is not None:
            self["currentbin"] = _v
        _v = arg.pop("direction", None)
        _v = direction if direction is not None else _v
        if _v is not None:
            self["direction"] = _v
        _v = arg.pop("enabled", None)
        _v = enabled if enabled is not None else _v
        if _v is not None:
            self["enabled"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
