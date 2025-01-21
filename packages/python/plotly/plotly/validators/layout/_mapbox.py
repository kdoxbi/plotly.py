import _plotly_utils.basevalidators


class MapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="mapbox", parent_name="layout", **kwargs):
        super(MapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Mapbox"),
            **kwargs,
        )
