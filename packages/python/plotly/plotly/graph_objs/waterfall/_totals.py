from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Totals(_BaseTraceHierarchyType):

    _parent_path_str = "waterfall"
    _path_str = "waterfall.totals"
    _valid_props = {"marker"}

    @property
    def marker(self):
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        super(Totals, self).__init__("totals")

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
The first argument to the plotly.graph_objs.waterfall.Totals
constructor must be a dict or
an instance of :class:`plotly.graph_objs.waterfall.Totals`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("marker", None)
        _v = marker if marker is not None else _v
        if _v is not None:
            self["marker"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
