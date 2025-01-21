from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Modebar(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.modebar"
    _valid_props = {
        "activecolor",
        "add",
        "addsrc",
        "bgcolor",
        "color",
        "orientation",
        "remove",
        "removesrc",
        "uirevision",
    }

    @property
    def activecolor(self):
        return self["activecolor"]

    @activecolor.setter
    def activecolor(self, val):
        self["activecolor"] = val

    @property
    def add(self):
        return self["add"]

    @add.setter
    def add(self, val):
        self["add"] = val

    @property
    def addsrc(self):
        return self["addsrc"]

    @addsrc.setter
    def addsrc(self, val):
        self["addsrc"] = val

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def orientation(self):
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def remove(self):
        return self["remove"]

    @remove.setter
    def remove(self, val):
        self["remove"] = val

    @property
    def removesrc(self):
        return self["removesrc"]

    @removesrc.setter
    def removesrc(self, val):
        self["removesrc"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        activecolor=None,
        add=None,
        addsrc=None,
        bgcolor=None,
        color=None,
        orientation=None,
        remove=None,
        removesrc=None,
        uirevision=None,
        **kwargs,
    ):
        super(Modebar, self).__init__("modebar")

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
The first argument to the plotly.graph_objs.layout.Modebar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Modebar`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("activecolor", None)
        _v = activecolor if activecolor is not None else _v
        if _v is not None:
            self["activecolor"] = _v
        _v = arg.pop("add", None)
        _v = add if add is not None else _v
        if _v is not None:
            self["add"] = _v
        _v = arg.pop("addsrc", None)
        _v = addsrc if addsrc is not None else _v
        if _v is not None:
            self["addsrc"] = _v
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("orientation", None)
        _v = orientation if orientation is not None else _v
        if _v is not None:
            self["orientation"] = _v
        _v = arg.pop("remove", None)
        _v = remove if remove is not None else _v
        if _v is not None:
            self["remove"] = _v
        _v = arg.pop("removesrc", None)
        _v = removesrc if removesrc is not None else _v
        if _v is not None:
            self["removesrc"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
