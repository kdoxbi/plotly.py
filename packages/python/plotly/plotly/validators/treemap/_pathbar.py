import _plotly_utils.basevalidators


class PathbarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pathbar", parent_name="treemap", **kwargs):
        super(PathbarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pathbar"),
            **kwargs,
        )
