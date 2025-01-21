from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Projection(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.geo"
    _path_str = "layout.geo.projection"
    _valid_props = {"distance", "parallels", "rotation", "scale", "tilt", "type"}

    @property
    def distance(self):
        return self["distance"]

    @distance.setter
    def distance(self, val):
        self["distance"] = val

    @property
    def parallels(self):
        return self["parallels"]

    @parallels.setter
    def parallels(self, val):
        self["parallels"] = val

    @property
    def rotation(self):
        return self["rotation"]

    @rotation.setter
    def rotation(self, val):
        self["rotation"] = val

    @property
    def scale(self):
        return self["scale"]

    @scale.setter
    def scale(self, val):
        self["scale"] = val

    @property
    def tilt(self):
        return self["tilt"]

    @tilt.setter
    def tilt(self, val):
        self["tilt"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        distance=None,
        parallels=None,
        rotation=None,
        scale=None,
        tilt=None,
        type=None,
        **kwargs,
    ):
        super(Projection, self).__init__("projection")

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
The first argument to the plotly.graph_objs.layout.geo.Projection
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.geo.Projection`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("distance", None)
        _v = distance if distance is not None else _v
        if _v is not None:
            self["distance"] = _v
        _v = arg.pop("parallels", None)
        _v = parallels if parallels is not None else _v
        if _v is not None:
            self["parallels"] = _v
        _v = arg.pop("rotation", None)
        _v = rotation if rotation is not None else _v
        if _v is not None:
            self["rotation"] = _v
        _v = arg.pop("scale", None)
        _v = scale if scale is not None else _v
        if _v is not None:
            self["scale"] = _v
        _v = arg.pop("tilt", None)
        _v = tilt if tilt is not None else _v
        if _v is not None:
            self["tilt"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
