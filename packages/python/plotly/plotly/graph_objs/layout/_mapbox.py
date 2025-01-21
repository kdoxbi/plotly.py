from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Mapbox(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.mapbox"
    _valid_props = {
        "accesstoken",
        "bearing",
        "bounds",
        "center",
        "domain",
        "layerdefaults",
        "layers",
        "pitch",
        "style",
        "uirevision",
        "zoom",
    }

    @property
    def accesstoken(self):
        return self["accesstoken"]

    @accesstoken.setter
    def accesstoken(self, val):
        self["accesstoken"] = val

    @property
    def bearing(self):
        return self["bearing"]

    @bearing.setter
    def bearing(self, val):
        self["bearing"] = val

    @property
    def bounds(self):
        return self["bounds"]

    @bounds.setter
    def bounds(self, val):
        self["bounds"] = val

    @property
    def center(self):
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def layers(self):
        return self["layers"]

    @layers.setter
    def layers(self, val):
        self["layers"] = val

    @property
    def layerdefaults(self):
        return self["layerdefaults"]

    @layerdefaults.setter
    def layerdefaults(self, val):
        self["layerdefaults"] = val

    @property
    def pitch(self):
        return self["pitch"]

    @pitch.setter
    def pitch(self, val):
        self["pitch"] = val

    @property
    def style(self):
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def zoom(self):
        return self["zoom"]

    @zoom.setter
    def zoom(self, val):
        self["zoom"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        accesstoken=None,
        bearing=None,
        bounds=None,
        center=None,
        domain=None,
        layers=None,
        layerdefaults=None,
        pitch=None,
        style=None,
        uirevision=None,
        zoom=None,
        **kwargs,
    ):
        super(Mapbox, self).__init__("mapbox")

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
The first argument to the plotly.graph_objs.layout.Mapbox
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Mapbox`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("accesstoken", None)
        _v = accesstoken if accesstoken is not None else _v
        if _v is not None:
            self["accesstoken"] = _v
        _v = arg.pop("bearing", None)
        _v = bearing if bearing is not None else _v
        if _v is not None:
            self["bearing"] = _v
        _v = arg.pop("bounds", None)
        _v = bounds if bounds is not None else _v
        if _v is not None:
            self["bounds"] = _v
        _v = arg.pop("center", None)
        _v = center if center is not None else _v
        if _v is not None:
            self["center"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("layers", None)
        _v = layers if layers is not None else _v
        if _v is not None:
            self["layers"] = _v
        _v = arg.pop("layerdefaults", None)
        _v = layerdefaults if layerdefaults is not None else _v
        if _v is not None:
            self["layerdefaults"] = _v
        _v = arg.pop("pitch", None)
        _v = pitch if pitch is not None else _v
        if _v is not None:
            self["pitch"] = _v
        _v = arg.pop("style", None)
        _v = style if style is not None else _v
        if _v is not None:
            self["style"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("zoom", None)
        _v = zoom if zoom is not None else _v
        if _v is not None:
            self["zoom"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
