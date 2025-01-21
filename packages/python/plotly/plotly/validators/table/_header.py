import _plotly_utils.basevalidators


class HeaderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="header", parent_name="table", **kwargs):
        super(HeaderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Header"),
            **kwargs,
        )
