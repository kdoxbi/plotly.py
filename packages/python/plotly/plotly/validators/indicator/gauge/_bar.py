import _plotly_utils.basevalidators


class BarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="bar", parent_name="indicator.gauge", **kwargs):
        super(BarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Bar"),
            **kwargs,
        )
