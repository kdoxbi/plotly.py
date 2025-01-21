from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Link(_BaseTraceHierarchyType):

    _parent_path_str = "sankey"
    _path_str = "sankey.link"
    _valid_props = {
        "arrowlen",
        "color",
        "colorscaledefaults",
        "colorscales",
        "colorsrc",
        "customdata",
        "customdatasrc",
        "hovercolor",
        "hovercolorsrc",
        "hoverinfo",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "label",
        "labelsrc",
        "line",
        "source",
        "sourcesrc",
        "target",
        "targetsrc",
        "value",
        "valuesrc",
    }

    @property
    def arrowlen(self):
        return self["arrowlen"]

    @arrowlen.setter
    def arrowlen(self, val):
        self["arrowlen"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def colorscales(self):
        return self["colorscales"]

    @colorscales.setter
    def colorscales(self, val):
        self["colorscales"] = val

    @property
    def colorscaledefaults(self):
        return self["colorscaledefaults"]

    @colorscaledefaults.setter
    def colorscaledefaults(self, val):
        self["colorscaledefaults"] = val

    @property
    def colorsrc(self):
        return self["colorsrc"]

    @colorsrc.setter
    def colorsrc(self, val):
        self["colorsrc"] = val

    @property
    def customdata(self):
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    @property
    def customdatasrc(self):
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    @property
    def hovercolor(self):
        return self["hovercolor"]

    @hovercolor.setter
    def hovercolor(self, val):
        self["hovercolor"] = val

    @property
    def hovercolorsrc(self):
        return self["hovercolorsrc"]

    @hovercolorsrc.setter
    def hovercolorsrc(self, val):
        self["hovercolorsrc"] = val

    @property
    def hoverinfo(self):
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    @property
    def hoverlabel(self):
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hovertemplate(self):
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    @property
    def hovertemplatesrc(self):
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    @property
    def label(self):
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

    @property
    def labelsrc(self):
        return self["labelsrc"]

    @labelsrc.setter
    def labelsrc(self, val):
        self["labelsrc"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def source(self):
        return self["source"]

    @source.setter
    def source(self, val):
        self["source"] = val

    @property
    def sourcesrc(self):
        return self["sourcesrc"]

    @sourcesrc.setter
    def sourcesrc(self, val):
        self["sourcesrc"] = val

    @property
    def target(self):
        return self["target"]

    @target.setter
    def target(self, val):
        self["target"] = val

    @property
    def targetsrc(self):
        return self["targetsrc"]

    @targetsrc.setter
    def targetsrc(self, val):
        self["targetsrc"] = val

    @property
    def value(self):
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    @property
    def valuesrc(self):
        return self["valuesrc"]

    @valuesrc.setter
    def valuesrc(self, val):
        self["valuesrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        arrowlen=None,
        color=None,
        colorscales=None,
        colorscaledefaults=None,
        colorsrc=None,
        customdata=None,
        customdatasrc=None,
        hovercolor=None,
        hovercolorsrc=None,
        hoverinfo=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        label=None,
        labelsrc=None,
        line=None,
        source=None,
        sourcesrc=None,
        target=None,
        targetsrc=None,
        value=None,
        valuesrc=None,
        **kwargs,
    ):
        super(Link, self).__init__("link")

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
The first argument to the plotly.graph_objs.sankey.Link
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sankey.Link`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("arrowlen", None)
        _v = arrowlen if arrowlen is not None else _v
        if _v is not None:
            self["arrowlen"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("colorscales", None)
        _v = colorscales if colorscales is not None else _v
        if _v is not None:
            self["colorscales"] = _v
        _v = arg.pop("colorscaledefaults", None)
        _v = colorscaledefaults if colorscaledefaults is not None else _v
        if _v is not None:
            self["colorscaledefaults"] = _v
        _v = arg.pop("colorsrc", None)
        _v = colorsrc if colorsrc is not None else _v
        if _v is not None:
            self["colorsrc"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("hovercolor", None)
        _v = hovercolor if hovercolor is not None else _v
        if _v is not None:
            self["hovercolor"] = _v
        _v = arg.pop("hovercolorsrc", None)
        _v = hovercolorsrc if hovercolorsrc is not None else _v
        if _v is not None:
            self["hovercolorsrc"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("hovertemplatesrc", None)
        _v = hovertemplatesrc if hovertemplatesrc is not None else _v
        if _v is not None:
            self["hovertemplatesrc"] = _v
        _v = arg.pop("label", None)
        _v = label if label is not None else _v
        if _v is not None:
            self["label"] = _v
        _v = arg.pop("labelsrc", None)
        _v = labelsrc if labelsrc is not None else _v
        if _v is not None:
            self["labelsrc"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("source", None)
        _v = source if source is not None else _v
        if _v is not None:
            self["source"] = _v
        _v = arg.pop("sourcesrc", None)
        _v = sourcesrc if sourcesrc is not None else _v
        if _v is not None:
            self["sourcesrc"] = _v
        _v = arg.pop("target", None)
        _v = target if target is not None else _v
        if _v is not None:
            self["target"] = _v
        _v = arg.pop("targetsrc", None)
        _v = targetsrc if targetsrc is not None else _v
        if _v is not None:
            self["targetsrc"] = _v
        _v = arg.pop("value", None)
        _v = value if value is not None else _v
        if _v is not None:
            self["value"] = _v
        _v = arg.pop("valuesrc", None)
        _v = valuesrc if valuesrc is not None else _v
        if _v is not None:
            self["valuesrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
