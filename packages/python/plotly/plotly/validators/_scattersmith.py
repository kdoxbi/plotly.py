import _plotly_utils.basevalidators


class ScattersmithValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattersmith", parent_name="", **kwargs):
        super(ScattersmithValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattersmith"),
            **kwargs,
        )
