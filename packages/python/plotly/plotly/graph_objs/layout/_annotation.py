from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Annotation(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.annotation"
    _valid_props = {
        "align",
        "arrowcolor",
        "arrowhead",
        "arrowside",
        "arrowsize",
        "arrowwidth",
        "ax",
        "axref",
        "ay",
        "ayref",
        "bgcolor",
        "bordercolor",
        "borderpad",
        "borderwidth",
        "captureevents",
        "clicktoshow",
        "font",
        "height",
        "hoverlabel",
        "hovertext",
        "name",
        "opacity",
        "showarrow",
        "standoff",
        "startarrowhead",
        "startarrowsize",
        "startstandoff",
        "templateitemname",
        "text",
        "textangle",
        "valign",
        "visible",
        "width",
        "x",
        "xanchor",
        "xclick",
        "xref",
        "xshift",
        "y",
        "yanchor",
        "yclick",
        "yref",
        "yshift",
    }

    @property
    def align(self):
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    @property
    def arrowcolor(self):
        return self["arrowcolor"]

    @arrowcolor.setter
    def arrowcolor(self, val):
        self["arrowcolor"] = val

    @property
    def arrowhead(self):
        return self["arrowhead"]

    @arrowhead.setter
    def arrowhead(self, val):
        self["arrowhead"] = val

    @property
    def arrowside(self):
        return self["arrowside"]

    @arrowside.setter
    def arrowside(self, val):
        self["arrowside"] = val

    @property
    def arrowsize(self):
        return self["arrowsize"]

    @arrowsize.setter
    def arrowsize(self, val):
        self["arrowsize"] = val

    @property
    def arrowwidth(self):
        return self["arrowwidth"]

    @arrowwidth.setter
    def arrowwidth(self, val):
        self["arrowwidth"] = val

    @property
    def ax(self):
        return self["ax"]

    @ax.setter
    def ax(self, val):
        self["ax"] = val

    @property
    def axref(self):
        return self["axref"]

    @axref.setter
    def axref(self, val):
        self["axref"] = val

    @property
    def ay(self):
        return self["ay"]

    @ay.setter
    def ay(self, val):
        self["ay"] = val

    @property
    def ayref(self):
        return self["ayref"]

    @ayref.setter
    def ayref(self, val):
        self["ayref"] = val

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
    def borderpad(self):
        return self["borderpad"]

    @borderpad.setter
    def borderpad(self, val):
        self["borderpad"] = val

    @property
    def borderwidth(self):
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    @property
    def captureevents(self):
        return self["captureevents"]

    @captureevents.setter
    def captureevents(self, val):
        self["captureevents"] = val

    @property
    def clicktoshow(self):
        return self["clicktoshow"]

    @clicktoshow.setter
    def clicktoshow(self, val):
        self["clicktoshow"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def height(self):
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    @property
    def hoverlabel(self):
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hovertext(self):
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

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
    def showarrow(self):
        return self["showarrow"]

    @showarrow.setter
    def showarrow(self, val):
        self["showarrow"] = val

    @property
    def standoff(self):
        return self["standoff"]

    @standoff.setter
    def standoff(self, val):
        self["standoff"] = val

    @property
    def startarrowhead(self):
        return self["startarrowhead"]

    @startarrowhead.setter
    def startarrowhead(self, val):
        self["startarrowhead"] = val

    @property
    def startarrowsize(self):
        return self["startarrowsize"]

    @startarrowsize.setter
    def startarrowsize(self, val):
        self["startarrowsize"] = val

    @property
    def startstandoff(self):
        return self["startstandoff"]

    @startstandoff.setter
    def startstandoff(self, val):
        self["startstandoff"] = val

    @property
    def templateitemname(self):
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textangle(self):
        return self["textangle"]

    @textangle.setter
    def textangle(self, val):
        self["textangle"] = val

    @property
    def valign(self):
        return self["valign"]

    @valign.setter
    def valign(self, val):
        self["valign"] = val

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
    def xclick(self):
        return self["xclick"]

    @xclick.setter
    def xclick(self, val):
        self["xclick"] = val

    @property
    def xref(self):
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    @property
    def xshift(self):
        return self["xshift"]

    @xshift.setter
    def xshift(self, val):
        self["xshift"] = val

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
    def yclick(self):
        return self["yclick"]

    @yclick.setter
    def yclick(self, val):
        self["yclick"] = val

    @property
    def yref(self):
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    @property
    def yshift(self):
        return self["yshift"]

    @yshift.setter
    def yshift(self, val):
        self["yshift"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        align=None,
        arrowcolor=None,
        arrowhead=None,
        arrowside=None,
        arrowsize=None,
        arrowwidth=None,
        ax=None,
        axref=None,
        ay=None,
        ayref=None,
        bgcolor=None,
        bordercolor=None,
        borderpad=None,
        borderwidth=None,
        captureevents=None,
        clicktoshow=None,
        font=None,
        height=None,
        hoverlabel=None,
        hovertext=None,
        name=None,
        opacity=None,
        showarrow=None,
        standoff=None,
        startarrowhead=None,
        startarrowsize=None,
        startstandoff=None,
        templateitemname=None,
        text=None,
        textangle=None,
        valign=None,
        visible=None,
        width=None,
        x=None,
        xanchor=None,
        xclick=None,
        xref=None,
        xshift=None,
        y=None,
        yanchor=None,
        yclick=None,
        yref=None,
        yshift=None,
        **kwargs,
    ):
        super(Annotation, self).__init__("annotations")

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
The first argument to the plotly.graph_objs.layout.Annotation
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Annotation`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("align", None)
        _v = align if align is not None else _v
        if _v is not None:
            self["align"] = _v
        _v = arg.pop("arrowcolor", None)
        _v = arrowcolor if arrowcolor is not None else _v
        if _v is not None:
            self["arrowcolor"] = _v
        _v = arg.pop("arrowhead", None)
        _v = arrowhead if arrowhead is not None else _v
        if _v is not None:
            self["arrowhead"] = _v
        _v = arg.pop("arrowside", None)
        _v = arrowside if arrowside is not None else _v
        if _v is not None:
            self["arrowside"] = _v
        _v = arg.pop("arrowsize", None)
        _v = arrowsize if arrowsize is not None else _v
        if _v is not None:
            self["arrowsize"] = _v
        _v = arg.pop("arrowwidth", None)
        _v = arrowwidth if arrowwidth is not None else _v
        if _v is not None:
            self["arrowwidth"] = _v
        _v = arg.pop("ax", None)
        _v = ax if ax is not None else _v
        if _v is not None:
            self["ax"] = _v
        _v = arg.pop("axref", None)
        _v = axref if axref is not None else _v
        if _v is not None:
            self["axref"] = _v
        _v = arg.pop("ay", None)
        _v = ay if ay is not None else _v
        if _v is not None:
            self["ay"] = _v
        _v = arg.pop("ayref", None)
        _v = ayref if ayref is not None else _v
        if _v is not None:
            self["ayref"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bordercolor", None)
        _v = bordercolor if bordercolor is not None else _v
        if _v is not None:
            self["bordercolor"] = _v
        _v = arg.pop("borderpad", None)
        _v = borderpad if borderpad is not None else _v
        if _v is not None:
            self["borderpad"] = _v
        _v = arg.pop("borderwidth", None)
        _v = borderwidth if borderwidth is not None else _v
        if _v is not None:
            self["borderwidth"] = _v
        _v = arg.pop("captureevents", None)
        _v = captureevents if captureevents is not None else _v
        if _v is not None:
            self["captureevents"] = _v
        _v = arg.pop("clicktoshow", None)
        _v = clicktoshow if clicktoshow is not None else _v
        if _v is not None:
            self["clicktoshow"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("height", None)
        _v = height if height is not None else _v
        if _v is not None:
            self["height"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("showarrow", None)
        _v = showarrow if showarrow is not None else _v
        if _v is not None:
            self["showarrow"] = _v
        _v = arg.pop("standoff", None)
        _v = standoff if standoff is not None else _v
        if _v is not None:
            self["standoff"] = _v
        _v = arg.pop("startarrowhead", None)
        _v = startarrowhead if startarrowhead is not None else _v
        if _v is not None:
            self["startarrowhead"] = _v
        _v = arg.pop("startarrowsize", None)
        _v = startarrowsize if startarrowsize is not None else _v
        if _v is not None:
            self["startarrowsize"] = _v
        _v = arg.pop("startstandoff", None)
        _v = startstandoff if startstandoff is not None else _v
        if _v is not None:
            self["startstandoff"] = _v
        _v = arg.pop("templateitemname", None)
        _v = templateitemname if templateitemname is not None else _v
        if _v is not None:
            self["templateitemname"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textangle", None)
        _v = textangle if textangle is not None else _v
        if _v is not None:
            self["textangle"] = _v
        _v = arg.pop("valign", None)
        _v = valign if valign is not None else _v
        if _v is not None:
            self["valign"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xanchor", None)
        _v = xanchor if xanchor is not None else _v
        if _v is not None:
            self["xanchor"] = _v
        _v = arg.pop("xclick", None)
        _v = xclick if xclick is not None else _v
        if _v is not None:
            self["xclick"] = _v
        _v = arg.pop("xref", None)
        _v = xref if xref is not None else _v
        if _v is not None:
            self["xref"] = _v
        _v = arg.pop("xshift", None)
        _v = xshift if xshift is not None else _v
        if _v is not None:
            self["xshift"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("yanchor", None)
        _v = yanchor if yanchor is not None else _v
        if _v is not None:
            self["yanchor"] = _v
        _v = arg.pop("yclick", None)
        _v = yclick if yclick is not None else _v
        if _v is not None:
            self["yclick"] = _v
        _v = arg.pop("yref", None)
        _v = yref if yref is not None else _v
        if _v is not None:
            self["yref"] = _v
        _v = arg.pop("yshift", None)
        _v = yshift if yshift is not None else _v
        if _v is not None:
            self["yshift"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
