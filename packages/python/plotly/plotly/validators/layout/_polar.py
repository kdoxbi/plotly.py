import _plotly_utils.basevalidators


class PolarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="polar", parent_name="layout", **kwargs):
        super(PolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Polar"),
            **kwargs,
        )
