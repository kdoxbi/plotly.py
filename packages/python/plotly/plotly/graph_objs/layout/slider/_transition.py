from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Transition(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.slider"
    _path_str = "layout.slider.transition"
    _valid_props = {"duration", "easing"}

    @property
    def duration(self):
        return self["duration"]

    @duration.setter
    def duration(self, val):
        self["duration"] = val

    @property
    def easing(self):
        return self["easing"]

    @easing.setter
    def easing(self, val):
        self["easing"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, duration=None, easing=None, **kwargs):
        super(Transition, self).__init__("transition")

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
The first argument to the plotly.graph_objs.layout.slider.Transition
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Transition`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("duration", None)
        _v = duration if duration is not None else _v
        if _v is not None:
            self["duration"] = _v
        _v = arg.pop("easing", None)
        _v = easing if easing is not None else _v
        if _v is not None:
            self["easing"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
