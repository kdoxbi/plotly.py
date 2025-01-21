from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Textfont(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map.layer.symbol"
    _path_str = "layout.map.layer.symbol.textfont"
    _valid_props = {"color", "family", "size", "style", "weight"}

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def family(self):
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    @property
    def size(self):
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    @property
    def style(self):
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    @property
    def weight(self):
        return self["weight"]

    @weight.setter
    def weight(self, val):
        self["weight"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        color=None,
        family=None,
        size=None,
        style=None,
        weight=None,
        **kwargs,
    ):
        super(Textfont, self).__init__("textfont")

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
The first argument to the plotly.graph_objs.layout.map.layer.symbol.Textfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.layer.symbol.Textfont`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("family", None)
        _v = family if family is not None else _v
        if _v is not None:
            self["family"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("style", None)
        _v = style if style is not None else _v
        if _v is not None:
            self["style"] = _v
        _v = arg.pop("weight", None)
        _v = weight if weight is not None else _v
        if _v is not None:
            self["weight"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
