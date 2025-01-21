from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Shape(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.shape"
    _valid_props = {
        "editable",
        "fillcolor",
        "fillrule",
        "label",
        "layer",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "name",
        "opacity",
        "path",
        "showlegend",
        "templateitemname",
        "type",
        "visible",
        "x0",
        "x0shift",
        "x1",
        "x1shift",
        "xanchor",
        "xref",
        "xsizemode",
        "y0",
        "y0shift",
        "y1",
        "y1shift",
        "yanchor",
        "yref",
        "ysizemode",
    }

    @property
    def editable(self):
        return self["editable"]

    @editable.setter
    def editable(self, val):
        self["editable"] = val

    @property
    def fillcolor(self):
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    @property
    def fillrule(self):
        return self["fillrule"]

    @fillrule.setter
    def fillrule(self, val):
        self["fillrule"] = val

    @property
    def label(self):
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

    @property
    def layer(self):
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    @property
    def legend(self):
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    @property
    def legendgroup(self):
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    @property
    def legendgrouptitle(self):
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    @property
    def legendrank(self):
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    @property
    def legendwidth(self):
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

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
    def path(self):
        return self["path"]

    @path.setter
    def path(self, val):
        self["path"] = val

    @property
    def showlegend(self):
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

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
    def x0(self):
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    @property
    def x0shift(self):
        return self["x0shift"]

    @x0shift.setter
    def x0shift(self, val):
        self["x0shift"] = val

    @property
    def x1(self):
        return self["x1"]

    @x1.setter
    def x1(self, val):
        self["x1"] = val

    @property
    def x1shift(self):
        return self["x1shift"]

    @x1shift.setter
    def x1shift(self, val):
        self["x1shift"] = val

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
    def xsizemode(self):
        return self["xsizemode"]

    @xsizemode.setter
    def xsizemode(self, val):
        self["xsizemode"] = val

    @property
    def y0(self):
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    @property
    def y0shift(self):
        return self["y0shift"]

    @y0shift.setter
    def y0shift(self, val):
        self["y0shift"] = val

    @property
    def y1(self):
        return self["y1"]

    @y1.setter
    def y1(self, val):
        self["y1"] = val

    @property
    def y1shift(self):
        return self["y1shift"]

    @y1shift.setter
    def y1shift(self, val):
        self["y1shift"] = val

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
    def ysizemode(self):
        return self["ysizemode"]

    @ysizemode.setter
    def ysizemode(self, val):
        self["ysizemode"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        editable=None,
        fillcolor=None,
        fillrule=None,
        label=None,
        layer=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        showlegend=None,
        templateitemname=None,
        type=None,
        visible=None,
        x0=None,
        x0shift=None,
        x1=None,
        x1shift=None,
        xanchor=None,
        xref=None,
        xsizemode=None,
        y0=None,
        y0shift=None,
        y1=None,
        y1shift=None,
        yanchor=None,
        yref=None,
        ysizemode=None,
        **kwargs,
    ):
        super(Shape, self).__init__("shapes")

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
The first argument to the plotly.graph_objs.layout.Shape
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Shape`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("editable", None)
        _v = editable if editable is not None else _v
        if _v is not None:
            self["editable"] = _v
        _v = arg.pop("fillcolor", None)
        _v = fillcolor if fillcolor is not None else _v
        if _v is not None:
            self["fillcolor"] = _v
        _v = arg.pop("fillrule", None)
        _v = fillrule if fillrule is not None else _v
        if _v is not None:
            self["fillrule"] = _v
        _v = arg.pop("label", None)
        _v = label if label is not None else _v
        if _v is not None:
            self["label"] = _v
        _v = arg.pop("layer", None)
        _v = layer if layer is not None else _v
        if _v is not None:
            self["layer"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
        _v = arg.pop("legendrank", None)
        _v = legendrank if legendrank is not None else _v
        if _v is not None:
            self["legendrank"] = _v
        _v = arg.pop("legendwidth", None)
        _v = legendwidth if legendwidth is not None else _v
        if _v is not None:
            self["legendwidth"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("path", None)
        _v = path if path is not None else _v
        if _v is not None:
            self["path"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
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
        _v = arg.pop("x0", None)
        _v = x0 if x0 is not None else _v
        if _v is not None:
            self["x0"] = _v
        _v = arg.pop("x0shift", None)
        _v = x0shift if x0shift is not None else _v
        if _v is not None:
            self["x0shift"] = _v
        _v = arg.pop("x1", None)
        _v = x1 if x1 is not None else _v
        if _v is not None:
            self["x1"] = _v
        _v = arg.pop("x1shift", None)
        _v = x1shift if x1shift is not None else _v
        if _v is not None:
            self["x1shift"] = _v
        _v = arg.pop("xanchor", None)
        _v = xanchor if xanchor is not None else _v
        if _v is not None:
            self["xanchor"] = _v
        _v = arg.pop("xref", None)
        _v = xref if xref is not None else _v
        if _v is not None:
            self["xref"] = _v
        _v = arg.pop("xsizemode", None)
        _v = xsizemode if xsizemode is not None else _v
        if _v is not None:
            self["xsizemode"] = _v
        _v = arg.pop("y0", None)
        _v = y0 if y0 is not None else _v
        if _v is not None:
            self["y0"] = _v
        _v = arg.pop("y0shift", None)
        _v = y0shift if y0shift is not None else _v
        if _v is not None:
            self["y0shift"] = _v
        _v = arg.pop("y1", None)
        _v = y1 if y1 is not None else _v
        if _v is not None:
            self["y1"] = _v
        _v = arg.pop("y1shift", None)
        _v = y1shift if y1shift is not None else _v
        if _v is not None:
            self["y1shift"] = _v
        _v = arg.pop("yanchor", None)
        _v = yanchor if yanchor is not None else _v
        if _v is not None:
            self["yanchor"] = _v
        _v = arg.pop("yref", None)
        _v = yref if yref is not None else _v
        if _v is not None:
            self["yref"] = _v
        _v = arg.pop("ysizemode", None)
        _v = ysizemode if ysizemode is not None else _v
        if _v is not None:
            self["ysizemode"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
