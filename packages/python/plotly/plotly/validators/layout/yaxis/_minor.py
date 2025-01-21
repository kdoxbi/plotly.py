import _plotly_utils.basevalidators


class MinorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="minor", parent_name="layout.yaxis", **kwargs):
        super(MinorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Minor"),
            **kwargs,
        )
