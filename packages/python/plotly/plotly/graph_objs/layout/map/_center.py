from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Center(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map"
    _path_str = "layout.map.center"
    _valid_props = {"lat", "lon"}

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
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, lat=None, lon=None, **kwargs):
        super(Center, self).__init__("center")

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
The first argument to the plotly.graph_objs.layout.map.Center
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.Center`"""
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
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
