from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    _parent_path_str = "choroplethmapbox.unselected"
    _path_str = "choroplethmapbox.unselected.marker"
    _valid_props = {"opacity"}

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, opacity=None, **kwargs):
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
The first argument to the plotly.graph_objs.choroplethmapbox.unselected.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.choroplethmapbox.unselected.Marker`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
