import _plotly_utils.basevalidators


class LabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="label", parent_name="layout.shape", **kwargs):
        super(LabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Label"),
            **kwargs,
        )
