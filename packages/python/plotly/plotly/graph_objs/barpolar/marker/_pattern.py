from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Pattern(_BaseTraceHierarchyType):

    _parent_path_str = "barpolar.marker"
    _path_str = "barpolar.marker.pattern"
    _valid_props = {
        "bgcolor",
        "bgcolorsrc",
        "fgcolor",
        "fgcolorsrc",
        "fgopacity",
        "fillmode",
        "shape",
        "shapesrc",
        "size",
        "sizesrc",
        "solidity",
        "soliditysrc",
    }

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
    def fgcolor(self):
        return self["fgcolor"]

    @fgcolor.setter
    def fgcolor(self, val):
        self["fgcolor"] = val

    @property
    def fgcolorsrc(self):
        return self["fgcolorsrc"]

    @fgcolorsrc.setter
    def fgcolorsrc(self, val):
        self["fgcolorsrc"] = val

    @property
    def fgopacity(self):
        return self["fgopacity"]

    @fgopacity.setter
    def fgopacity(self, val):
        self["fgopacity"] = val

    @property
    def fillmode(self):
        return self["fillmode"]

    @fillmode.setter
    def fillmode(self, val):
        self["fillmode"] = val

    @property
    def shape(self):
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def shapesrc(self):
        return self["shapesrc"]

    @shapesrc.setter
    def shapesrc(self, val):
        self["shapesrc"] = val

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
    def solidity(self):
        return self["solidity"]

    @solidity.setter
    def solidity(self, val):
        self["solidity"] = val

    @property
    def soliditysrc(self):
        return self["soliditysrc"]

    @soliditysrc.setter
    def soliditysrc(self, val):
        self["soliditysrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        bgcolorsrc=None,
        fgcolor=None,
        fgcolorsrc=None,
        fgopacity=None,
        fillmode=None,
        shape=None,
        shapesrc=None,
        size=None,
        sizesrc=None,
        solidity=None,
        soliditysrc=None,
        **kwargs,
    ):
        super(Pattern, self).__init__("pattern")

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
The first argument to the plotly.graph_objs.barpolar.marker.Pattern
constructor must be a dict or
an instance of :class:`plotly.graph_objs.barpolar.marker.Pattern`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bgcolorsrc", None)
        _v = bgcolorsrc if bgcolorsrc is not None else _v
        if _v is not None:
            self["bgcolorsrc"] = _v
        _v = arg.pop("fgcolor", None)
        _v = fgcolor if fgcolor is not None else _v
        if _v is not None:
            self["fgcolor"] = _v
        _v = arg.pop("fgcolorsrc", None)
        _v = fgcolorsrc if fgcolorsrc is not None else _v
        if _v is not None:
            self["fgcolorsrc"] = _v
        _v = arg.pop("fgopacity", None)
        _v = fgopacity if fgopacity is not None else _v
        if _v is not None:
            self["fgopacity"] = _v
        _v = arg.pop("fillmode", None)
        _v = fillmode if fillmode is not None else _v
        if _v is not None:
            self["fillmode"] = _v
        _v = arg.pop("shape", None)
        _v = shape if shape is not None else _v
        if _v is not None:
            self["shape"] = _v
        _v = arg.pop("shapesrc", None)
        _v = shapesrc if shapesrc is not None else _v
        if _v is not None:
            self["shapesrc"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("sizesrc", None)
        _v = sizesrc if sizesrc is not None else _v
        if _v is not None:
            self["sizesrc"] = _v
        _v = arg.pop("solidity", None)
        _v = solidity if solidity is not None else _v
        if _v is not None:
            self["solidity"] = _v
        _v = arg.pop("soliditysrc", None)
        _v = soliditysrc if soliditysrc is not None else _v
        if _v is not None:
            self["soliditysrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
