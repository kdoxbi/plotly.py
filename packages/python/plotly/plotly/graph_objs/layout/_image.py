from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Image(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.image"
    _valid_props = {
        "layer",
        "name",
        "opacity",
        "sizex",
        "sizey",
        "sizing",
        "source",
        "templateitemname",
        "visible",
        "x",
        "xanchor",
        "xref",
        "y",
        "yanchor",
        "yref",
    }

    @property
    def layer(self):
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def opacity(self):
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def sizex(self):
        return self["sizex"]

    @sizex.setter
    def sizex(self, val):
        self["sizex"] = val

    @property
    def sizey(self):
        return self["sizey"]

    @sizey.setter
    def sizey(self, val):
        self["sizey"] = val

    @property
    def sizing(self):
        return self["sizing"]

    @sizing.setter
    def sizing(self, val):
        self["sizing"] = val

    @property
    def source(self):
        return self["source"]

    @source.setter
    def source(self, val):
        self["source"] = val

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
    def x(self):
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def xanchor(self):
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    @property
    def xref(self):
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    @property
    def y(self):
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def yanchor(self):
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    @property
    def yref(self):
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        layer=None,
        name=None,
        opacity=None,
        sizex=None,
        sizey=None,
        sizing=None,
        source=None,
        templateitemname=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs,
    ):
        super(Image, self).__init__("images")

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
The first argument to the plotly.graph_objs.layout.Image
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Image`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("layer", None)
        _v = layer if layer is not None else _v
        if _v is not None:
            self["layer"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("sizex", None)
        _v = sizex if sizex is not None else _v
        if _v is not None:
            self["sizex"] = _v
        _v = arg.pop("sizey", None)
        _v = sizey if sizey is not None else _v
        if _v is not None:
            self["sizey"] = _v
        _v = arg.pop("sizing", None)
        _v = sizing if sizing is not None else _v
        if _v is not None:
            self["sizing"] = _v
        _v = arg.pop("source", None)
        _v = source if source is not None else _v
        if _v is not None:
            self["source"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xanchor", None)
        _v = xanchor if xanchor is not None else _v
        if _v is not None:
            self["xanchor"] = _v
        _v = arg.pop("xref", None)
        _v = xref if xref is not None else _v
        if _v is not None:
            self["xref"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("yanchor", None)
        _v = yanchor if yanchor is not None else _v
        if _v is not None:
            self["yanchor"] = _v
        _v = arg.pop("yref", None)
        _v = yref if yref is not None else _v
        if _v is not None:
            self["yref"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
