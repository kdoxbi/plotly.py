from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Newselection(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.newselection"
    _valid_props = {"line", "mode"}

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

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

    def __init__(self, arg=None, line=None, mode=None, **kwargs):
        super(Newselection, self).__init__("newselection")

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
The first argument to the plotly.graph_objs.layout.Newselection
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Newselection`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("mode", None)
        _v = mode if mode is not None else _v
        if _v is not None:
            self["mode"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
