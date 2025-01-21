from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Delta(_BaseTraceHierarchyType):

    _parent_path_str = "indicator"
    _path_str = "indicator.delta"
    _valid_props = {
        "decreasing",
        "font",
        "increasing",
        "position",
        "prefix",
        "reference",
        "relative",
        "suffix",
        "valueformat",
    }

    @property
    def decreasing(self):
        return self["decreasing"]

    @decreasing.setter
    def decreasing(self, val):
        self["decreasing"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def increasing(self):
        return self["increasing"]

    @increasing.setter
    def increasing(self, val):
        self["increasing"] = val

    @property
    def position(self):
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

    @property
    def prefix(self):
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    @property
    def reference(self):
        return self["reference"]

    @reference.setter
    def reference(self, val):
        self["reference"] = val

    @property
    def relative(self):
        return self["relative"]

    @relative.setter
    def relative(self, val):
        self["relative"] = val

    @property
    def suffix(self):
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    @property
    def valueformat(self):
        return self["valueformat"]

    @valueformat.setter
    def valueformat(self, val):
        self["valueformat"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        decreasing=None,
        font=None,
        increasing=None,
        position=None,
        prefix=None,
        reference=None,
        relative=None,
        suffix=None,
        valueformat=None,
        **kwargs,
    ):
        super(Delta, self).__init__("delta")

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
The first argument to the plotly.graph_objs.indicator.Delta
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Delta`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("decreasing", None)
        _v = decreasing if decreasing is not None else _v
        if _v is not None:
            self["decreasing"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("increasing", None)
        _v = increasing if increasing is not None else _v
        if _v is not None:
            self["increasing"] = _v
        _v = arg.pop("position", None)
        _v = position if position is not None else _v
        if _v is not None:
            self["position"] = _v
        _v = arg.pop("prefix", None)
        _v = prefix if prefix is not None else _v
        if _v is not None:
            self["prefix"] = _v
        _v = arg.pop("reference", None)
        _v = reference if reference is not None else _v
        if _v is not None:
            self["reference"] = _v
        _v = arg.pop("relative", None)
        _v = relative if relative is not None else _v
        if _v is not None:
            self["relative"] = _v
        _v = arg.pop("suffix", None)
        _v = suffix if suffix is not None else _v
        if _v is not None:
            self["suffix"] = _v
        _v = arg.pop("valueformat", None)
        _v = valueformat if valueformat is not None else _v
        if _v is not None:
            self["valueformat"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
