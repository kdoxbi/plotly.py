import _plotly_utils.basevalidators


class RootValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="root", parent_name="treemap", **kwargs):
        super(RootValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Root"),
            **kwargs,
        )
