from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Currentvalue(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.slider"
    _path_str = "layout.slider.currentvalue"
    _valid_props = {"font", "offset", "prefix", "suffix", "visible", "xanchor"}

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def offset(self):
        return self["offset"]

    @offset.setter
    def offset(self, val):
        self["offset"] = val

    @property
    def prefix(self):
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    @property
    def suffix(self):
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def xanchor(self):
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        font=None,
        offset=None,
        prefix=None,
        suffix=None,
        visible=None,
        xanchor=None,
        **kwargs,
    ):
        super(Currentvalue, self).__init__("currentvalue")

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
The first argument to the plotly.graph_objs.layout.slider.Currentvalue
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Currentvalue`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("offset", None)
        _v = offset if offset is not None else _v
        if _v is not None:
            self["offset"] = _v
        _v = arg.pop("prefix", None)
        _v = prefix if prefix is not None else _v
        if _v is not None:
            self["prefix"] = _v
        _v = arg.pop("suffix", None)
        _v = suffix if suffix is not None else _v
        if _v is not None:
            self["suffix"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("xanchor", None)
        _v = xanchor if xanchor is not None else _v
        if _v is not None:
            self["xanchor"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
