from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class YBins(_BaseTraceHierarchyType):

    _parent_path_str = "histogram2dcontour"
    _path_str = "histogram2dcontour.ybins"
    _valid_props = {"end", "size", "start"}

    @property
    def end(self):
        return self["end"]

    @end.setter
    def end(self, val):
        self["end"] = val

    @property
    def size(self):
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    @property
    def start(self):
        return self["start"]

    @start.setter
    def start(self, val):
        self["start"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, end=None, size=None, start=None, **kwargs):
        super(YBins, self).__init__("ybins")

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
The first argument to the plotly.graph_objs.histogram2dcontour.YBins
constructor must be a dict or
an instance of :class:`plotly.graph_objs.histogram2dcontour.YBins`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("end", None)
        _v = end if end is not None else _v
        if _v is not None:
            self["end"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("start", None)
        _v = start if start is not None else _v
        if _v is not None:
            self["start"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
