from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cluster(_BaseTraceHierarchyType):

    _parent_path_str = "scattermapbox"
    _path_str = "scattermapbox.cluster"
    _valid_props = {
        "color",
        "colorsrc",
        "enabled",
        "maxzoom",
        "opacity",
        "opacitysrc",
        "size",
        "sizesrc",
        "step",
        "stepsrc",
    }

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def colorsrc(self):
        return self["colorsrc"]

    @colorsrc.setter
    def colorsrc(self, val):
        self["colorsrc"] = val

    @property
    def enabled(self):
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

    @property
    def maxzoom(self):
        return self["maxzoom"]

    @maxzoom.setter
    def maxzoom(self, val):
        self["maxzoom"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def opacitysrc(self):
        return self["opacitysrc"]

    @opacitysrc.setter
    def opacitysrc(self, val):
        self["opacitysrc"] = val

    @property
    def size(self):
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    @property
    def sizesrc(self):
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    @property
    def step(self):
        return self["step"]

    @step.setter
    def step(self, val):
        self["step"] = val

    @property
    def stepsrc(self):
        return self["stepsrc"]

    @stepsrc.setter
    def stepsrc(self, val):
        self["stepsrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        enabled=None,
        maxzoom=None,
        opacity=None,
        opacitysrc=None,
        size=None,
        sizesrc=None,
        step=None,
        stepsrc=None,
        **kwargs,
    ):
        super(Cluster, self).__init__("cluster")

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
The first argument to the plotly.graph_objs.scattermapbox.Cluster
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattermapbox.Cluster`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("colorsrc", None)
        _v = colorsrc if colorsrc is not None else _v
        if _v is not None:
            self["colorsrc"] = _v
        _v = arg.pop("enabled", None)
        _v = enabled if enabled is not None else _v
        if _v is not None:
            self["enabled"] = _v
        _v = arg.pop("maxzoom", None)
        _v = maxzoom if maxzoom is not None else _v
        if _v is not None:
            self["maxzoom"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("opacitysrc", None)
        _v = opacitysrc if opacitysrc is not None else _v
        if _v is not None:
            self["opacitysrc"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("sizesrc", None)
        _v = sizesrc if sizesrc is not None else _v
        if _v is not None:
            self["sizesrc"] = _v
        _v = arg.pop("step", None)
        _v = step if step is not None else _v
        if _v is not None:
            self["step"] = _v
        _v = arg.pop("stepsrc", None)
        _v = stepsrc if stepsrc is not None else _v
        if _v is not None:
            self["stepsrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
