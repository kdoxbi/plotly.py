from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    _parent_path_str = "pie"
    _path_str = "pie.marker"
    _valid_props = {"colors", "colorssrc", "line", "pattern"}

    @property
    def colors(self):
        return self["colors"]

    @colors.setter
    def colors(self, val):
        self["colors"] = val

    @property
    def colorssrc(self):
        return self["colorssrc"]

    @colorssrc.setter
    def colorssrc(self, val):
        self["colorssrc"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def pattern(self):
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self, arg=None, colors=None, colorssrc=None, line=None, pattern=None, **kwargs
    ):
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.pie.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.pie.Marker`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("colors", None)
        _v = colors if colors is not None else _v
        if _v is not None:
            self["colors"] = _v
        _v = arg.pop("colorssrc", None)
        _v = colorssrc if colorssrc is not None else _v
        if _v is not None:
            self["colorssrc"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("pattern", None)
        _v = pattern if pattern is not None else _v
        if _v is not None:
            self["pattern"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
