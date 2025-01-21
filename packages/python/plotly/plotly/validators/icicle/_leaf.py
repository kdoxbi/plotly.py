import _plotly_utils.basevalidators


class LeafValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="leaf", parent_name="icicle", **kwargs):
        super(LeafValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Leaf"),
            **kwargs,
        )
