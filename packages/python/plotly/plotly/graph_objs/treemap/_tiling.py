from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tiling(_BaseTraceHierarchyType):

    _parent_path_str = "treemap"
    _path_str = "treemap.tiling"
    _valid_props = {"flip", "packing", "pad", "squarifyratio"}

    @property
    def flip(self):
        return self["flip"]

    @flip.setter
    def flip(self, val):
        self["flip"] = val

    @property
    def packing(self):
        return self["packing"]

    @packing.setter
    def packing(self, val):
        self["packing"] = val

    @property
    def pad(self):
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    @property
    def squarifyratio(self):
        return self["squarifyratio"]

    @squarifyratio.setter
    def squarifyratio(self, val):
        self["squarifyratio"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, flip=None, packing=None, pad=None, squarifyratio=None, **kwargs
    ):
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
The first argument to the plotly.graph_objs.treemap.Tiling
constructor must be a dict or
an instance of :class:`plotly.graph_objs.treemap.Tiling`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("flip", None)
        _v = flip if flip is not None else _v
        if _v is not None:
            self["flip"] = _v
        _v = arg.pop("packing", None)
        _v = packing if packing is not None else _v
        if _v is not None:
            self["packing"] = _v
        _v = arg.pop("pad", None)
        _v = pad if pad is not None else _v
        if _v is not None:
            self["pad"] = _v
        _v = arg.pop("squarifyratio", None)
        _v = squarifyratio if squarifyratio is not None else _v
        if _v is not None:
            self["squarifyratio"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
