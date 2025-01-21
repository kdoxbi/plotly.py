import _plotly_utils.basevalidators


class ViolinValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="violin", parent_name="", **kwargs):
        super(ViolinValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Violin"),
            **kwargs,
        )
