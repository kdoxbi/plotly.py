from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Ternary(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.ternary"
    _valid_props = {"aaxis", "baxis", "bgcolor", "caxis", "domain", "sum", "uirevision"}

    @property
    def aaxis(self):
        return self["aaxis"]

    @aaxis.setter
    def aaxis(self, val):
        self["aaxis"] = val

    @property
    def baxis(self):
        return self["baxis"]

    @baxis.setter
    def baxis(self, val):
        self["baxis"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def caxis(self):
        return self["caxis"]

    @caxis.setter
    def caxis(self, val):
        self["caxis"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def sum(self):
        return self["sum"]

    @sum.setter
    def sum(self, val):
        self["sum"] = val

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
        aaxis=None,
        baxis=None,
        bgcolor=None,
        caxis=None,
        domain=None,
        sum=None,
        uirevision=None,
        **kwargs,
    ):
        super(Ternary, self).__init__("ternary")

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
The first argument to the plotly.graph_objs.layout.Ternary
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Ternary`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("aaxis", None)
        _v = aaxis if aaxis is not None else _v
        if _v is not None:
            self["aaxis"] = _v
        _v = arg.pop("baxis", None)
        _v = baxis if baxis is not None else _v
        if _v is not None:
            self["baxis"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("caxis", None)
        _v = caxis if caxis is not None else _v
        if _v is not None:
            self["caxis"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("sum", None)
        _v = sum if sum is not None else _v
        if _v is not None:
            self["sum"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
