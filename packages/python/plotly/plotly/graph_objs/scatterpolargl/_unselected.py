from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Unselected(_BaseTraceHierarchyType):

    _parent_path_str = "scatterpolargl"
    _path_str = "scatterpolargl.unselected"
    _valid_props = {"marker", "textfont"}

    @property
    def marker(self):
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def textfont(self):
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, marker=None, textfont=None, **kwargs):
        super(Unselected, self).__init__("unselected")

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
The first argument to the plotly.graph_objs.scatterpolargl.Unselected
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterpolargl.Unselected`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("marker", None)
        _v = marker if marker is not None else _v
        if _v is not None:
            self["marker"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
