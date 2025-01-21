from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Z(_BaseTraceHierarchyType):

    _parent_path_str = "surface.contours"
    _path_str = "surface.contours.z"
    _valid_props = {
        "color",
        "end",
        "highlight",
        "highlightcolor",
        "highlightwidth",
        "project",
        "show",
        "size",
        "start",
        "usecolormap",
        "width",
    }

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def end(self):
        return self["end"]

    @end.setter
    def end(self, val):
        self["end"] = val

    @property
    def highlight(self):
        return self["highlight"]

    @highlight.setter
    def highlight(self, val):
        self["highlight"] = val

    @property
    def highlightcolor(self):
        return self["highlightcolor"]

    @highlightcolor.setter
    def highlightcolor(self, val):
        self["highlightcolor"] = val

    @property
    def highlightwidth(self):
        return self["highlightwidth"]

    @highlightwidth.setter
    def highlightwidth(self, val):
        self["highlightwidth"] = val

    @property
    def project(self):
        return self["project"]

    @project.setter
    def project(self, val):
        self["project"] = val

    @property
    def show(self):
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

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
    def usecolormap(self):
        return self["usecolormap"]

    @usecolormap.setter
    def usecolormap(self, val):
        self["usecolormap"] = val

    @property
    def width(self):
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        color=None,
        end=None,
        highlight=None,
        highlightcolor=None,
        highlightwidth=None,
        project=None,
        show=None,
        size=None,
        start=None,
        usecolormap=None,
        width=None,
        **kwargs,
    ):
        super(Z, self).__init__("z")

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
The first argument to the plotly.graph_objs.surface.contours.Z
constructor must be a dict or
an instance of :class:`plotly.graph_objs.surface.contours.Z`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("end", None)
        _v = end if end is not None else _v
        if _v is not None:
            self["end"] = _v
        _v = arg.pop("highlight", None)
        _v = highlight if highlight is not None else _v
        if _v is not None:
            self["highlight"] = _v
        _v = arg.pop("highlightcolor", None)
        _v = highlightcolor if highlightcolor is not None else _v
        if _v is not None:
            self["highlightcolor"] = _v
        _v = arg.pop("highlightwidth", None)
        _v = highlightwidth if highlightwidth is not None else _v
        if _v is not None:
            self["highlightwidth"] = _v
        _v = arg.pop("project", None)
        _v = project if project is not None else _v
        if _v is not None:
            self["project"] = _v
        _v = arg.pop("show", None)
        _v = show if show is not None else _v
        if _v is not None:
            self["show"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("start", None)
        _v = start if start is not None else _v
        if _v is not None:
            self["start"] = _v
        _v = arg.pop("usecolormap", None)
        _v = usecolormap if usecolormap is not None else _v
        if _v is not None:
            self["usecolormap"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
