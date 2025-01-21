from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Legend(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.legend"
    _valid_props = {
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "entrywidth",
        "entrywidthmode",
        "font",
        "groupclick",
        "grouptitlefont",
        "indentation",
        "itemclick",
        "itemdoubleclick",
        "itemsizing",
        "itemwidth",
        "orientation",
        "title",
        "tracegroupgap",
        "traceorder",
        "uirevision",
        "valign",
        "visible",
        "x",
        "xanchor",
        "xref",
        "y",
        "yanchor",
        "yref",
    }

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
    def entrywidth(self):
        return self["entrywidth"]

    @entrywidth.setter
    def entrywidth(self, val):
        self["entrywidth"] = val

    @property
    def entrywidthmode(self):
        return self["entrywidthmode"]

    @entrywidthmode.setter
    def entrywidthmode(self, val):
        self["entrywidthmode"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def groupclick(self):
        return self["groupclick"]

    @groupclick.setter
    def groupclick(self, val):
        self["groupclick"] = val

    @property
    def grouptitlefont(self):
        return self["grouptitlefont"]

    @grouptitlefont.setter
    def grouptitlefont(self, val):
        self["grouptitlefont"] = val

    @property
    def indentation(self):
        return self["indentation"]

    @indentation.setter
    def indentation(self, val):
        self["indentation"] = val

    @property
    def itemclick(self):
        return self["itemclick"]

    @itemclick.setter
    def itemclick(self, val):
        self["itemclick"] = val

    @property
    def itemdoubleclick(self):
        return self["itemdoubleclick"]

    @itemdoubleclick.setter
    def itemdoubleclick(self, val):
        self["itemdoubleclick"] = val

    @property
    def itemsizing(self):
        return self["itemsizing"]

    @itemsizing.setter
    def itemsizing(self, val):
        self["itemsizing"] = val

    @property
    def itemwidth(self):
        return self["itemwidth"]

    @itemwidth.setter
    def itemwidth(self, val):
        self["itemwidth"] = val

    @property
    def orientation(self):
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def title(self):
        return self["title"]

    @title.setter
    def title(self, val):
        self["title"] = val

    @property
    def tracegroupgap(self):
        return self["tracegroupgap"]

    @tracegroupgap.setter
    def tracegroupgap(self, val):
        self["tracegroupgap"] = val

    @property
    def traceorder(self):
        return self["traceorder"]

    @traceorder.setter
    def traceorder(self, val):
        self["traceorder"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

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
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        entrywidth=None,
        entrywidthmode=None,
        font=None,
        groupclick=None,
        grouptitlefont=None,
        indentation=None,
        itemclick=None,
        itemdoubleclick=None,
        itemsizing=None,
        itemwidth=None,
        orientation=None,
        title=None,
        tracegroupgap=None,
        traceorder=None,
        uirevision=None,
        valign=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs,
    ):
        super(Legend, self).__init__("legend")

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
The first argument to the plotly.graph_objs.layout.Legend
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Legend`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

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
        _v = arg.pop("entrywidth", None)
        _v = entrywidth if entrywidth is not None else _v
        if _v is not None:
            self["entrywidth"] = _v
        _v = arg.pop("entrywidthmode", None)
        _v = entrywidthmode if entrywidthmode is not None else _v
        if _v is not None:
            self["entrywidthmode"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("groupclick", None)
        _v = groupclick if groupclick is not None else _v
        if _v is not None:
            self["groupclick"] = _v
        _v = arg.pop("grouptitlefont", None)
        _v = grouptitlefont if grouptitlefont is not None else _v
        if _v is not None:
            self["grouptitlefont"] = _v
        _v = arg.pop("indentation", None)
        _v = indentation if indentation is not None else _v
        if _v is not None:
            self["indentation"] = _v
        _v = arg.pop("itemclick", None)
        _v = itemclick if itemclick is not None else _v
        if _v is not None:
            self["itemclick"] = _v
        _v = arg.pop("itemdoubleclick", None)
        _v = itemdoubleclick if itemdoubleclick is not None else _v
        if _v is not None:
            self["itemdoubleclick"] = _v
        _v = arg.pop("itemsizing", None)
        _v = itemsizing if itemsizing is not None else _v
        if _v is not None:
            self["itemsizing"] = _v
        _v = arg.pop("itemwidth", None)
        _v = itemwidth if itemwidth is not None else _v
        if _v is not None:
            self["itemwidth"] = _v
        _v = arg.pop("orientation", None)
        _v = orientation if orientation is not None else _v
        if _v is not None:
            self["orientation"] = _v
        _v = arg.pop("title", None)
        _v = title if title is not None else _v
        if _v is not None:
            self["title"] = _v
        _v = arg.pop("tracegroupgap", None)
        _v = tracegroupgap if tracegroupgap is not None else _v
        if _v is not None:
            self["tracegroupgap"] = _v
        _v = arg.pop("traceorder", None)
        _v = traceorder if traceorder is not None else _v
        if _v is not None:
            self["traceorder"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("valign", None)
        _v = valign if valign is not None else _v
        if _v is not None:
            self["valign"] = _v
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
