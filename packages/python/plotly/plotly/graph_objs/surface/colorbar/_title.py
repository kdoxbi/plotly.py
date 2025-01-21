from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Title(_BaseTraceHierarchyType):

    _parent_path_str = "surface.colorbar"
    _path_str = "surface.colorbar.title"
    _valid_props = {"font", "side", "text"}

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def side(self):
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, font=None, side=None, text=None, **kwargs):
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.surface.colorbar.Title
constructor must be a dict or
an instance of :class:`plotly.graph_objs.surface.colorbar.Title`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("side", None)
        _v = side if side is not None else _v
        if _v is not None:
            self["side"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
