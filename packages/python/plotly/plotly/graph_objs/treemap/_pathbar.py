from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Pathbar(_BaseTraceHierarchyType):

    _parent_path_str = "treemap"
    _path_str = "treemap.pathbar"
    _valid_props = {"edgeshape", "side", "textfont", "thickness", "visible"}

    @property
    def edgeshape(self):
        return self["edgeshape"]

    @edgeshape.setter
    def edgeshape(self, val):
        self["edgeshape"] = val

    @property
    def side(self):
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    @property
    def textfont(self):
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def thickness(self):
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        edgeshape=None,
        side=None,
        textfont=None,
        thickness=None,
        visible=None,
        **kwargs,
    ):
        super(Pathbar, self).__init__("pathbar")

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
The first argument to the plotly.graph_objs.treemap.Pathbar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.treemap.Pathbar`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("edgeshape", None)
        _v = edgeshape if edgeshape is not None else _v
        if _v is not None:
            self["edgeshape"] = _v
        _v = arg.pop("side", None)
        _v = side if side is not None else _v
        if _v is not None:
            self["side"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
        _v = arg.pop("thickness", None)
        _v = thickness if thickness is not None else _v
        if _v is not None:
            self["thickness"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
