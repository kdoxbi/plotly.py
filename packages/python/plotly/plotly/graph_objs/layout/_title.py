from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Title(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.title"
    _valid_props = {
        "automargin",
        "font",
        "pad",
        "subtitle",
        "text",
        "x",
        "xanchor",
        "xref",
        "y",
        "yanchor",
        "yref",
    }

    @property
    def automargin(self):
        return self["automargin"]

    @automargin.setter
    def automargin(self, val):
        self["automargin"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def pad(self):
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    @property
    def subtitle(self):
        return self["subtitle"]

    @subtitle.setter
    def subtitle(self, val):
        self["subtitle"] = val

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

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
        automargin=None,
        font=None,
        pad=None,
        subtitle=None,
        text=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs,
    ):
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.layout.Title
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Title`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("automargin", None)
        _v = automargin if automargin is not None else _v
        if _v is not None:
            self["automargin"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("pad", None)
        _v = pad if pad is not None else _v
        if _v is not None:
            self["pad"] = _v
        _v = arg.pop("subtitle", None)
        _v = subtitle if subtitle is not None else _v
        if _v is not None:
            self["subtitle"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
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
