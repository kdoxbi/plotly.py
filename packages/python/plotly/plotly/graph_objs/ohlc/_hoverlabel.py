from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Hoverlabel(_BaseTraceHierarchyType):

    _parent_path_str = "ohlc"
    _path_str = "ohlc.hoverlabel"
    _valid_props = {
        "align",
        "alignsrc",
        "bgcolor",
        "bgcolorsrc",
        "bordercolor",
        "bordercolorsrc",
        "font",
        "namelength",
        "namelengthsrc",
        "split",
    }

    @property
    def align(self):
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    @property
    def alignsrc(self):
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bgcolorsrc(self):
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def bordercolorsrc(self):
        return self["bordercolorsrc"]

    @bordercolorsrc.setter
    def bordercolorsrc(self, val):
        self["bordercolorsrc"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def namelength(self):
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    @property
    def namelengthsrc(self):
        return self["namelengthsrc"]

    @namelengthsrc.setter
    def namelengthsrc(self, val):
        self["namelengthsrc"] = val

    @property
    def split(self):
        return self["split"]

    @split.setter
    def split(self, val):
        self["split"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        bgcolor=None,
        bgcolorsrc=None,
        bordercolor=None,
        bordercolorsrc=None,
        font=None,
        namelength=None,
        namelengthsrc=None,
        split=None,
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
The first argument to the plotly.graph_objs.ohlc.Hoverlabel
constructor must be a dict or
an instance of :class:`plotly.graph_objs.ohlc.Hoverlabel`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("align", None)
        _v = align if align is not None else _v
        if _v is not None:
            self["align"] = _v
        _v = arg.pop("alignsrc", None)
        _v = alignsrc if alignsrc is not None else _v
        if _v is not None:
            self["alignsrc"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bgcolorsrc", None)
        _v = bgcolorsrc if bgcolorsrc is not None else _v
        if _v is not None:
            self["bgcolorsrc"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("bordercolorsrc", None)
        _v = bordercolorsrc if bordercolorsrc is not None else _v
        if _v is not None:
            self["bordercolorsrc"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("namelength", None)
        _v = namelength if namelength is not None else _v
        if _v is not None:
            self["namelength"] = _v
        _v = arg.pop("namelengthsrc", None)
        _v = namelengthsrc if namelengthsrc is not None else _v
        if _v is not None:
            self["namelengthsrc"] = _v
        _v = arg.pop("split", None)
        _v = split if split is not None else _v
        if _v is not None:
            self["split"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
