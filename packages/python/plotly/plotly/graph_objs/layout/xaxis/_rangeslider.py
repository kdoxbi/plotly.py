from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Rangeslider(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.xaxis"
    _path_str = "layout.xaxis.rangeslider"
    _valid_props = {
        "autorange",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "range",
        "thickness",
        "visible",
        "yaxis",
    }

    @property
    def autorange(self):
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bordercolor(self):
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def borderwidth(self):
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    @property
    def range(self):
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    @property
    def thickness(self):
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        autorange=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        range=None,
        thickness=None,
        visible=None,
        yaxis=None,
        **kwargs,
    ):
        super(Rangeslider, self).__init__("rangeslider")

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
The first argument to the plotly.graph_objs.layout.xaxis.Rangeslider
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.xaxis.Rangeslider`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("autorange", None)
        _v = autorange if autorange is not None else _v
        if _v is not None:
            self["autorange"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("borderwidth", None)
        _v = borderwidth if borderwidth is not None else _v
        if _v is not None:
            self["borderwidth"] = _v
        _v = arg.pop("range", None)
        _v = range if range is not None else _v
        if _v is not None:
            self["range"] = _v
        _v = arg.pop("thickness", None)
        _v = thickness if thickness is not None else _v
        if _v is not None:
            self["thickness"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
