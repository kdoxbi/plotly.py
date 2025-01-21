import _plotly_utils.basevalidators


class ScattercarpetValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattercarpet", parent_name="", **kwargs):
        super(ScattercarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattercarpet"),
            **kwargs,
        )
