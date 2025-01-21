from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Textfont(_BaseTraceHierarchyType):

    _parent_path_str = "scatter.selected"
    _path_str = "scatter.selected.textfont"
    _valid_props = {"color"}

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, color=None, **kwargs):
        super(Textfont, self).__init__("textfont")

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
The first argument to the plotly.graph_objs.scatter.selected.Textfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter.selected.Textfont`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
