import _plotly_utils.basevalidators


class Error_XValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_x", parent_name="scattergl", **kwargs):
        super(Error_XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorX"),
            **kwargs,
        )
