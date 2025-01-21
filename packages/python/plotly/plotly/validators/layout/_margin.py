import _plotly_utils.basevalidators


class MarginValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="margin", parent_name="layout", **kwargs):
        super(MarginValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Margin"),
            **kwargs,
        )
