from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Autorangeoptions(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.yaxis"
    _path_str = "layout.yaxis.autorangeoptions"
    _valid_props = {
        "clipmax",
        "clipmin",
        "include",
        "includesrc",
        "maxallowed",
        "minallowed",
    }

    @property
    def clipmax(self):
        return self["clipmax"]

    @clipmax.setter
    def clipmax(self, val):
        self["clipmax"] = val

    @property
    def clipmin(self):
        return self["clipmin"]

    @clipmin.setter
    def clipmin(self, val):
        self["clipmin"] = val

    @property
    def include(self):
        return self["include"]

    @include.setter
    def include(self, val):
        self["include"] = val

    @property
    def includesrc(self):
        return self["includesrc"]

    @includesrc.setter
    def includesrc(self, val):
        self["includesrc"] = val

    @property
    def maxallowed(self):
        return self["maxallowed"]

    @maxallowed.setter
    def maxallowed(self, val):
        self["maxallowed"] = val

    @property
    def minallowed(self):
        return self["minallowed"]

    @minallowed.setter
    def minallowed(self, val):
        self["minallowed"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        clipmax=None,
        clipmin=None,
        include=None,
        includesrc=None,
        maxallowed=None,
        minallowed=None,
        **kwargs,
    ):
        super(Autorangeoptions, self).__init__("autorangeoptions")

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
The first argument to the plotly.graph_objs.layout.yaxis.Autorangeoptions
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.yaxis.Autorangeoptions`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("clipmax", None)
        _v = clipmax if clipmax is not None else _v
        if _v is not None:
            self["clipmax"] = _v
        _v = arg.pop("clipmin", None)
        _v = clipmin if clipmin is not None else _v
        if _v is not None:
            self["clipmin"] = _v
        _v = arg.pop("include", None)
        _v = include if include is not None else _v
        if _v is not None:
            self["include"] = _v
        _v = arg.pop("includesrc", None)
        _v = includesrc if includesrc is not None else _v
        if _v is not None:
            self["includesrc"] = _v
        _v = arg.pop("maxallowed", None)
        _v = maxallowed if maxallowed is not None else _v
        if _v is not None:
            self["maxallowed"] = _v
        _v = arg.pop("minallowed", None)
        _v = minallowed if minallowed is not None else _v
        if _v is not None:
            self["minallowed"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
