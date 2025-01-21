from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Rotation(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.geo.projection"
    _path_str = "layout.geo.projection.rotation"
    _valid_props = {"lat", "lon", "roll"}

    @property
    def lat(self):
        return self["lat"]

    @lat.setter
    def lat(self, val):
        self["lat"] = val

    @property
    def lon(self):
        return self["lon"]

    @lon.setter
    def lon(self, val):
        self["lon"] = val

    @property
    def roll(self):
        return self["roll"]

    @roll.setter
    def roll(self, val):
        self["roll"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, lat=None, lon=None, roll=None, **kwargs):
        super(Rotation, self).__init__("rotation")

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
The first argument to the plotly.graph_objs.layout.geo.projection.Rotation
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.geo.projection.Rotation`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("lat", None)
        _v = lat if lat is not None else _v
        if _v is not None:
            self["lat"] = _v
        _v = arg.pop("lon", None)
        _v = lon if lon is not None else _v
        if _v is not None:
            self["lon"] = _v
        _v = arg.pop("roll", None)
        _v = roll if roll is not None else _v
        if _v is not None:
            self["roll"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
