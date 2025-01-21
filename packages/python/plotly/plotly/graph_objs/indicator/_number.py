from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Number(_BaseTraceHierarchyType):

    _parent_path_str = "indicator"
    _path_str = "indicator.number"
    _valid_props = {"font", "prefix", "suffix", "valueformat"}

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def prefix(self):
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

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
        self, arg=None, font=None, prefix=None, suffix=None, valueformat=None, **kwargs
    ):
        super(Number, self).__init__("number")

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
The first argument to the plotly.graph_objs.indicator.Number
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Number`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("prefix", None)
        _v = prefix if prefix is not None else _v
        if _v is not None:
            self["prefix"] = _v
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
