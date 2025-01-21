from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class YAxis(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.xaxis.rangeslider"
    _path_str = "layout.xaxis.rangeslider.yaxis"
    _valid_props = {"range", "rangemode"}

    @property
    def range(self):
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    @property
    def rangemode(self):
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, range=None, rangemode=None, **kwargs):
        super(YAxis, self).__init__("yaxis")

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
The first argument to the plotly.graph_objs.layout.xaxis.rangeslider.YAxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.xaxis.rangeslider.YAxis`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("range", None)
        _v = range if range is not None else _v
        if _v is not None:
            self["range"] = _v
        _v = arg.pop("rangemode", None)
        _v = rangemode if rangemode is not None else _v
        if _v is not None:
            self["rangemode"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
