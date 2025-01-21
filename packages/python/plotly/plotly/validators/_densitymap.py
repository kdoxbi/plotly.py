import _plotly_utils.basevalidators


class DensitymapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="densitymap", parent_name="", **kwargs):
        super(DensitymapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Densitymap"),
            **kwargs,
        )
