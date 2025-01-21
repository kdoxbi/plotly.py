from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class ErrorX(_BaseTraceHierarchyType):

    _parent_path_str = "scatter3d"
    _path_str = "scatter3d.error_x"
    _valid_props = {
        "array",
        "arrayminus",
        "arrayminussrc",
        "arraysrc",
        "color",
        "copy_zstyle",
        "symmetric",
        "thickness",
        "traceref",
        "tracerefminus",
        "type",
        "value",
        "valueminus",
        "visible",
        "width",
    }

    @property
    def array(self):
        return self["array"]

    @array.setter
    def array(self, val):
        self["array"] = val

    @property
    def arrayminus(self):
        return self["arrayminus"]

    @arrayminus.setter
    def arrayminus(self, val):
        self["arrayminus"] = val

    @property
    def arrayminussrc(self):
        return self["arrayminussrc"]

    @arrayminussrc.setter
    def arrayminussrc(self, val):
        self["arrayminussrc"] = val

    @property
    def arraysrc(self):
        return self["arraysrc"]

    @arraysrc.setter
    def arraysrc(self, val):
        self["arraysrc"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def copy_zstyle(self):
        return self["copy_zstyle"]

    @copy_zstyle.setter
    def copy_zstyle(self, val):
        self["copy_zstyle"] = val

    @property
    def symmetric(self):
        return self["symmetric"]

    @symmetric.setter
    def symmetric(self, val):
        self["symmetric"] = val

    @property
    def thickness(self):
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    @property
    def traceref(self):
        return self["traceref"]

    @traceref.setter
    def traceref(self, val):
        self["traceref"] = val

    @property
    def tracerefminus(self):
        return self["tracerefminus"]

    @tracerefminus.setter
    def tracerefminus(self, val):
        self["tracerefminus"] = val

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
    def valueminus(self):
        return self["valueminus"]

    @valueminus.setter
    def valueminus(self, val):
        self["valueminus"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

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
        array=None,
        arrayminus=None,
        arrayminussrc=None,
        arraysrc=None,
        color=None,
        copy_zstyle=None,
        symmetric=None,
        thickness=None,
        traceref=None,
        tracerefminus=None,
        type=None,
        value=None,
        valueminus=None,
        visible=None,
        width=None,
        **kwargs,
    ):
        super(ErrorX, self).__init__("error_x")

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
The first argument to the plotly.graph_objs.scatter3d.ErrorX
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter3d.ErrorX`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("array", None)
        _v = array if array is not None else _v
        if _v is not None:
            self["array"] = _v
        _v = arg.pop("arrayminus", None)
        _v = arrayminus if arrayminus is not None else _v
        if _v is not None:
            self["arrayminus"] = _v
        _v = arg.pop("arrayminussrc", None)
        _v = arrayminussrc if arrayminussrc is not None else _v
        if _v is not None:
            self["arrayminussrc"] = _v
        _v = arg.pop("arraysrc", None)
        _v = arraysrc if arraysrc is not None else _v
        if _v is not None:
            self["arraysrc"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("copy_zstyle", None)
        _v = copy_zstyle if copy_zstyle is not None else _v
        if _v is not None:
            self["copy_zstyle"] = _v
        _v = arg.pop("symmetric", None)
        _v = symmetric if symmetric is not None else _v
        if _v is not None:
            self["symmetric"] = _v
        _v = arg.pop("thickness", None)
        _v = thickness if thickness is not None else _v
        if _v is not None:
            self["thickness"] = _v
        _v = arg.pop("traceref", None)
        _v = traceref if traceref is not None else _v
        if _v is not None:
            self["traceref"] = _v
        _v = arg.pop("tracerefminus", None)
        _v = tracerefminus if tracerefminus is not None else _v
        if _v is not None:
            self["tracerefminus"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        _v = arg.pop("valueminus", None)
        _v = valueminus if valueminus is not None else _v
        if _v is not None:
            self["valueminus"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
