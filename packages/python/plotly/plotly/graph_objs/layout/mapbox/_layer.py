from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Layer(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.mapbox"
    _path_str = "layout.mapbox.layer"
    _valid_props = {
        "below",
        "circle",
        "color",
        "coordinates",
        "fill",
        "line",
        "maxzoom",
        "minzoom",
        "name",
        "opacity",
        "source",
        "sourceattribution",
        "sourcelayer",
        "sourcetype",
        "symbol",
        "templateitemname",
        "type",
        "visible",
    }

    @property
    def below(self):
        return self["below"]

    @below.setter
    def below(self, val):
        self["below"] = val

    @property
    def circle(self):
        return self["circle"]

    @circle.setter
    def circle(self, val):
        self["circle"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def coordinates(self):
        return self["coordinates"]

    @coordinates.setter
    def coordinates(self, val):
        self["coordinates"] = val

    @property
    def fill(self):
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def maxzoom(self):
        return self["maxzoom"]

    @maxzoom.setter
    def maxzoom(self, val):
        self["maxzoom"] = val

    @property
    def minzoom(self):
        return self["minzoom"]

    @minzoom.setter
    def minzoom(self, val):
        self["minzoom"] = val

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
    def source(self):
        return self["source"]

    @source.setter
    def source(self, val):
        self["source"] = val

    @property
    def sourceattribution(self):
        return self["sourceattribution"]

    @sourceattribution.setter
    def sourceattribution(self, val):
        self["sourceattribution"] = val

    @property
    def sourcelayer(self):
        return self["sourcelayer"]

    @sourcelayer.setter
    def sourcelayer(self, val):
        self["sourcelayer"] = val

    @property
    def sourcetype(self):
        return self["sourcetype"]

    @sourcetype.setter
    def sourcetype(self, val):
        self["sourcetype"] = val

    @property
    def symbol(self):
        return self["symbol"]

    @symbol.setter
    def symbol(self, val):
        self["symbol"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def type(self):
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

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
        below=None,
        circle=None,
        color=None,
        coordinates=None,
        fill=None,
        line=None,
        maxzoom=None,
        minzoom=None,
        name=None,
        opacity=None,
        source=None,
        sourceattribution=None,
        sourcelayer=None,
        sourcetype=None,
        symbol=None,
        templateitemname=None,
        type=None,
        visible=None,
        **kwargs,
    ):
        super(Layer, self).__init__("layers")

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
The first argument to the plotly.graph_objs.layout.mapbox.Layer
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.mapbox.Layer`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("below", None)
        _v = below if below is not None else _v
        if _v is not None:
            self["below"] = _v
        _v = arg.pop("circle", None)
        _v = circle if circle is not None else _v
        if _v is not None:
            self["circle"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("coordinates", None)
        _v = coordinates if coordinates is not None else _v
        if _v is not None:
            self["coordinates"] = _v
        _v = arg.pop("fill", None)
        _v = fill if fill is not None else _v
        if _v is not None:
            self["fill"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("maxzoom", None)
        _v = maxzoom if maxzoom is not None else _v
        if _v is not None:
            self["maxzoom"] = _v
        _v = arg.pop("minzoom", None)
        _v = minzoom if minzoom is not None else _v
        if _v is not None:
            self["minzoom"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("source", None)
        _v = source if source is not None else _v
        if _v is not None:
            self["source"] = _v
        _v = arg.pop("sourceattribution", None)
        _v = sourceattribution if sourceattribution is not None else _v
        if _v is not None:
            self["sourceattribution"] = _v
        _v = arg.pop("sourcelayer", None)
        _v = sourcelayer if sourcelayer is not None else _v
        if _v is not None:
            self["sourcelayer"] = _v
        _v = arg.pop("sourcetype", None)
        _v = sourcetype if sourcetype is not None else _v
        if _v is not None:
            self["sourcetype"] = _v
        _v = arg.pop("symbol", None)
        _v = symbol if symbol is not None else _v
        if _v is not None:
            self["symbol"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
