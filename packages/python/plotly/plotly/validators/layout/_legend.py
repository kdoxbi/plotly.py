import _plotly_utils.basevalidators


class LegendValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="legend", parent_name="layout", **kwargs):
        super(LegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Legend"),
            **kwargs,
        )
