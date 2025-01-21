from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Stream(_BaseTraceHierarchyType):

    _parent_path_str = "densitymapbox"
    _path_str = "densitymapbox.stream"
    _valid_props = {"maxpoints", "token"}

    @property
    def maxpoints(self):
        return self["maxpoints"]

    @maxpoints.setter
    def maxpoints(self, val):
        self["maxpoints"] = val

    @property
    def token(self):
        return self["token"]

    @token.setter
    def token(self, val):
        self["token"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        super(Stream, self).__init__("stream")

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
The first argument to the plotly.graph_objs.densitymapbox.Stream
constructor must be a dict or
an instance of :class:`plotly.graph_objs.densitymapbox.Stream`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("maxpoints", None)
        _v = maxpoints if maxpoints is not None else _v
        if _v is not None:
            self["maxpoints"] = _v
        _v = arg.pop("token", None)
        _v = token if token is not None else _v
        if _v is not None:
            self["token"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
