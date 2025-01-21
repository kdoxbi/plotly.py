import _plotly_utils.basevalidators


class ColoraxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="coloraxis", parent_name="layout", **kwargs):
        super(ColoraxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Coloraxis"),
            **kwargs,
        )
