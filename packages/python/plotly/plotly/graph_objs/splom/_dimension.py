from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Dimension(_BaseTraceHierarchyType):

    _parent_path_str = "splom"
    _path_str = "splom.dimension"
    _valid_props = {
        "axis",
        "label",
        "name",
        "templateitemname",
        "values",
        "valuessrc",
        "visible",
    }

    @property
    def axis(self):
        return self["axis"]

    @axis.setter
    def axis(self, val):
        self["axis"] = val

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
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def values(self):
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    @property
    def valuessrc(self):
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

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
        axis=None,
        label=None,
        name=None,
        templateitemname=None,
        values=None,
        valuessrc=None,
        visible=None,
        **kwargs,
    ):
        super(Dimension, self).__init__("dimensions")

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
The first argument to the plotly.graph_objs.splom.Dimension
constructor must be a dict or
an instance of :class:`plotly.graph_objs.splom.Dimension`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("axis", None)
        _v = axis if axis is not None else _v
        if _v is not None:
            self["axis"] = _v
        _v = arg.pop("label", None)
        _v = label if label is not None else _v
        if _v is not None:
            self["label"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("values", None)
        _v = values if values is not None else _v
        if _v is not None:
            self["values"] = _v
        _v = arg.pop("valuessrc", None)
        _v = valuessrc if valuessrc is not None else _v
        if _v is not None:
            self["valuessrc"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
