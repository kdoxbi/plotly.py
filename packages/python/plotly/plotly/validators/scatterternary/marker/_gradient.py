import _plotly_utils.basevalidators


class GradientValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="gradient", parent_name="scatterternary.marker", **kwargs
    ):
        super(GradientValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Gradient"),
            **kwargs,
        )
