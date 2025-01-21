import _plotly_utils.basevalidators


class Scatter3DValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatter3d", parent_name="", **kwargs):
        super(Scatter3DValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatter3d"),
            **kwargs,
        )
