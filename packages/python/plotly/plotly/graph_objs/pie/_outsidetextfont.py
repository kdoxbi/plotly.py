from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Outsidetextfont(_BaseTraceHierarchyType):

    _parent_path_str = "pie"
    _path_str = "pie.outsidetextfont"
    _valid_props = {
        "color",
        "colorsrc",
        "family",
        "familysrc",
        "lineposition",
        "linepositionsrc",
        "shadow",
        "shadowsrc",
        "size",
        "sizesrc",
        "style",
        "stylesrc",
        "textcase",
        "textcasesrc",
        "variant",
        "variantsrc",
        "weight",
        "weightsrc",
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
    def family(self):
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    @property
    def familysrc(self):
        return self["familysrc"]

    @familysrc.setter
    def familysrc(self, val):
        self["familysrc"] = val

    @property
    def lineposition(self):
        return self["lineposition"]

    @lineposition.setter
    def lineposition(self, val):
        self["lineposition"] = val

    @property
    def linepositionsrc(self):
        return self["linepositionsrc"]

    @linepositionsrc.setter
    def linepositionsrc(self, val):
        self["linepositionsrc"] = val

    @property
    def shadow(self):
        return self["shadow"]

    @shadow.setter
    def shadow(self, val):
        self["shadow"] = val

    @property
    def shadowsrc(self):
        return self["shadowsrc"]

    @shadowsrc.setter
    def shadowsrc(self, val):
        self["shadowsrc"] = val

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
    def style(self):
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    @property
    def stylesrc(self):
        return self["stylesrc"]

    @stylesrc.setter
    def stylesrc(self, val):
        self["stylesrc"] = val

    @property
    def textcase(self):
        return self["textcase"]

    @textcase.setter
    def textcase(self, val):
        self["textcase"] = val

    @property
    def textcasesrc(self):
        return self["textcasesrc"]

    @textcasesrc.setter
    def textcasesrc(self, val):
        self["textcasesrc"] = val

    @property
    def variant(self):
        return self["variant"]

    @variant.setter
    def variant(self, val):
        self["variant"] = val

    @property
    def variantsrc(self):
        return self["variantsrc"]

    @variantsrc.setter
    def variantsrc(self, val):
        self["variantsrc"] = val

    @property
    def weight(self):
        return self["weight"]

    @weight.setter
    def weight(self, val):
        self["weight"] = val

    @property
    def weightsrc(self):
        return self["weightsrc"]

    @weightsrc.setter
    def weightsrc(self, val):
        self["weightsrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        family=None,
        familysrc=None,
        lineposition=None,
        linepositionsrc=None,
        shadow=None,
        shadowsrc=None,
        size=None,
        sizesrc=None,
        style=None,
        stylesrc=None,
        textcase=None,
        textcasesrc=None,
        variant=None,
        variantsrc=None,
        weight=None,
        weightsrc=None,
        **kwargs,
    ):
        super(Outsidetextfont, self).__init__("outsidetextfont")

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
The first argument to the plotly.graph_objs.pie.Outsidetextfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.pie.Outsidetextfont`"""
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
        _v = arg.pop("family", None)
        _v = family if family is not None else _v
        if _v is not None:
            self["family"] = _v
        _v = arg.pop("familysrc", None)
        _v = familysrc if familysrc is not None else _v
        if _v is not None:
            self["familysrc"] = _v
        _v = arg.pop("lineposition", None)
        _v = lineposition if lineposition is not None else _v
        if _v is not None:
            self["lineposition"] = _v
        _v = arg.pop("linepositionsrc", None)
        _v = linepositionsrc if linepositionsrc is not None else _v
        if _v is not None:
            self["linepositionsrc"] = _v
        _v = arg.pop("shadow", None)
        _v = shadow if shadow is not None else _v
        if _v is not None:
            self["shadow"] = _v
        _v = arg.pop("shadowsrc", None)
        _v = shadowsrc if shadowsrc is not None else _v
        if _v is not None:
            self["shadowsrc"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("sizesrc", None)
        _v = sizesrc if sizesrc is not None else _v
        if _v is not None:
            self["sizesrc"] = _v
        _v = arg.pop("style", None)
        _v = style if style is not None else _v
        if _v is not None:
            self["style"] = _v
        _v = arg.pop("stylesrc", None)
        _v = stylesrc if stylesrc is not None else _v
        if _v is not None:
            self["stylesrc"] = _v
        _v = arg.pop("textcase", None)
        _v = textcase if textcase is not None else _v
        if _v is not None:
            self["textcase"] = _v
        _v = arg.pop("textcasesrc", None)
        _v = textcasesrc if textcasesrc is not None else _v
        if _v is not None:
            self["textcasesrc"] = _v
        _v = arg.pop("variant", None)
        _v = variant if variant is not None else _v
        if _v is not None:
            self["variant"] = _v
        _v = arg.pop("variantsrc", None)
        _v = variantsrc if variantsrc is not None else _v
        if _v is not None:
            self["variantsrc"] = _v
        _v = arg.pop("weight", None)
        _v = weight if weight is not None else _v
        if _v is not None:
            self["weight"] = _v
        _v = arg.pop("weightsrc", None)
        _v = weightsrc if weightsrc is not None else _v
        if _v is not None:
            self["weightsrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
