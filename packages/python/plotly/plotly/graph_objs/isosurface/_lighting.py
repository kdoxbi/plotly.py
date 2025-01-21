from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Lighting(_BaseTraceHierarchyType):

    _parent_path_str = "isosurface"
    _path_str = "isosurface.lighting"
    _valid_props = {
        "ambient",
        "diffuse",
        "facenormalsepsilon",
        "fresnel",
        "roughness",
        "specular",
        "vertexnormalsepsilon",
    }

    @property
    def ambient(self):
        return self["ambient"]

    @ambient.setter
    def ambient(self, val):
        self["ambient"] = val

    @property
    def diffuse(self):
        return self["diffuse"]

    @diffuse.setter
    def diffuse(self, val):
        self["diffuse"] = val

    @property
    def facenormalsepsilon(self):
        return self["facenormalsepsilon"]

    @facenormalsepsilon.setter
    def facenormalsepsilon(self, val):
        self["facenormalsepsilon"] = val

    @property
    def fresnel(self):
        return self["fresnel"]

    @fresnel.setter
    def fresnel(self, val):
        self["fresnel"] = val

    @property
    def roughness(self):
        return self["roughness"]

    @roughness.setter
    def roughness(self, val):
        self["roughness"] = val

    @property
    def specular(self):
        return self["specular"]

    @specular.setter
    def specular(self, val):
        self["specular"] = val

    @property
    def vertexnormalsepsilon(self):
        return self["vertexnormalsepsilon"]

    @vertexnormalsepsilon.setter
    def vertexnormalsepsilon(self, val):
        self["vertexnormalsepsilon"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        ambient=None,
        diffuse=None,
        facenormalsepsilon=None,
        fresnel=None,
        roughness=None,
        specular=None,
        vertexnormalsepsilon=None,
        **kwargs,
    ):
        super(Lighting, self).__init__("lighting")

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
The first argument to the plotly.graph_objs.isosurface.Lighting
constructor must be a dict or
an instance of :class:`plotly.graph_objs.isosurface.Lighting`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("ambient", None)
        _v = ambient if ambient is not None else _v
        if _v is not None:
            self["ambient"] = _v
        _v = arg.pop("diffuse", None)
        _v = diffuse if diffuse is not None else _v
        if _v is not None:
            self["diffuse"] = _v
        _v = arg.pop("facenormalsepsilon", None)
        _v = facenormalsepsilon if facenormalsepsilon is not None else _v
        if _v is not None:
            self["facenormalsepsilon"] = _v
        _v = arg.pop("fresnel", None)
        _v = fresnel if fresnel is not None else _v
        if _v is not None:
            self["fresnel"] = _v
        _v = arg.pop("roughness", None)
        _v = roughness if roughness is not None else _v
        if _v is not None:
            self["roughness"] = _v
        _v = arg.pop("specular", None)
        _v = specular if specular is not None else _v
        if _v is not None:
            self["specular"] = _v
        _v = arg.pop("vertexnormalsepsilon", None)
        _v = vertexnormalsepsilon if vertexnormalsepsilon is not None else _v
        if _v is not None:
            self["vertexnormalsepsilon"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
