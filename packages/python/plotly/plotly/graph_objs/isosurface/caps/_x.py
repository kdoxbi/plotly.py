from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class X(_BaseTraceHierarchyType):

    _parent_path_str = "isosurface.caps"
    _path_str = "isosurface.caps.x"
    _valid_props = {"fill", "show"}

    @property
    def fill(self):
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    @property
    def show(self):
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        super(X, self).__init__("x")

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
The first argument to the plotly.graph_objs.isosurface.caps.X
constructor must be a dict or
an instance of :class:`plotly.graph_objs.isosurface.caps.X`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("fill", None)
        _v = fill if fill is not None else _v
        if _v is not None:
            self["fill"] = _v
        _v = arg.pop("show", None)
        _v = show if show is not None else _v
        if _v is not None:
            self["show"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
