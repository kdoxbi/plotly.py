from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Colorscale(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.colorscale"
    _valid_props = {"diverging", "sequential", "sequentialminus"}

    @property
    def diverging(self):
        return self["diverging"]

    @diverging.setter
    def diverging(self, val):
        self["diverging"] = val

    @property
    def sequential(self):
        return self["sequential"]

    @sequential.setter
    def sequential(self, val):
        self["sequential"] = val

    @property
    def sequentialminus(self):
        return self["sequentialminus"]

    @sequentialminus.setter
    def sequentialminus(self, val):
        self["sequentialminus"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, diverging=None, sequential=None, sequentialminus=None, **kwargs
    ):
        super(Colorscale, self).__init__("colorscale")

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
The first argument to the plotly.graph_objs.layout.Colorscale
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Colorscale`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("diverging", None)
        _v = diverging if diverging is not None else _v
        if _v is not None:
            self["diverging"] = _v
        _v = arg.pop("sequential", None)
        _v = sequential if sequential is not None else _v
        if _v is not None:
            self["sequential"] = _v
        _v = arg.pop("sequentialminus", None)
        _v = sequentialminus if sequentialminus is not None else _v
        if _v is not None:
            self["sequentialminus"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
