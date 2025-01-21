import _plotly_utils.basevalidators


class ThresholdValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="threshold", parent_name="indicator.gauge", **kwargs
    ):
        super(ThresholdValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Threshold"),
            **kwargs,
        )
