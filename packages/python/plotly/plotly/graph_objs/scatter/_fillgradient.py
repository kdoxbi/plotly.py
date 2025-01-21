from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Fillgradient(_BaseTraceHierarchyType):

    _parent_path_str = "scatter"
    _path_str = "scatter.fillgradient"
    _valid_props = {"colorscale", "start", "stop", "type"}

    @property
    def colorscale(self):
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    @property
    def start(self):
        return self["start"]

    @start.setter
    def start(self, val):
        self["start"] = val

    @property
    def stop(self):
        return self["stop"]

    @stop.setter
    def stop(self, val):
        self["stop"] = val

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

    def __init__(
        self, arg=None, colorscale=None, start=None, stop=None, type=None, **kwargs
    ):
        super(Fillgradient, self).__init__("fillgradient")

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
The first argument to the plotly.graph_objs.scatter.Fillgradient
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter.Fillgradient`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("start", None)
        _v = start if start is not None else _v
        if _v is not None:
            self["start"] = _v
        _v = arg.pop("stop", None)
        _v = stop if stop is not None else _v
        if _v is not None:
            self["stop"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
