import _plotly_utils.basevalidators


class MapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="map", parent_name="layout", **kwargs):
        super(MapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Map"),
            **kwargs,
        )
