import _plotly_utils.basevalidators


class SelectionsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="selections", parent_name="layout", **kwargs):
        super(SelectionsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Selection"),
            **kwargs,
        )
