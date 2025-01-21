import _plotly_utils.basevalidators


class Error_ZValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_z", parent_name="scatter3d", **kwargs):
        super(Error_ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorZ"),
            **kwargs,
        )
