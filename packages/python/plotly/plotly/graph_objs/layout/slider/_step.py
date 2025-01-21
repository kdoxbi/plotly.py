from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Step(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.slider"
    _path_str = "layout.slider.step"
    _valid_props = {
        "args",
        "execute",
        "label",
        "method",
        "name",
        "templateitemname",
        "value",
        "visible",
    }

    @property
    def args(self):
        return self["args"]

    @args.setter
    def args(self, val):
        self["args"] = val

    @property
    def execute(self):
        return self["execute"]

    @execute.setter
    def execute(self, val):
        self["execute"] = val

    @property
    def label(self):
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

    @property
    def method(self):
        return self["method"]

    @method.setter
    def method(self, val):
        self["method"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def value(self):
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        args=None,
        execute=None,
        label=None,
        method=None,
        name=None,
        templateitemname=None,
        value=None,
        visible=None,
        **kwargs,
    ):
        super(Step, self).__init__("steps")

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
The first argument to the plotly.graph_objs.layout.slider.Step
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Step`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("args", None)
        _v = args if args is not None else _v
        if _v is not None:
            self["args"] = _v
        _v = arg.pop("execute", None)
        _v = execute if execute is not None else _v
        if _v is not None:
            self["execute"] = _v
        _v = arg.pop("label", None)
        _v = label if label is not None else _v
        if _v is not None:
            self["label"] = _v
        _v = arg.pop("method", None)
        _v = method if method is not None else _v
        if _v is not None:
            self["method"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
