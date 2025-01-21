import _plotly_utils.basevalidators


class FillpatternValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="fillpattern", parent_name="scatter", **kwargs):
        super(FillpatternValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Fillpattern"),
            **kwargs,
        )
