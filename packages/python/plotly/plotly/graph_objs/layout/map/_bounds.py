from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Bounds(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map"
    _path_str = "layout.map.bounds"
    _valid_props = {"east", "north", "south", "west"}

    @property
    def east(self):
        return self["east"]

    @east.setter
    def east(self, val):
        self["east"] = val

    @property
    def north(self):
        return self["north"]

    @north.setter
    def north(self, val):
        self["north"] = val

    @property
    def south(self):
        return self["south"]

    @south.setter
    def south(self, val):
        self["south"] = val

    @property
    def west(self):
        return self["west"]

    @west.setter
    def west(self, val):
        self["west"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, east=None, north=None, south=None, west=None, **kwargs
    ):
        super(Bounds, self).__init__("bounds")

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
The first argument to the plotly.graph_objs.layout.map.Bounds
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.Bounds`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("east", None)
        _v = east if east is not None else _v
        if _v is not None:
            self["east"] = _v
        _v = arg.pop("north", None)
        _v = north if north is not None else _v
        if _v is not None:
            self["north"] = _v
        _v = arg.pop("south", None)
        _v = south if south is not None else _v
        if _v is not None:
            self["south"] = _v
        _v = arg.pop("west", None)
        _v = west if west is not None else _v
        if _v is not None:
            self["west"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
