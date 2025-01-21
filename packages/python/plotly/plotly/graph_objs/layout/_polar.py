from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Polar(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.polar"
    _valid_props = {
        "angularaxis",
        "bargap",
        "barmode",
        "bgcolor",
        "domain",
        "gridshape",
        "hole",
        "radialaxis",
        "sector",
        "uirevision",
    }

    @property
    def angularaxis(self):
        return self["angularaxis"]

    @angularaxis.setter
    def angularaxis(self, val):
        self["angularaxis"] = val

    @property
    def bargap(self):
        return self["bargap"]

    @bargap.setter
    def bargap(self, val):
        self["bargap"] = val

    @property
    def barmode(self):
        return self["barmode"]

    @barmode.setter
    def barmode(self, val):
        self["barmode"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def gridshape(self):
        return self["gridshape"]

    @gridshape.setter
    def gridshape(self, val):
        self["gridshape"] = val

    @property
    def hole(self):
        return self["hole"]

    @hole.setter
    def hole(self, val):
        self["hole"] = val

    @property
    def radialaxis(self):
        return self["radialaxis"]

    @radialaxis.setter
    def radialaxis(self, val):
        self["radialaxis"] = val

    @property
    def sector(self):
        return self["sector"]

    @sector.setter
    def sector(self, val):
        self["sector"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        angularaxis=None,
        bargap=None,
        barmode=None,
        bgcolor=None,
        domain=None,
        gridshape=None,
        hole=None,
        radialaxis=None,
        sector=None,
        uirevision=None,
        **kwargs,
    ):
        super(Polar, self).__init__("polar")

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
The first argument to the plotly.graph_objs.layout.Polar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Polar`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("angularaxis", None)
        _v = angularaxis if angularaxis is not None else _v
        if _v is not None:
            self["angularaxis"] = _v
        _v = arg.pop("bargap", None)
        _v = bargap if bargap is not None else _v
        if _v is not None:
            self["bargap"] = _v
        _v = arg.pop("barmode", None)
        _v = barmode if barmode is not None else _v
        if _v is not None:
            self["barmode"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("gridshape", None)
        _v = gridshape if gridshape is not None else _v
        if _v is not None:
            self["gridshape"] = _v
        _v = arg.pop("hole", None)
        _v = hole if hole is not None else _v
        if _v is not None:
            self["hole"] = _v
        _v = arg.pop("radialaxis", None)
        _v = radialaxis if radialaxis is not None else _v
        if _v is not None:
            self["radialaxis"] = _v
        _v = arg.pop("sector", None)
        _v = sector if sector is not None else _v
        if _v is not None:
            self["sector"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
