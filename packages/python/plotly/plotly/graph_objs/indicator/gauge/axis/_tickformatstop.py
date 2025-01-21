from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tickformatstop(_BaseTraceHierarchyType):

    _parent_path_str = "indicator.gauge.axis"
    _path_str = "indicator.gauge.axis.tickformatstop"
    _valid_props = {"dtickrange", "enabled", "name", "templateitemname", "value"}

    @property
    def dtickrange(self):
        return self["dtickrange"]

    @dtickrange.setter
    def dtickrange(self, val):
        self["dtickrange"] = val

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
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

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

    def __init__(
        self,
        arg=None,
        dtickrange=None,
        enabled=None,
        name=None,
        templateitemname=None,
        value=None,
        **kwargs,
    ):
        super(Tickformatstop, self).__init__("tickformatstops")

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
The first argument to the plotly.graph_objs.indicator.gauge.axis.Tickformatstop
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.gauge.axis.Tickformatstop`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("dtickrange", None)
        _v = dtickrange if dtickrange is not None else _v
        if _v is not None:
            self["dtickrange"] = _v
        _v = arg.pop("enabled", None)
        _v = enabled if enabled is not None else _v
        if _v is not None:
            self["enabled"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
