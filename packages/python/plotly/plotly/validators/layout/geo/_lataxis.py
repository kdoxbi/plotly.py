import _plotly_utils.basevalidators


class LataxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="lataxis", parent_name="layout.geo", **kwargs):
        super(LataxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lataxis"),
            **kwargs,
        )
