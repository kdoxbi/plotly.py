import _plotly_utils.basevalidators


class UniformtextValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="uniformtext", parent_name="layout", **kwargs):
        super(UniformtextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Uniformtext"),
            **kwargs,
        )
