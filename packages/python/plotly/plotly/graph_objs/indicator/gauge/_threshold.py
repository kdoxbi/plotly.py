from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Threshold(_BaseTraceHierarchyType):

    _parent_path_str = "indicator.gauge"
    _path_str = "indicator.gauge.threshold"
    _valid_props = {"line", "thickness", "value"}

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def thickness(self):
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    @property
    def value(self):
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, line=None, thickness=None, value=None, **kwargs):
        super(Threshold, self).__init__("threshold")

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
The first argument to the plotly.graph_objs.indicator.gauge.Threshold
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.gauge.Threshold`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("thickness", None)
        _v = thickness if thickness is not None else _v
        if _v is not None:
            self["thickness"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
