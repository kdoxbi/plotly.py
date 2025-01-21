import _plotly_utils.basevalidators


class ScatterternaryValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatterternary", parent_name="", **kwargs):
        super(ScatterternaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterternary"),
            **kwargs,
        )
