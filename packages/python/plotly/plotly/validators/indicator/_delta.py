import _plotly_utils.basevalidators


class DeltaValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="delta", parent_name="indicator", **kwargs):
        super(DeltaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Delta"),
            **kwargs,
        )
