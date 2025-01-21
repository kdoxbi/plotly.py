from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Symbol(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map.layer"
    _path_str = "layout.map.layer.symbol"
    _valid_props = {"icon", "iconsize", "placement", "text", "textfont", "textposition"}

    @property
    def icon(self):
        return self["icon"]

    @icon.setter
    def icon(self, val):
        self["icon"] = val

    @property
    def iconsize(self):
        return self["iconsize"]

    @iconsize.setter
    def iconsize(self, val):
        self["iconsize"] = val

    @property
    def placement(self):
        return self["placement"]

    @placement.setter
    def placement(self, val):
        self["placement"] = val

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textfont(self):
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def textposition(self):
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        icon=None,
        iconsize=None,
        placement=None,
        text=None,
        textfont=None,
        textposition=None,
        **kwargs,
    ):
        super(Symbol, self).__init__("symbol")

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
The first argument to the plotly.graph_objs.layout.map.layer.Symbol
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.layer.Symbol`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("icon", None)
        _v = icon if icon is not None else _v
        if _v is not None:
            self["icon"] = _v
        _v = arg.pop("iconsize", None)
        _v = iconsize if iconsize is not None else _v
        if _v is not None:
            self["iconsize"] = _v
        _v = arg.pop("placement", None)
        _v = placement if placement is not None else _v
        if _v is not None:
            self["placement"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textfont", None)
        _v = textfont if textfont is not None else _v
        if _v is not None:
            self["textfont"] = _v
        _v = arg.pop("textposition", None)
        _v = textposition if textposition is not None else _v
        if _v is not None:
            self["textposition"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
