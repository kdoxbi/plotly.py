from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gradient(_BaseTraceHierarchyType):

    _parent_path_str = "scatterternary.marker"
    _path_str = "scatterternary.marker.gradient"
    _valid_props = {"color", "colorsrc", "type", "typesrc"}

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
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def typesrc(self):
        return self["typesrc"]

    @typesrc.setter
    def typesrc(self, val):
        self["typesrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, color=None, colorsrc=None, type=None, typesrc=None, **kwargs
    ):
        super(Gradient, self).__init__("gradient")

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
The first argument to the plotly.graph_objs.scatterternary.marker.Gradient
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterternary.marker.Gradient`"""
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
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("typesrc", None)
        _v = typesrc if typesrc is not None else _v
        if _v is not None:
            self["typesrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
