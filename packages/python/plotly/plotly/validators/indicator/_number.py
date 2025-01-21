import _plotly_utils.basevalidators


class NumberValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="number", parent_name="indicator", **kwargs):
        super(NumberValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Number"),
            **kwargs,
        )
