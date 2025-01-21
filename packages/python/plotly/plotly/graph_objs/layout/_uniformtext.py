from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Uniformtext(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.uniformtext"
    _valid_props = {"minsize", "mode"}

    @property
    def minsize(self):
        return self["minsize"]

    @minsize.setter
    def minsize(self, val):
        self["minsize"] = val

    @property
    def mode(self):
        return self["mode"]

    @mode.setter
    def mode(self, val):
        self["mode"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, minsize=None, mode=None, **kwargs):
        super(Uniformtext, self).__init__("uniformtext")

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
The first argument to the plotly.graph_objs.layout.Uniformtext
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Uniformtext`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("minsize", None)
        _v = minsize if minsize is not None else _v
        if _v is not None:
            self["minsize"] = _v
        _v = arg.pop("mode", None)
        _v = mode if mode is not None else _v
        if _v is not None:
            self["mode"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
