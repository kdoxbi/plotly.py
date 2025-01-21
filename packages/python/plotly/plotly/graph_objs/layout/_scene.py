from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Scene(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.scene"
    _valid_props = {
        "annotationdefaults",
        "annotations",
        "aspectmode",
        "aspectratio",
        "bgcolor",
        "camera",
        "domain",
        "dragmode",
        "hovermode",
        "uirevision",
        "xaxis",
        "yaxis",
        "zaxis",
    }

    @property
    def annotations(self):
        return self["annotations"]

    @annotations.setter
    def annotations(self, val):
        self["annotations"] = val

    @property
    def annotationdefaults(self):
        return self["annotationdefaults"]

    @annotationdefaults.setter
    def annotationdefaults(self, val):
        self["annotationdefaults"] = val

    @property
    def aspectmode(self):
        return self["aspectmode"]

    @aspectmode.setter
    def aspectmode(self, val):
        self["aspectmode"] = val

    @property
    def aspectratio(self):
        return self["aspectratio"]

    @aspectratio.setter
    def aspectratio(self, val):
        self["aspectratio"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def camera(self):
        return self["camera"]

    @camera.setter
    def camera(self, val):
        self["camera"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def dragmode(self):
        return self["dragmode"]

    @dragmode.setter
    def dragmode(self, val):
        self["dragmode"] = val

    @property
    def hovermode(self):
        return self["hovermode"]

    @hovermode.setter
    def hovermode(self, val):
        self["hovermode"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def xaxis(self):
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    @property
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def zaxis(self):
        return self["zaxis"]

    @zaxis.setter
    def zaxis(self, val):
        self["zaxis"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        annotations=None,
        annotationdefaults=None,
        aspectmode=None,
        aspectratio=None,
        bgcolor=None,
        camera=None,
        domain=None,
        dragmode=None,
        hovermode=None,
        uirevision=None,
        xaxis=None,
        yaxis=None,
        zaxis=None,
        **kwargs,
    ):
        super(Scene, self).__init__("scene")

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
The first argument to the plotly.graph_objs.layout.Scene
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Scene`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("annotations", None)
        _v = annotations if annotations is not None else _v
        if _v is not None:
            self["annotations"] = _v
        _v = arg.pop("annotationdefaults", None)
        _v = annotationdefaults if annotationdefaults is not None else _v
        if _v is not None:
            self["annotationdefaults"] = _v
        _v = arg.pop("aspectmode", None)
        _v = aspectmode if aspectmode is not None else _v
        if _v is not None:
            self["aspectmode"] = _v
        _v = arg.pop("aspectratio", None)
        _v = aspectratio if aspectratio is not None else _v
        if _v is not None:
            self["aspectratio"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("camera", None)
        _v = camera if camera is not None else _v
        if _v is not None:
            self["camera"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("dragmode", None)
        _v = dragmode if dragmode is not None else _v
        if _v is not None:
            self["dragmode"] = _v
        _v = arg.pop("hovermode", None)
        _v = hovermode if hovermode is not None else _v
        if _v is not None:
            self["hovermode"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        _v = arg.pop("zaxis", None)
        _v = zaxis if zaxis is not None else _v
        if _v is not None:
            self["zaxis"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
