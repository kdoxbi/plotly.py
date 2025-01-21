import _plotly_utils.basevalidators


class TernaryValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="ternary", parent_name="layout", **kwargs):
        super(TernaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Ternary"),
            **kwargs,
        )
