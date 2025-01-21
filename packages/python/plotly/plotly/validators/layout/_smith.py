import _plotly_utils.basevalidators


class SmithValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="smith", parent_name="layout", **kwargs):
        super(SmithValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Smith"),
            **kwargs,
        )
