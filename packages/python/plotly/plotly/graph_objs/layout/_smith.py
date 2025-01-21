from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Smith(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.smith"
    _valid_props = {"bgcolor", "domain", "imaginaryaxis", "realaxis"}

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
    def imaginaryaxis(self):
        return self["imaginaryaxis"]

    @imaginaryaxis.setter
    def imaginaryaxis(self, val):
        self["imaginaryaxis"] = val

    @property
    def realaxis(self):
        return self["realaxis"]

    @realaxis.setter
    def realaxis(self, val):
        self["realaxis"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        domain=None,
        imaginaryaxis=None,
        realaxis=None,
        **kwargs,
    ):
        super(Smith, self).__init__("smith")

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
The first argument to the plotly.graph_objs.layout.Smith
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Smith`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("imaginaryaxis", None)
        _v = imaginaryaxis if imaginaryaxis is not None else _v
        if _v is not None:
            self["imaginaryaxis"] = _v
        _v = arg.pop("realaxis", None)
        _v = realaxis if realaxis is not None else _v
        if _v is not None:
            self["realaxis"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
