import _plotly_utils.basevalidators


class ColorbarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="colorbar", parent_name="heatmap", **kwargs):
        super(ColorbarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ColorBar"),
            **kwargs,
        )
