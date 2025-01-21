from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Hoverlabel(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.hoverlabel"
    _valid_props = {
        "align",
        "bgcolor",
        "bordercolor",
        "font",
        "grouptitlefont",
        "namelength",
    }

    @property
    def align(self):
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def grouptitlefont(self):
        return self["grouptitlefont"]

    @grouptitlefont.setter
    def grouptitlefont(self, val):
        self["grouptitlefont"] = val

    @property
    def namelength(self):
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        align=None,
        bgcolor=None,
        bordercolor=None,
        font=None,
        grouptitlefont=None,
        namelength=None,
        **kwargs,
    ):
        super(Hoverlabel, self).__init__("hoverlabel")

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
The first argument to the plotly.graph_objs.layout.Hoverlabel
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Hoverlabel`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("align", None)
        _v = align if align is not None else _v
        if _v is not None:
            self["align"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("grouptitlefont", None)
        _v = grouptitlefont if grouptitlefont is not None else _v
        if _v is not None:
            self["grouptitlefont"] = _v
        _v = arg.pop("namelength", None)
        _v = namelength if namelength is not None else _v
        if _v is not None:
            self["namelength"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
