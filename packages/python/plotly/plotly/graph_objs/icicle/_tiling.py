from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tiling(_BaseTraceHierarchyType):

    _parent_path_str = "icicle"
    _path_str = "icicle.tiling"
    _valid_props = {"flip", "orientation", "pad"}

    @property
    def flip(self):
        return self["flip"]

    @flip.setter
    def flip(self, val):
        self["flip"] = val

    @property
    def orientation(self):
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def pad(self):
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, flip=None, orientation=None, pad=None, **kwargs):
        super(Tiling, self).__init__("tiling")

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
The first argument to the plotly.graph_objs.icicle.Tiling
constructor must be a dict or
an instance of :class:`plotly.graph_objs.icicle.Tiling`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("flip", None)
        _v = flip if flip is not None else _v
        if _v is not None:
            self["flip"] = _v
        _v = arg.pop("orientation", None)
        _v = orientation if orientation is not None else _v
        if _v is not None:
            self["orientation"] = _v
        _v = arg.pop("pad", None)
        _v = pad if pad is not None else _v
        if _v is not None:
            self["pad"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
