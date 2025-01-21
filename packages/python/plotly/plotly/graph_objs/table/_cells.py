from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cells(_BaseTraceHierarchyType):

    _parent_path_str = "table"
    _path_str = "table.cells"
    _valid_props = {
        "align",
        "alignsrc",
        "fill",
        "font",
        "format",
        "formatsrc",
        "height",
        "line",
        "prefix",
        "prefixsrc",
        "suffix",
        "suffixsrc",
        "values",
        "valuessrc",
    }

    @property
    def align(self):
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    @property
    def alignsrc(self):
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    @property
    def fill(self):
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def format(self):
        return self["format"]

    @format.setter
    def format(self, val):
        self["format"] = val

    @property
    def formatsrc(self):
        return self["formatsrc"]

    @formatsrc.setter
    def formatsrc(self, val):
        self["formatsrc"] = val

    @property
    def height(self):
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def prefix(self):
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    @property
    def prefixsrc(self):
        return self["prefixsrc"]

    @prefixsrc.setter
    def prefixsrc(self, val):
        self["prefixsrc"] = val

    @property
    def suffix(self):
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    @property
    def suffixsrc(self):
        return self["suffixsrc"]

    @suffixsrc.setter
    def suffixsrc(self, val):
        self["suffixsrc"] = val

    @property
    def values(self):
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    @property
    def valuessrc(self):
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        fill=None,
        font=None,
        format=None,
        formatsrc=None,
        height=None,
        line=None,
        prefix=None,
        prefixsrc=None,
        suffix=None,
        suffixsrc=None,
        values=None,
        valuessrc=None,
        **kwargs,
    ):
        super(Cells, self).__init__("cells")

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
The first argument to the plotly.graph_objs.table.Cells
constructor must be a dict or
an instance of :class:`plotly.graph_objs.table.Cells`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("align", None)
        _v = align if align is not None else _v
        if _v is not None:
            self["align"] = _v
        _v = arg.pop("alignsrc", None)
        _v = alignsrc if alignsrc is not None else _v
        if _v is not None:
            self["alignsrc"] = _v
        _v = arg.pop("fill", None)
        _v = fill if fill is not None else _v
        if _v is not None:
            self["fill"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("format", None)
        _v = format if format is not None else _v
        if _v is not None:
            self["format"] = _v
        _v = arg.pop("formatsrc", None)
        _v = formatsrc if formatsrc is not None else _v
        if _v is not None:
            self["formatsrc"] = _v
        _v = arg.pop("height", None)
        _v = height if height is not None else _v
        if _v is not None:
            self["height"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("prefix", None)
        _v = prefix if prefix is not None else _v
        if _v is not None:
            self["prefix"] = _v
        _v = arg.pop("prefixsrc", None)
        _v = prefixsrc if prefixsrc is not None else _v
        if _v is not None:
            self["prefixsrc"] = _v
        _v = arg.pop("suffix", None)
        _v = suffix if suffix is not None else _v
        if _v is not None:
            self["suffix"] = _v
        _v = arg.pop("suffixsrc", None)
        _v = suffixsrc if suffixsrc is not None else _v
        if _v is not None:
            self["suffixsrc"] = _v
        _v = arg.pop("values", None)
        _v = values if values is not None else _v
        if _v is not None:
            self["values"] = _v
        _v = arg.pop("valuessrc", None)
        _v = valuessrc if valuessrc is not None else _v
        if _v is not None:
            self["valuessrc"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
