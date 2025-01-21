from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Button(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.xaxis.rangeselector"
    _path_str = "layout.xaxis.rangeselector.button"
    _valid_props = {
        "count",
        "label",
        "name",
        "step",
        "stepmode",
        "templateitemname",
        "visible",
    }

    @property
    def count(self):
        return self["count"]

    @count.setter
    def count(self, val):
        self["count"] = val

    @property
    def label(self):
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def step(self):
        return self["step"]

    @step.setter
    def step(self, val):
        self["step"] = val

    @property
    def stepmode(self):
        return self["stepmode"]

    @stepmode.setter
    def stepmode(self, val):
        self["stepmode"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

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
        count=None,
        label=None,
        name=None,
        step=None,
        stepmode=None,
        templateitemname=None,
        visible=None,
        **kwargs,
    ):
        super(Button, self).__init__("buttons")

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
The first argument to the plotly.graph_objs.layout.xaxis.rangeselector.Button
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.xaxis.rangeselector.Button`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("count", None)
        _v = count if count is not None else _v
        if _v is not None:
            self["count"] = _v
        _v = arg.pop("label", None)
        _v = label if label is not None else _v
        if _v is not None:
            self["label"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("step", None)
        _v = step if step is not None else _v
        if _v is not None:
            self["step"] = _v
        _v = arg.pop("stepmode", None)
        _v = stepmode if stepmode is not None else _v
        if _v is not None:
            self["stepmode"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
