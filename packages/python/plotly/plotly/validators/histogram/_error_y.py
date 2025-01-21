import _plotly_utils.basevalidators


class Error_YValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_y", parent_name="histogram", **kwargs):
        super(Error_YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorY"),
            **kwargs,
        )
