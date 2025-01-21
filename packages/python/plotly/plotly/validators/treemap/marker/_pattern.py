import _plotly_utils.basevalidators


class PatternValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pattern", parent_name="treemap.marker", **kwargs):
        super(PatternValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pattern"),
            **kwargs,
        )
