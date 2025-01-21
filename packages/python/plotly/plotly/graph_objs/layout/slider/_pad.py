from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Pad(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.slider"
    _path_str = "layout.slider.pad"
    _valid_props = {"b", "l", "r", "t"}

    @property
    def b(self):
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

    @property
    def l(self):
        return self["l"]

    @l.setter
    def l(self, val):
        self["l"] = val

    @property
    def r(self):
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

    @property
    def t(self):
        return self["t"]

    @t.setter
    def t(self, val):
        self["t"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, b=None, l=None, r=None, t=None, **kwargs):
        super(Pad, self).__init__("pad")

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
The first argument to the plotly.graph_objs.layout.slider.Pad
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Pad`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("b", None)
        _v = b if b is not None else _v
        if _v is not None:
            self["b"] = _v
        _v = arg.pop("l", None)
        _v = l if l is not None else _v
        if _v is not None:
            self["l"] = _v
        _v = arg.pop("r", None)
        _v = r if r is not None else _v
        if _v is not None:
            self["r"] = _v
        _v = arg.pop("t", None)
        _v = t if t is not None else _v
        if _v is not None:
            self["t"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
