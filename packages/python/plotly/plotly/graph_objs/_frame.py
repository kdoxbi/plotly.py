from plotly.basedatatypes import BaseFrameHierarchyType as _BaseFrameHierarchyType
import copy as _copy


class Frame(_BaseFrameHierarchyType):

    _parent_path_str = ""
    _path_str = "frame"
    _valid_props = {"baseframe", "data", "group", "layout", "name", "traces"}

    @property
    def baseframe(self):
        return self["baseframe"]

    @baseframe.setter
    def baseframe(self, val):
        self["baseframe"] = val

    @property
    def data(self):
        return self["data"]

    @data.setter
    def data(self, val):
        self["data"] = val

    @property
    def group(self):
        return self["group"]

    @group.setter
    def group(self, val):
        self["group"] = val

    @property
    def layout(self):
        return self["layout"]

    @layout.setter
    def layout(self, val):
        self["layout"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def traces(self):
        return self["traces"]

    @traces.setter
    def traces(self, val):
        self["traces"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        baseframe=None,
        data=None,
        group=None,
        layout=None,
        name=None,
        traces=None,
        **kwargs,
    ):
        super(Frame, self).__init__("frames")

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
The first argument to the plotly.graph_objs.Frame
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Frame`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("baseframe", None)
        _v = baseframe if baseframe is not None else _v
        if _v is not None:
            self["baseframe"] = _v
        _v = arg.pop("data", None)
        _v = data if data is not None else _v
        if _v is not None:
            self["data"] = _v
        _v = arg.pop("group", None)
        _v = group if group is not None else _v
        if _v is not None:
            self["group"] = _v
        _v = arg.pop("layout", None)
        _v = layout if layout is not None else _v
        if _v is not None:
            self["layout"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("traces", None)
        _v = traces if traces is not None else _v
        if _v is not None:
            self["traces"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
