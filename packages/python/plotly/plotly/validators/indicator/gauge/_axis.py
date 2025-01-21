import _plotly_utils.basevalidators


class AxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="axis", parent_name="indicator.gauge", **kwargs):
        super(AxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Axis"),
            **kwargs,
        )
