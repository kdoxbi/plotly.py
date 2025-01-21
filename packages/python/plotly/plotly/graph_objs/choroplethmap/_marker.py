from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    _parent_path_str = "choroplethmap"
    _path_str = "choroplethmap.marker"
    _valid_props = {"line", "opacity", "opacitysrc"}

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

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
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, line=None, opacity=None, opacitysrc=None, **kwargs):
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.choroplethmap.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.choroplethmap.Marker`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("opacitysrc", None)
        _v = opacitysrc if opacitysrc is not None else _v
        if _v is not None:
            self["opacitysrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
