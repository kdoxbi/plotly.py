import _plotly_utils.basevalidators


class ScatterglValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattergl", parent_name="", **kwargs):
        super(ScatterglValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattergl"),
            **kwargs,
        )
