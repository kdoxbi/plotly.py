import _plotly_utils.basevalidators


class BoundsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="bounds", parent_name="layout.mapbox", **kwargs):
        super(BoundsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Bounds"),
            **kwargs,
        )
