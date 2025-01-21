import _plotly_utils.basevalidators


class ScatterpolarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatterpolar", parent_name="", **kwargs):
        super(ScatterpolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterpolar"),
            **kwargs,
        )
