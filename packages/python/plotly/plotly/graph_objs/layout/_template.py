from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Template(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.template"
    _valid_props = {"data", "layout"}

    @property
    def data(self):
        return self["data"]

    @data.setter
    def data(self, val):
        self["data"] = val

    @property
    def layout(self):
        return self["layout"]

    @layout.setter
    def layout(self, val):
        self["layout"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, data=None, layout=None, **kwargs):
        super(Template, self).__init__("template")

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
The first argument to the plotly.graph_objs.layout.Template
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Template`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("data", None)
        _v = data if data is not None else _v
        if _v is not None:
            self["data"] = _v
        _v = arg.pop("layout", None)
        _v = layout if layout is not None else _v
        if _v is not None:
            self["layout"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
