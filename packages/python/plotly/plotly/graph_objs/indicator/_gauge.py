from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gauge(_BaseTraceHierarchyType):

    _parent_path_str = "indicator"
    _path_str = "indicator.gauge"
    _valid_props = {
        "axis",
        "bar",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "shape",
        "stepdefaults",
        "steps",
        "threshold",
    }

    @property
    def axis(self):
        return self["axis"]

    @axis.setter
    def axis(self, val):
        self["axis"] = val

    @property
    def bar(self):
        return self["bar"]

    @bar.setter
    def bar(self, val):
        self["bar"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def borderwidth(self):
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    @property
    def shape(self):
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def steps(self):
        return self["steps"]

    @steps.setter
    def steps(self, val):
        self["steps"] = val

    @property
    def stepdefaults(self):
        return self["stepdefaults"]

    @stepdefaults.setter
    def stepdefaults(self, val):
        self["stepdefaults"] = val

    @property
    def threshold(self):
        return self["threshold"]

    @threshold.setter
    def threshold(self, val):
        self["threshold"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        axis=None,
        bar=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        shape=None,
        steps=None,
        stepdefaults=None,
        threshold=None,
        **kwargs,
    ):
        super(Gauge, self).__init__("gauge")

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
The first argument to the plotly.graph_objs.indicator.Gauge
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Gauge`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("axis", None)
        _v = axis if axis is not None else _v
        if _v is not None:
            self["axis"] = _v
        _v = arg.pop("bar", None)
        _v = bar if bar is not None else _v
        if _v is not None:
            self["bar"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("borderwidth", None)
        _v = borderwidth if borderwidth is not None else _v
        if _v is not None:
            self["borderwidth"] = _v
        _v = arg.pop("shape", None)
        _v = shape if shape is not None else _v
        if _v is not None:
            self["shape"] = _v
        _v = arg.pop("steps", None)
        _v = steps if steps is not None else _v
        if _v is not None:
            self["steps"] = _v
        _v = arg.pop("stepdefaults", None)
        _v = stepdefaults if stepdefaults is not None else _v
        if _v is not None:
            self["stepdefaults"] = _v
        _v = arg.pop("threshold", None)
        _v = threshold if threshold is not None else _v
        if _v is not None:
            self["threshold"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
