from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Contours(_BaseTraceHierarchyType):

    _parent_path_str = "contourcarpet"
    _path_str = "contourcarpet.contours"
    _valid_props = {
        "coloring",
        "end",
        "labelfont",
        "labelformat",
        "operation",
        "showlabels",
        "showlines",
        "size",
        "start",
        "type",
        "value",
    }

    @property
    def coloring(self):
        return self["coloring"]

    @coloring.setter
    def coloring(self, val):
        self["coloring"] = val

    @property
    def end(self):
        return self["end"]

    @end.setter
    def end(self, val):
        self["end"] = val

    @property
    def labelfont(self):
        return self["labelfont"]

    @labelfont.setter
    def labelfont(self, val):
        self["labelfont"] = val

    @property
    def labelformat(self):
        return self["labelformat"]

    @labelformat.setter
    def labelformat(self, val):
        self["labelformat"] = val

    @property
    def operation(self):
        return self["operation"]

    @operation.setter
    def operation(self, val):
        self["operation"] = val

    @property
    def showlabels(self):
        return self["showlabels"]

    @showlabels.setter
    def showlabels(self, val):
        self["showlabels"] = val

    @property
    def showlines(self):
        return self["showlines"]

    @showlines.setter
    def showlines(self, val):
        self["showlines"] = val

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
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def value(self):
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        coloring=None,
        end=None,
        labelfont=None,
        labelformat=None,
        operation=None,
        showlabels=None,
        showlines=None,
        size=None,
        start=None,
        type=None,
        value=None,
        **kwargs,
    ):
        super(Contours, self).__init__("contours")

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
The first argument to the plotly.graph_objs.contourcarpet.Contours
constructor must be a dict or
an instance of :class:`plotly.graph_objs.contourcarpet.Contours`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("coloring", None)
        _v = coloring if coloring is not None else _v
        if _v is not None:
            self["coloring"] = _v
        _v = arg.pop("end", None)
        _v = end if end is not None else _v
        if _v is not None:
            self["end"] = _v
        _v = arg.pop("labelfont", None)
        _v = labelfont if labelfont is not None else _v
        if _v is not None:
            self["labelfont"] = _v
        _v = arg.pop("labelformat", None)
        _v = labelformat if labelformat is not None else _v
        if _v is not None:
            self["labelformat"] = _v
        _v = arg.pop("operation", None)
        _v = operation if operation is not None else _v
        if _v is not None:
            self["operation"] = _v
        _v = arg.pop("showlabels", None)
        _v = showlabels if showlabels is not None else _v
        if _v is not None:
            self["showlabels"] = _v
        _v = arg.pop("showlines", None)
        _v = showlines if showlines is not None else _v
        if _v is not None:
            self["showlines"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("start", None)
        _v = start if start is not None else _v
        if _v is not None:
            self["start"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
