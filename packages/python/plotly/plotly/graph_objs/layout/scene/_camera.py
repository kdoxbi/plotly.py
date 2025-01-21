from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Camera(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.scene"
    _path_str = "layout.scene.camera"
    _valid_props = {"center", "eye", "projection", "up"}

    @property
    def center(self):
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    @property
    def eye(self):
        return self["eye"]

    @eye.setter
    def eye(self, val):
        self["eye"] = val

    @property
    def projection(self):
        return self["projection"]

    @projection.setter
    def projection(self, val):
        self["projection"] = val

    @property
    def up(self):
        return self["up"]

    @up.setter
    def up(self, val):
        self["up"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, center=None, eye=None, projection=None, up=None, **kwargs
    ):
        super(Camera, self).__init__("camera")

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
The first argument to the plotly.graph_objs.layout.scene.Camera
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.scene.Camera`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("center", None)
        _v = center if center is not None else _v
        if _v is not None:
            self["center"] = _v
        _v = arg.pop("eye", None)
        _v = eye if eye is not None else _v
        if _v is not None:
            self["eye"] = _v
        _v = arg.pop("projection", None)
        _v = projection if projection is not None else _v
        if _v is not None:
            self["projection"] = _v
        _v = arg.pop("up", None)
        _v = up if up is not None else _v
        if _v is not None:
            self["up"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
