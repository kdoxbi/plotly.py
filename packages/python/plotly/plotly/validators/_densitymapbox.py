import _plotly_utils.basevalidators


class DensitymapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="densitymapbox", parent_name="", **kwargs):
        super(DensitymapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Densitymapbox"),
            **kwargs,
        )
