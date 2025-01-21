import _plotly_utils.basevalidators


class FillgradientValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="fillgradient", parent_name="scatter", **kwargs):
        super(FillgradientValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Fillgradient"),
            **kwargs,
        )
